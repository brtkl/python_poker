# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:43:21 2021

@author: brtk
"""

from Deck import Deck
from eval_hand import eval_hand
from calc_probwin import calc_probwin

class Round():
    """ round of a game. Game consists of rounds, round consist of stages
    (pre-flop, flop, turn, river) """
    def __init__(self, 
                 cur_game, 
                 bblind=10, 
                 sblind=5):
        self.deck=Deck()
        self.deck.shuffle()
        self.bblind=bblind
        self.sblind=sblind
        self.stage='pre-flop'
        self.pot=0
        self.maxbet=0
        self.table=[]
        self.players_r_active=cur_game.players_active[:]
        self.button=cur_game.button_idx
        self.minraise=bblind
        self.simnum_prob=cur_game.simnum_prob
    
    def assigncards(self):
        for p in self.players_r_active:
            p.hand=self.deck.draw(2)
            print(f"{p.name} hand: {p.hand}")
        
    def assignblinds(self):
        lenact=len(self.players_r_active)
        if lenact==2:
            tmp=0
        else:
            tmp=1
        self.players_r_active[(self.button+tmp) % lenact].updatebalance(-self.sblind)
        self.players_r_active[(self.button+1+tmp) % lenact].updatebalance(-self.bblind)
        self.player_ord_preflop=self.players_r_active[
            (self.button+2+tmp) % lenact:]+self.players_r_active[:(self.button+
                                                               2+tmp) % lenact]
        self.player_ord_postflop=self.players_r_active[
            (self.button+1) % lenact:]+self.players_r_active[:(self.button
                                                               +1) % lenact]
        self.pot=self.sblind+self.bblind
        self.maxbet=self.bblind
    
    def betting(self):
        if len(self.players_r_active)>1:
            n=0
            for p in self.players_r_active:
                    p.probwin=round(calc_probwin(p.hand, self.table, 
                                                 simnum=self.simnum_prob)[0],2)
            if self.stage == 'pre-flop':
               tmp=self.player_ord_preflop
            else:
               tmp=self.player_ord_postflop
            while((min([i.bet for i in self.players_r_active if i.balance!=0]
                       +[self.maxbet]) != self.maxbet) or n<1):
                for p in tmp:
                    if len(self.players_r_active)>1 and (p.bet<self.maxbet or 
                                                         n<1) and p.folded==0:
                        p.strategy.strat(self.stage)
                n+=1
    
    def nextstage(self,newstage):
        if newstage not in ['flop','turn','river']:
            return ['newstage needs to be flop, turn or river']
        
        if ((self.stage=='pre-flop' and newstage != 'flop') or 
            (self.stage=='flop' and newstage != 'turn') or
            (self.stage=='turn' and newstage != 'river')):
            return ['wrong order of stages']
        
        if len(self.players_r_active)>1:
            self.stage=newstage
            if newstage=='flop':
                self.table=self.deck.draw(3)
            elif newstage=='turn':
                self.table+=self.deck.draw(1)
            elif newstage=='river':
                self.table+=self.deck.draw(1)
            print(f"{newstage}: {self.table}")
            
    
    def finalizeround(self):
        if len(self.players_r_active)==1:
            print(f"{self.players_r_active[0].name} wins, opponents folded")
            self.players_r_active[0].updatebalance(self.pot, balanceonly=1)
        else:
            maxhand=max([eval_hand(i.hand+self.table) for i in self.players_r_active])
            winplay=[i for i in self.players_r_active if 
                     eval_hand(i.hand+self.table)==maxhand]
            if len(winplay)==1:
                winplay[0].updatebalance(self.pot, balanceonly=1)
                print(f"{winplay[0].name} wins having {winplay[0].hand}")
            elif len(winplay)>1:
                for i in winplay:
                    i.updatebalance(self.pot/len(winplay), balanceonly=1)
                    print(f"{i.name} drew having {i.hand}")
            
    