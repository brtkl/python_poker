# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:26:14 2021

@author: brtk
"""

class Strategy:  
    """ defining strategy methods that players can use"""
    def __init__(self, player, round_):
        self.player=player
        self.round_=round_
        
    def strat(self, stage):
        # if stage=='pre-flop':
            if self.player.bet <= self.round_.maxbet:
                if self.player.probwin>0.6:
                    self.player.raise_(self.round_.minraise)
                    print(f'Player {self.player.name} raises by {self.round_.minraise}')
                elif self.player.probwin>=0.4 or self.player.bet==self.round_.maxbet:
                    self.player.check()
                    print(f'Player {self.player.name} checks')
                else:
                    self.player.fold()
                    print(f'Player {self.player.name} folds')
