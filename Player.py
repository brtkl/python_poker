# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:25:07 2021

@author: brtk
"""

from Strategy import Strategy

class Player():
    """ defining a player with attributes"""
    def __init__(self, name, balance=1000, strategy='default'):
        self.balance=balance
        self.name=name
        self.hand=[]
        self.bet=0
        self.probwin=0
        self.folded=0
        
    def prepare_for_round(self, cur_round):
        self.hand=[]
        self.cur_round=cur_round
        self.strategy=Strategy(self,cur_round)
        self.bet=0
        self.probwin=0
        self.folded=0
        
    def updatebalance(self, bet, balanceonly=0):
        self.balance+=bet
        if balanceonly == 0:
            self.bet+=-bet
        
    def check(self):
        allintxt='checks'
        if self.balance==0:
            allintxt='does nothing - already all in'
        print(f'Player {self.name} {allintxt}')
        
    def call(self):
        allintxt=''
        val=self.cur_round.maxbet-self.bet
        if val>=self.balance:
            val=self.balance
            allintxt='(all in)'
        self.updatebalance(-val)
        self.cur_round.pot+=val
        self.cur_round.maxbet=max(self.cur_round.maxbet,self.bet)
        print(f'Player {self.name} calls {allintxt}')
    
    def raise_(self, val):
        allintxt=''
        if val>=self.balance:
            val=self.balance
            allintxt='(all in)'
        if self.bet<self.cur_round.maxbet:
            raisval=val-(self.cur_round.maxbet-self.bet)
        else:
            raisval=val
        self.cur_round.minraise=max(self.cur_round.minraise, val-self.bet)
        self.updatebalance(-val)
        self.cur_round.pot+=val
        self.cur_round.maxbet=max(self.cur_round.maxbet, self.bet)
        print(f'Player {self.name} raises by {raisval} {allintxt}')
    
    def fold(self):
        self.folded=1
        self.cur_round.players_r_active.remove(self)
        print(f'Player {self.name} folds')