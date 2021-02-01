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
    def __init__(self, players, mode='sim', maxrounds=100):
        self.players_init=players
        self.players_active=[Player(p) for p in players]
        self.maxrounds=maxrounds
        self.mode=mode
        
    def play(self):
        n=0
        while(len(self.players_active)>0 and n<=self.maxrounds):
            r=Round(self)
            for p in self.players_active:
                if p.balance<=0:
                    self.players_active.remove(p)
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
        
        



