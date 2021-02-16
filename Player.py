# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:25:07 2021

@author: brtk
"""

from Strategy import Strategy

class Player():
    """ defining a player with attributes"""
    def __init__(self, name, balance=1000, stratmode='test'):
        self.balance=balance
        self.name=name
        self.stratmode=stratmode
        self.hand=[]
        self.bet=0
        self.probwin=0
        self.folded=0
        self.allin=0
        self.pot_eligible_tot=0
        self.pots_idx=[]
        self.cards_req=[]
        
    def prepare_for_round(self, cur_round):
        self.hand=[]
        self.cur_round=cur_round
        self.strategy=Strategy(self, cur_round, mode=self.stratmode)
        self.bet=0
        self.probwin=0
        self.folded=0
        
    def updatebalance(self, bet, balanceonly=0):
        self.balance=round(self.balance+bet,2)
        if balanceonly == 0:
            self.bet+=-bet
        if self.balance==0:
            self.allin=1
        
    def updatetable(self, val, raise_='N', raisval=0):
        if raisval>val:
            return('ERROR: raisval greater than val')
        self.cur_round.pot+=val
        self.cur_round.maxbet=max(self.cur_round.maxbet,self.bet)
        if raise_=='Y':
            self.cur_round.minraise=max(self.cur_round.minraise, raisval)
            
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
        self.updatetable(val)
        print(f'Player {self.name} calls {allintxt}')
    
    def raise_(self, val):
        """ Note, when using raise_, val param denotes all the money the player
        needs to shift from his stack to the table, which means that if 
        player.bet<round.maxbet then some of the val value will be used for 
        calling and the remaining for actual raising
        """
        allintxt=''
        if val>=self.balance:
            val=self.balance
            allintxt='(all in)'
        if self.bet<self.cur_round.maxbet:
            raisval=val-(self.cur_round.maxbet-self.bet)
        else:
            raisval=val
        self.updatebalance(-val)
        self.updatetable(val, raise_='Y', raisval=raisval)
        print(f'Player {self.name} raises by {raisval} {allintxt}')
    
    def fold(self):
        self.folded=1
        self.cur_round.players_r_active.remove(self)
        print(f'Player {self.name} folds')
        
    def makebet(self, val):
        """collating check, call, raise_ and fold methods depending 
        on bet value. Might be used to simplify strategy."""
        if val==0 and self.bet<self.cur_round.maxbet:
            self.fold()
        elif val==0 and self.bet>=self.cur_round.maxbet:
            self.check()
        elif val>=self.balance and self.cur_round.maxbet>self.balance+self.bet:
            self.call() #all in call
        elif val>=self.balance and self.cur_round.maxbet<=self.balance+self.bet:
            self.raise_(self.balance) #all in raise
        elif val<self.balance and val>=self.cur_round.minraise:
            self.raise_(val)
        elif val<self.balance and val<self.cur_round.minraise:
            if (self.bet<self.cur_round.maxbet and val+self.balance>=
                    self.cur_round.maxbet):
                self.call()
            elif self.bet==self.cur_round.maxbet:
                self.check()
            elif (self.bet<self.cur_round.maxbet and val+self.balance<
                    self.cur_round.maxbet):
                self.fold()
        