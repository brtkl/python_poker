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
    def __init__(self, players, mode='sim', maxrounds=20, simnum_prob=10000):
        self.players_init=players
        self.players_active=[Player(p) for p in players]
        self.maxrounds=maxrounds
        self.mode=mode
        self.button_idx=0
        self.simnum_prob=simnum_prob
    
    def display_balances(self):
        for p in self.players_active:
            print(f"{p.name} balance: {p.balance}")
    
    def play(self):
        n=1
        while(len(self.players_active)>1 and n<=self.maxrounds):
            r=Round(self)
            for p in self.players_active[:]:
                p.prepare_for_round(r)
            print(f"\nRound {n} begins")
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
                    if p is self.players_active[self.button_idx]:
                        button_rem=1
                    self.players_active.remove(p)
            self.button_idx=(self.button_idx+1-button_rem) % len(self.players_active)
            n+=1
        
        

g=Game(['brtkl', 'comp'], simnum_prob=1000)

g.play()
