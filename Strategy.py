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
        allinfn=0
        if stage=='pre-flop':
            thrsh=0.4
        else:
            thrsh=0.45
        if self.player.bet <= self.round_.maxbet:
            checkminbal=min([i.balance for i in self.round_.players_r_active])
            if self.player.balance==0:
                self.player.check() #already all in
            elif self.player.probwin>0.6:
                if checkminbal==0: 
                    if self.player.bet < self.round_.maxbet:
                        self.player.call() #if opp made all in it's sufficient to call
                    else:
                        self.player.check()
                else:
                    propos=self.round_.minraise #replace with Erlang dist?
                    if stage != 'pre-flop' and self.player.probwin>0.8:
                        propos=self.player.balance #go all-in
                        allinfn=1
                    if self.round_.maxbet>=self.player.balance>0 and allinfn==1:
                        self.player.call() #call to all in
                    else:
                        self.player.raise_(
                            max(self.round_.maxbet - self.player.bet + 
                            self.round_.minraise , min(checkminbal, propos)))
                
            elif self.player.probwin>=thrsh and self.player.bet<self.round_.maxbet:
                self.player.call()
                
            elif self.player.bet==self.round_.maxbet:
                self.player.check()
                
            else:
                self.player.fold()
