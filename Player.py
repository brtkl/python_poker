# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:25:07 2021

@author: brtk
"""

from Strategy import Strategy

class Player():
    """ defining a player with attributes. 
    All attributes need to be defined in a dictionary and passed in defdict, 
    e.g. 
    Player({'name':'c1', 'strat':'sasmonkey'})
    Player({'name':'Me', 'type':'human'})
    Possible atributes;
    -name
    -balance (startig balance)
    -strat (see strategy class for possible values. 
            Note that human is reserved for type=human)
    -type (should be human for iteractive game, otherwise 'comp' (default))
    -cards (defining which cards the player should receive. Used only for
            testing purposes.)
    """
    def __init__(self, defdict):
        """Possible keys for defdict:
            name, balance, type, cards, strat"""
        if isinstance(defdict, str):
            self.name=defdict
        elif isinstance(defdict, dict):
            self.name=defdict['name']
        self.balance=defdict['balance'] if 'balance' in defdict else 1000
        self.type=defdict['type'] if 'type' in defdict else 'comp'
        if self.type not in ['human', 'comp']:
            raise ValueError('type should be human or comp')
        self.cards_req=defdict['cards'] if 'cards' in defdict else []
        if 'strat' in defdict:
            self.strat=defdict['strat']
        else:
            if 'type' in defdict and defdict['type']=='human':    
                self.strat='human'
            else:    
                self.strat='test'
        self.hand=[]
        self.bet=0
        self.probwin=0
        self.probdist=[]
        self.folded=0
        self.allin=0 #20210220: not used at the moment
        self.pot_eligible_tot=0 #total eligible pot amount
        self.pots_idx=[] #indexes of eligible pots. 0 is the main pot
        self.balance_game_init=self.balance
        self.bb100=0
        self.hands_played=0
        self.bb_won=0
        
    def prepare_for_round(self, cur_round):
        self.hand=[]
        self.cur_round=cur_round
        self.strategy=Strategy(self, cur_round, mode=self.strat)
        self.bet=0
        self.probwin=0
        self.probdist=0
        self.folded=0
        self.allin=0 
        self.pot_eligible_tot=0 
        self.pots_idx=[] 
        self.balance_round_init=self.balance #needed for bb100
        self.hands_played+=1 #needed for bb100
        
    def update_bb100(self):
        winamt=self.balance-self.balance_round_init
        winbb=winamt/self.cur_round.bblind
        self.bb_won+=winbb
        self.bb100=self.bb_won/(self.hands_played/100)
        
    def updatebalance(self, bet, balanceonly=0):
        self.balance=round(self.balance+bet,2)
        if balanceonly == 0:
            self.bet+=-bet
        if self.balance==0:
            self.allin=1
        
    def updatetable(self, val, raise_='N', raisval=0):
        if raisval>val:
            raise ValueError('raisval greater than val')
        self.cur_round.pot+=val
        self.cur_round.maxbet=max(self.cur_round.maxbet,self.bet)
        if raise_=='Y':
            self.cur_round.minraise=max(self.cur_round.minraise, raisval)
            
    def check(self):
        allintxt='checks'
        if self.balance==0:
            allintxt='does nothing - already all in'
        self.cur_round.cur_game.print_c(f'##Player {self.name} {allintxt}')
        
    def call(self):
        allintxt=''
        val=self.cur_round.maxbet-self.bet
        if val>=self.balance:
            val=self.balance
            allintxt='(all in)'
        self.updatebalance(-val)
        self.updatetable(val)
        self.cur_round.cur_game.print_c(
            f'##Player {self.name} calls {allintxt}')
    
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
        self.cur_round.cur_game.print_c(
            f'##Player {self.name} raises by {raisval} {allintxt}')
    
    def fold(self):
        self.folded=1
        self.cur_round.players_r_active.remove(self)
        self.cur_round.cur_game.print_c(
            f'##Player {self.name} folds')
        
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
        elif val<self.balance and (val-self.cur_round.maxbet+self.bet
                                   >=self.cur_round.minraise):
            self.raise_(val)
        elif val<self.balance and (val-self.cur_round.maxbet+self.bet
                                   <self.cur_round.minraise):
            if (self.bet<self.cur_round.maxbet and val+self.bet>=
                    self.cur_round.maxbet):
                self.call()
            elif self.bet==self.cur_round.maxbet:
                self.check()
            elif (self.bet<self.cur_round.maxbet and val+self.bet<
                    self.cur_round.maxbet):
                self.fold()
        