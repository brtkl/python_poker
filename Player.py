# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:25:07 2021

@author: brtk
"""

from Strategy import Strategy

class Player():
    """ defining a player with attributes"""
    def __init__(self, name, cur_round, balance=1000, strategy='default'):
        self.balance=balance
        self.strategy=Strategy(self,cur_round)
        self.name=name
        self.hand=[]
        self.bet=0
        self.folded=0
        self.cur_round=cur_round
        
    def updatebalance(self, bet, balanceonly=0):
        self.balance+=-bet
        if balanceonly == 0:
            self.bet+=bet
        
    def check(self):
        val=self.cur_round.maxbet-self.bet
        self.updatebalance(val)
        self.cur_round.pot+=val
        self.cur_round.maxbet=max(self.cur_round.maxbet,self.bet)
    
    def raise_(self, val):
        if val<self.cur_round.maxbet:
            print('ERROR: raise by at least the previous bet/raise')
        self.updatebalance(val)
        self.cur_round.pot+=val
        self.cur_round.maxbet=max(self.cur_round.maxbet,self.bet)
    
    def fold(self):
        self.folded=1
        self.cur_round.players_active.remove(self)