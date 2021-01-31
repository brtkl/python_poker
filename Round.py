# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:43:21 2021

@author: brtk
"""

from Player import Player
from Deck import Deck
from eval_hand import eval_hand

class Round():
    """ round of a game. Game consists of rounds, round consist of stages
    (pre-flop, flop, turn, river) """
    def __init__(self, 
                 #players=[], 
                 bblind=10, 
                 sblind=5):
        self.deck=Deck()
        self.deck.shuffle()
        #self.players=players
        self.bblind=bblind
        self.sblind=sblind
        self.stage='pre-flop'
        self.pot=0
        self.maxbet=0
        self.table=[]
        self.round_finished=0
        self.players_active=2
        self.hplayer=Player('brtkl', self)
        self.cplayer=Player('cmp', self)
        self.button='brtkl'
    
    def assigncards(self):
        self.hplayer.hand=self.deck.draw(2)
        self.cplayer.hand=self.deck.draw(2)
        
    def assignblinds(self):
        if self.button==self.hplayer.name:
            tmp1=self.sblind
            tmp2=self.bblind
            self.player_ord=[self.hplayer,self.cplayer]
        else:
            tmp1=self.bblind
            tmp2=self.sblind
            self.player_ord=[self.cplayer,self.hplayer]
        self.hplayer.updatebalance(tmp1)
        self.cplayer.updatebalance(tmp2)
        self.pot=self.sblind+self.bblind
        self.maxbet=self.bblind
    
    def betting(self):
        if self.round_finished==0:
            n=0
            if self.stage != 'pre-flop':
                tmp=sorted(self.player_ord,reverse=True)
            while(min([i.bet for i in self.player_ord]) != self.maxbet or n<1):
                for p in tmp:
                    if self.players_active>1:
                        p.strategy.strat(self.stage)
                n+=1
    
    def nextstage(self,newstage):
        if self.round_finished==0:
            self.stage=newstage
            if newstage=='flop':
                self.table=self.deck.draw(3)
            elif newstage=='turn':
                self.table+=self.deck.draw(1)
            elif newstage=='river':
                self.table+=self.deck.draw(1)
    
    def checkwiner(self):
        resh=eval_hand(self.hplayer.hand,self.table)
        resc=eval_hand(self.cplayer.hand,self.table)
        if resh>resc:
            self.hplayer.updatebalance(self.pot, balanceonly=1)
        elif resh==resc:
            self.hplayer.updatebalance(self.pot/2, balanceonly=1)
            self.cplayer.updatebalance(self.pot/2, balanceonly=1)
        elif resh<resc:
            self.cplayer.updatebalance(self.pot, balanceonly=1)
            
    