# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:49:04 2021

@author: brtk
"""

import _util_pickl
import _util_managedb
from Simulation import Simulation

class Training():
    """training of strategies/players"""
    
    def __init__(self
                 , players_to_load
                 , ngames=100
                 , maxrounds=100
                 , console_print='N'
                 , simnum_prob=2000
                 , sblind=5
                 , bblind=10
                 , balance_game_init=1000
                 , button='random'
                 ):
        self.players_to_load=players_to_load
        self.players_loaded=[]
        self.ngames=ngames
        self.maxrounds=maxrounds
        self.console_print=console_print
        self.simnum_prob=simnum_prob
        self.bblind=bblind
        self.sblind=sblind
        self.balance_game_init=balance_game_init
        self.button=button
    
    def train_pickl(self, update_results='Y'):
        for p in self.players_to_load:
            tmp=_util_pickl.load_player(p)
            tmp.balance_game_init=self.balance_game_init
            self.players_loaded.append(tmp)
        s=Simulation(None
                    , ngames=self.ngames
                    , maxrounds=self.maxrounds
                    , console_print='N'
                    , trainmode='Y'
                    , simnum_prob=self.simnum_prob
                    , sblind=self.sblind
                    , bblind=self.bblind
                    , button=self.button
                    )
        s.assign_players(self.players_loaded)
        s.run_sim()
        s.summary()
        if update_results=='Y':
            for p in self.players_loaded:
                _util_pickl.save_player(p, overwrite='Y')
                
                
    def train(self, update_results='Y'):
        for p in self.players_to_load:
            tmp=_util_managedb.recreate_player(p)
            tmp.balance_game_init=self.balance_game_init
            self.players_loaded.append(tmp)
        s=Simulation(None
                    , ngames=self.ngames
                    , maxrounds=self.maxrounds
                    , console_print='N'
                    , trainmode='Y'
                    , simnum_prob=self.simnum_prob
                    , sblind=self.sblind
                    , bblind=self.bblind
                    , button=self.button
                    )
        s.assign_players(self.players_loaded)
        s.run_sim()
        s.summary()
        if update_results=='Y':
            for p in self.players_loaded:
                _util_managedb.save_stats(p)
        