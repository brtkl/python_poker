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
        self.button='brtkl'
        self.minraise=bblind
    
    def assigncards(self):
        for p in self.players_r_active:
            p.hand=self.deck.draw(2)
            print(f"{p.name} hand: {p.hand}")
        
    def assignblinds(self):
        if self.button==self.players_r_active[0].name:
            tmp1=self.sblind
            tmp2=self.bblind
            self.player_ord=[self.players_r_active[0],self.players_r_active[1]]
        else:
            tmp1=self.bblind
            tmp2=self.sblind
            self.player_ord=[self.players_r_active[1],self.players_r_active[0]]
        self.players_r_active[0].updatebalance(-tmp1)
        self.players_r_active[1].updatebalance(-tmp2)
        self.pot=self.sblind+self.bblind
        self.maxbet=self.bblind
    
    def betting(self):
        if len(self.players_r_active)>1:
            n=0
            tmp=self.player_ord[:]
            for p in tmp:
                    p.probwin=round(calc_probwin(p.hand, self.table)[0],2)
            if self.stage != 'pre-flop':
                tmp.reverse()
            while((min([i.bet for i in self.players_r_active]) != self.maxbet) or n<1):
                for p in tmp:
                    if len(self.players_r_active)>1 and (p.bet<self.maxbet or n<1):
                        p.strategy.strat(self.stage)
                n+=1
    
    def nextstage(self,newstage):
        if len(self.players_r_active)>1:
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
        resh=eval_hand(self.players_r_active[0].hand+self.table)
        resc=eval_hand(self.players_r_active[1].hand+self.table)
        if (resh>resc and self.players_r_active[0].folded==0
            ) or self.players_r_active[1].folded==1:
            self.players_r_active[0].updatebalance(self.pot, balanceonly=1)
            if self.players_r_active[1].folded==1:
                print(f"{self.players_r_active[0].name} wins, opponent folded")
            else:
                print(f"{self.players_r_active[0].name} wins having {resh}")
                
        
        elif (resh<resc and self.players_r_active[1].folded==0
              ) or self.players_r_active[0].folded==1:
            self.players_r_active[1].updatebalance(self.pot, balanceonly=1)
            if self.players_r_active[0].folded==1:
                print(f"{self.players_r_active[1].name} wins, opponent folded")
            else:
                print(f"{self.players_r_active[1].name} wins having {resc}")
            
        elif resh==resc:
            self.players_r_active[0].updatebalance(self.pot/2, balanceonly=1)
            self.players_r_active[1].updatebalance(self.pot/2, balanceonly=1)
            print(f"{self.players_r_active[0].name} and "
                  +f"{self.players_r_active[1].name} win, both"
                  +f"having {resc}")
            
    