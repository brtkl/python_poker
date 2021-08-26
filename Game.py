# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:32:25 2021

@author: brtk
"""

# import os
# os.chdir(r'C:\_D\FX\_GLOBAL\learning\python\poker')

from Round import Round
from Player import Player
import pandas
from random import shuffle
import uuid
from _util_managedb import save_log


class Game():
    """ Game class - main mode"""
    def __init__(self
                 , players
                 , mode='sim' #sim or interactive
                 , maxrounds=20
                 , console_print=True
                 , simnum_prob=10000
                 , sblind=5
                 , bblind=10
                 , round_req={}
                 , button_idx=0 
                 , log=True
                 , logsql=False
                 ):
        self.id=str(uuid.uuid1())
        self.players_active=[]
        if players != None and len(players)>0:
            for p in players:
                self.players_active.append(Player(p))
        self.flop_req=round_req['flop'] if 'flop' in round_req else []
        self.turn_req=round_req['turn'] if 'turn' in round_req else []
        self.river_req=round_req['river'] if 'river' in round_req else []
        self.maxrounds=maxrounds
        self.console_print=console_print
        self.mode=mode
        self.button_idx=button_idx
        self.simnum_prob=simnum_prob
        self.bblind=bblind
        self.sblind=sblind
        self.players_init=self.players_active[:]
        self.log=log
        self.logsql=logsql
        self.listres=[]
        if self.players_active:
            self.remove_notenough_sb_on_bb()
            if not (2<=len(self.players_active)<=10):
                raise ValueError('between 2 and 10 valid players need to be'
                                 +' defined')
            if not (0<=button_idx<=len(self.players_active)-1):
                raise ValueError('starting button_idx incorrect')
        if type(console_print) != type(True):
            raise ValueError('console_print should be boolean')
        if mode not in ['sim', 'interactive']:
            raise ValueError('mode can be sim or ineractive')
            
    def assign_players(self
                       , players_obj
                       , restart_balance=False
                       , reorder_players=False
                       ):
        """to be used when Players not created in Game instance"""
        if self.players_active:
            raise ValueError('Some players already defined for a game')
        if len(players_obj)>0 and players_obj not in (None,''):
            if reorder_players:
                shuffle(players_obj)
            for p in players_obj:
                self.players_active.append(p)
                if restart_balance:
                    p.balance=p.balance_game_init
        self.players_init=self.players_active[:]
        self.remove_notenough_sb_on_bb()
        if not (2<=len(self.players_active)<=10):
            raise ValueError('between 2 and 10 valid players need to be'
                             +' assigned')
        if not (0<=self.button_idx<=len(self.players_active)-1):
            raise ValueError('starting button_idx incorrect')
    
    def print_c(self, val):
        if self.console_print:
            print(val)
    
    def display_balances(self):
        for p in self.players_active:
            self.print_c(f"{p.name} balance: {p.balance}")
            
    def remove_notenough_sb_on_bb(self):
        """removing player on bblind spot who has less than sblind amount"""
        tmp_2play=1 if len(self.players_active)==2 else 0
        bbpl=self.players_active[(self.button_idx+2-tmp_2play) % 
                                 len(self.players_active)]
        button_rem=0
        if bbpl.balance<self.sblind:
            if self.players_active.index(bbpl)<=self.button_idx:
                button_rem=1
                #if players before button were eliminated we need 
                #to go back with the new button idx since it takes
                #into account players_active only.
                #e.g. 5 players, no 4 was button.
                #players 2 and 4 are eliminated
                #new button should be no 5 but its now the 3rd player
                #in the new players_active list, so 4+1-2
            self.players_active.remove(bbpl)
            self.button_idx=(self.button_idx-button_rem) % len(self.players_active)
    
    def play(self):
        n=1
        while(10>=len(self.players_active)>1 and n<=self.maxrounds):
            r=Round(self, sblind=self.sblind, bblind=self.bblind)
            self.print_c("#####################################\n##Round"+
                         f" {n} begins")
            for p in self.players_active[:]:
                p.prepare_for_round(r)
            r.assigncards()
            r.assignblinds()
            #pre-flop bets
            r.betting(n_r=n, log=self.log, listsave=self.listres)
            #flop bets
            r.nextstage('flop')
            r.betting(n_r=n, log=self.log, listsave=self.listres)
            #turn bets
            r.nextstage('turn')
            r.betting(n_r=n, log=self.log, listsave=self.listres)
            #river bets
            r.nextstage('river')
            r.betting(n_r=n, log=self.log, listsave=self.listres)
            r.finalizeround(n_r=n, log=self.log, listsave=self.listres)
                        
            self.display_balances()
            
            button_rem=0
            for p in self.players_active[:]:
                if p.balance<=0:
                    if self.players_active.index(p)<=self.button_idx:
                        button_rem+=1
                        #if players before button were eliminated we need 
                        #to go back with the new button idx since it takes
                        #into account players_active only.
                        #e.g. 5 players, no 4 was button.
                        #players 2 and 4 are eliminated
                        #new button should be no 5 but its now the 3rd player
                        #in the new players_active list, so 4+1-2
                    self.players_active.remove(p)
            self.button_idx=(self.button_idx+1-button_rem) % len(
                self.players_active)
            
            #after new button is determined we need to check whether new 
            #Bblind player has at least Small blind amount. If not, then they 
            #are eliminated and button idx further adjusted if needed
            self.remove_notenough_sb_on_bb()
            n+=1
            
            if self.log and (len(self.players_active)<2 or n>self.maxrounds):
                self.df_log=pandas.DataFrame(self.listres)
                if self.logsql:
                    save_log(self.df_log)

