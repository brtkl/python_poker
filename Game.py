# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:32:25 2021

@author: brtk
"""

import os
os.chdir(r'D:\FX\_GLOBAL\learning\python\poker')

from Round import Round
from Player import Player


class Game():
    """ Game class - main mode"""
    def __init__(self, players, mode='sim', maxrounds=20, simnum_prob=10000
                 , sblind=5, bblind=10):
        self.players_init=players
        self.players_active=[]
        for p in players:
            if isinstance(p, str):
                self.players_active.append(Player(p))
            elif isinstance(p, dict): 
                tmp=Player(p['name'])
                self.players_active.append(tmp)
                if 'balance' in p:
                    tmp.balance=p['balance']
                if 'cards' in p:
                    tmp.cards_req=p['cards']
                if 'strat' in p:
                    tmp.strategy=p['strat']
        self.maxrounds=maxrounds
        self.mode=mode
        self.button_idx=0
        self.simnum_prob=simnum_prob
        self.bblind=bblind
        self.sblind=sblind
        if self.players_active[(self.button_idx+2) % len(self.players_active)
                               ].balance<sblind:
            del self.players_active[self.button_idx+2]
            #removing player on bblind spot who has less than sblind amount
        if not (2<=len(self.players_active)<=10):
            print('ERROR: between 2 and 10 valid players need to be defined')
    
    def display_balances(self):
        for p in self.players_active:
            print(f"{p.name} balance: {p.balance}")
    
    def play(self):
        n=1
        while(10>=len(self.players_active)>1 and n<=self.maxrounds):
            r=Round(self, sblind=self.sblind, bblind=self.bblind)
            print(f"\nRound {n} begins")
            for p in self.players_active[:]:
                p.prepare_for_round(r)
            r.assigncards()
            r.assignblinds()
            #pre-flop bets
            r.betting()
            #flop bets
            r.nextstage('flop')
            r.betting()
            #turn bets
            r.nextstage('turn')
            r.betting()
            #river bets
            r.nextstage('river')
            r.betting()
            r.finalizeround()
                        
            self.display_balances()
            button_rem=0
            
            for p in self.players_active[:]:
                if p.balance<=0:
                    if self.players_active.index(p)==self.button_idx:
                        button_rem=1
                        #if button lost everything we don't add +1 to self.button_idx
                    self.players_active.remove(p)
            self.button_idx=(self.button_idx+1-button_rem) % len(self.players_active)
            
            #after new button is determined we need to check whether new Bblind
            #player has at least Small blind amount. If not, then they are eliminated
            bbpl=self.players_active[(self.button_idx+2) % len(self.players_active)]
            if bbpl.balance<self.sblind:
                self.players_active.remove(bbpl)
            n+=1


#g=Game([{'name':'brtkl', 'balance':1000, 'cards'=[]},
#        {'name':'c1', 'balance':1000, 'cards'=[]},
#        {'name':'c2', 'balance':1000, 'cards'=[]}])
#
#g.play()
