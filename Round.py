# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:43:21 2021

@author: brtk
"""

from Player import Player
from Deck import Deck
from eval_hand import eval_hand
from calc_probwin import calc_probwin

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
        self.hplayer=Player('brtkl', self)
        self.cplayer=Player('cmp', self)
        self.players_active=[self.hplayer, self.cplayer]
        self.button='brtkl'
        self.minraise=bblind
    
    def assigncards(self):
        self.hplayer.hand=self.deck.draw(2)
        self.cplayer.hand=self.deck.draw(2)
        print(f"{self.hplayer.name} hand: {self.hplayer.hand} \n")
        print(f"{self.cplayer.name} hand: {self.cplayer.hand} \n")
        
    def assignblinds(self):
        if self.button==self.hplayer.name:
            tmp1=self.sblind
            tmp2=self.bblind
            self.player_ord=[self.hplayer,self.cplayer]
        else:
            tmp1=self.bblind
            tmp2=self.sblind
            self.player_ord=[self.cplayer,self.hplayer]
        self.hplayer.updatebalance(-tmp1)
        self.cplayer.updatebalance(-tmp2)
        self.pot=self.sblind+self.bblind
        self.maxbet=self.bblind
    
    def betting(self):
        if len(self.players_active)>1:
            n=0
            tmp=self.player_ord[:]
            for p in tmp:
                    p.probwin=round(calc_probwin(p.hand, self.table)[0],2)
            if self.stage != 'pre-flop':
                tmp.reverse()
            while((min([i.bet for i in self.players_active]) != self.maxbet) or n<1):
                for p in tmp:
                    if len(self.players_active)>1 and (p.bet<self.maxbet or n<1):
                        p.strategy.strat(self.stage)
                n+=1
    
    def nextstage(self,newstage):
        if len(self.players_active)>1:
            self.stage=newstage
            if newstage=='flop':
                self.table=self.deck.draw(3)
            elif newstage=='turn':
                self.table+=self.deck.draw(1)
            elif newstage=='river':
                self.table+=self.deck.draw(1)
            print(f"{newstage}: {self.table} \n")
        else:
            print("All but 1 players folded \n")
            
    
    def finalizeround(self):
        resh=eval_hand(self.hplayer.hand+self.table)
        resc=eval_hand(self.cplayer.hand+self.table)
        if (resh>resc and self.hplayer.folded==0) or self.cplayer.folded==1:
            self.hplayer.updatebalance(self.pot, balanceonly=1)
            if self.cplayer.folded==1:
                print(f"{self.hplayer.name} wins, opponent folded")
            else:
                print(f"{self.hplayer.name} wins having {resh}")
                
        
        elif (resh<resc and self.cplayer.folded==0) or self.hplayer.folded==1:
            self.cplayer.updatebalance(self.pot, balanceonly=1)
            if self.hplayer.folded==1:
                print(f"{self.cplayer.name} wins, opponent folded")
            else:
                print(f"{self.cplayer.name} wins having {resc}")
            
        elif resh==resc:
            self.hplayer.updatebalance(self.pot/2, balanceonly=1)
            self.cplayer.updatebalance(self.pot/2, balanceonly=1)
            print(f"{self.hplayer.name} and {self.cplayer.name} win, both"
                  +f"having {resc}")
            
    