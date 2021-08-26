# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:56:58 2021

@author: brtk
"""

from Game import Game
from Player import Player
import random
import pandas
from _util_managedb import save_log

class Simulation():
    """simulating multiple games and presenting results"""
    def __init__(self
                 , players
                 , ngames=100
                 , maxrounds=100
                 , console_print=False
                 , trainmode=False
                 , simnum_prob=2000
                 , sblind=5
                 , bblind=10
                 , button='random'
                 , log=True
                 , logsql=True):
        self.players_sim_init=[]
        self.button_meth=button
        if players != None and len(players)>0:
            for p in players:
                self.players_sim_init.append(Player(p))
            if button=='random':
                self.button_idx=random.choice(range(len(self.players_sim_init)))
            else:
                self.button_idx=0
        self.ngames=ngames
        self.maxrounds=maxrounds
        self.console_print=console_print
        self.simnum_prob=simnum_prob
        self.bblind=bblind
        self.sblind=sblind
        self.trainmode=trainmode
        self.log=log
        self.logsql=logsql
        self.listres_sim=[]
        if type(console_print) != type(True):
            raise ValueError('console_print should be boolean')
            
    def assign_players(self
                       , players_obj
                       ):
        """to be used when Players not created in Simulation instance"""
        if self.players_sim_init:
            raise ValueError('Some players already defined for a Simulation')
        if len(players_obj)>0 and players_obj not in (None,''):
            for p in players_obj:
                self.players_sim_init.append(p)
            if self.button_meth=='random':
                self.button_idx=random.choice(range(len(self.players_sim_init)))
            else:
                self.button_idx=0
            
        
    def run_sim(self):
        for i in range(1,self.ngames+1):
            g=Game(None
                   , maxrounds=self.maxrounds
                   , simnum_prob=self.simnum_prob
                   , console_print=False
                   , sblind=self.sblind
                   , bblind=self.bblind
                   , button_idx=self.button_idx
                   )
            
            if i==1:
                tmpord=False
            else:
                tmpord=True
            
            g.assign_players(self.players_sim_init
                             , restart_balance=True
                             , reorder_players=tmpord
                             )
            g.play()
            # for p in self.players_sim_init:
            #     p.simulation_results+=p.balance
            if self.console_print:
                print(f'\nStatus after game {i}')
                self.summary()
            if self.trainmode:
                if i % round(self.ngames/10)==0 or i==self.ngames:
                    print(f'{round((i/self.ngames)*100)}% completed ')
            if self.log:
                self.listres_sim+=g.listres
                
        if self.log:
            self.df_log=pandas.DataFrame(self.listres_sim)
            if self.logsql:
                save_log(self.df_log)
    
    def summary(self):
        for p in self.players_sim_init:
            print(f'{p.name}/{p.strat}: bb/100: {p.bb100}, bbwon: {p.bb_won}, '
                  +f'nrounds: {p.hands_played}')
        
    