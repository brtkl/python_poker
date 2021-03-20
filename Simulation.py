# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:56:58 2021

@author: brtk
"""

from Game import Game
from Player import Player
import random

class Simulation():
    """simulating multiple games and presenting results"""
    def __init__(self
                 , players
                 , ngames=100
                 , maxrounds=100
                 , console_print='N'
                 , simnum_prob=2000
                 , sblind=5
                 , bblind=10
                 , button='random'):
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
        if console_print not in ['Y', 'N']:
            raise ValueError('console_print can be Y or N')
            
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
                   , console_print='N'
                   , sblind=self.sblind
                   , bblind=self.bblind
                   , button_idx=self.button_idx
                   )
            
            g.assign_players(self.players_sim_init
                             , restart_balance='Y'
                             )
            g.play()
            for p in self.players_sim_init:
                p.simulation_results+=p.balance
            if self.console_print=='Y':
                print(f'\nStatus after game {i}')
                self.summary()
    
    def summary(self):
        for p in self.players_sim_init:
            print(f'{p.name}/{p.strat}: {p.simulation_results}  bb/100: '
                  +f'{p.bb100}  nrounds: {p.hands_played}')
        
    