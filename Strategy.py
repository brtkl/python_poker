# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:26:14 2021

@author: brtk
"""

import sys
import random
import math

class Strategy:  
    """ defining strategy methods that players can use"""
    def __init__(self, player, round_, mode='test'):
        self.player=player
        self.round_=round_
        self.mode=mode
        
    def moveon(self):
        checkmaxbal=max([i.balance for i in self.round_.players_r_active
                              if i is not self.player])
        if self.player.balance==0 or (checkmaxbal==0 and self.player.bet>=
                                      self.round_.maxbet):
            return True
        else:
            return False
        
    def allin(self):
        checkmaxbal=max([i.balance for i in self.round_.players_r_active
                              if i is not self.player])
        """method to be used in strat"""
        if checkmaxbal==0: 
            if self.player.bet < self.round_.maxbet:
                self.player.call() 
                #if all opps made all in it's sufficient to call
            else:
                self.player.check()
        else:
            propos=min(self.player.balance, checkmaxbal+self.round_.maxbet
                       -self.player.bet) 
            #go all-in or force opponnents to go all in
            if self.round_.maxbet>=propos+self.player.bet:
                self.player.call() 
                #call to all in whennot enough money to raise
            else:
                self.player.raise_(propos)
    
    def raise_str(self,raiseby=0):
        """method to be used in strat
        here raisby is the actual raise value
        e.g. if 5 to call and raiseby==10 then 15 is shifted"""
        checkmaxbal=max([i.balance for i in self.round_.players_r_active
                              if i is not self.player])
        if raiseby<self.round_.minraise:
            #raiseby=self.round_.minraise
            raiseby=0 #0 is more conservative
        if checkmaxbal==0: 
            if self.player.bet < self.round_.maxbet:
                self.player.call() 
                #if all opps made all in it's sufficient to call
            else:
                self.player.check()
        else:
            propos=min(checkmaxbal+self.round_.maxbet
                       -self.player.bet, raiseby+self.round_.maxbet
                       -self.player.bet, self.player.balance) 
            if (self.round_.maxbet>=propos+self.player.bet):
                    self.player.call() 
                    #call to all in whennot enough money to raise
            else:
                self.player.raise_(propos)
        
        
    #MAIN STRAT METHOD
    def strat(self, stage):
        
        if self.mode=='test':
            if stage=='pre-flop':
                thrsh=0.4
            else:
                thrsh=0.45
            if self.player.balance==0:
                self.player.check() #already all in
            elif self.player.probwin>0.8:
                self.allin()
            elif self.player.probwin>0.5:
                self.raise_str()
            elif self.player.probwin>=thrsh and self.player.bet<self.round_.maxbet:
                self.player.call()
            elif self.player.bet==self.round_.maxbet:
                self.player.check()
            else:
                self.player.fold()
        
        elif self.mode=='tryharder':
            tmp=self.player.probwin
            numpl=len(self.round_.players_r_active)
            pst=tmp*numpl/2 #standardized prob
            
            if self.moveon():
                self.player.check() 
                
            elif self.player.balance>0:
                if pst>0.8 or self.player.balance<self.round_.minraise:
                    self.allin() #go all in
                elif pst>=0.5 and self.player.bet<=self.round_.maxbet:
                    self.raise_str(raiseby=math.floor(tmp*self.player.balance))
                elif pst>=0.3 and self.player.bet<self.round_.maxbet:
                    self.player.call() 
                else:
                    self.player.fold()
                    
            
        elif self.mode=='tryharder2':
            tmp=self.player.probwin
            numpl=len(self.round_.players_r_active)
            if self.moveon():
                self.player.check() 
            elif self.player.balance>0:
                if tmp>0.8 or self.player.balance<self.round_.minraise:
                    self.allin() #go all in
                elif tmp>=(1/numpl) and self.player.bet<=self.round_.maxbet:
                    self.raise_str(raiseby=math.floor(tmp*self.player.balance))
                elif tmp>=(1/numpl)*0.6 and self.player.bet<self.round_.maxbet:
                    self.player.call() 
                else:
                    self.player.fold()
                
        
        elif self.mode=='potexp':
            tmp=self.player.probwin
            if self.moveon():
                self.player.check() 
            elif self.player.balance>0:
                bet=(tmp*self.round_.pot-self.player.bet)/(1-tmp)
                if tmp>0.95 or self.player.balance<self.round_.minraise:
                    self.allin() #go all in
                else:
                    self.player.makebet(bet)
                    
        elif self.mode=='sasmonkey':
            tmp=random.uniform(0,1)
            if self.player.balance==0:
                self.player.check() #already all in
            elif self.player.balance>0:
                if tmp<0.02 or self.player.balance<self.round_.minraise:
                    self.allin() #go all in
                elif ((tmp<0.43 and (self.player.bet<self.round_.maxbet)) or 
                      (tmp<0.5 and (self.player.bet==self.round_.maxbet))):
                    self.raise_str(raiseby=math.floor(tmp*self.player.balance))
                elif tmp<0.83 and self.player.bet<self.round_.maxbet:
                    self.player.call() 
                elif tmp>=0.5 and self.player.bet==self.round_.maxbet:
                    self.player.check()
                else:
                    self.player.fold()
                    
        elif self.mode=='sassimple':
            tmp=self.player.probwin
            if self.player.balance==0:
                self.player.check() #already all in
            elif self.player.balance>0:
                if tmp>0.9 or self.player.balance<self.round_.minraise:
                    self.allin() #go all in
                elif tmp>=0.5 and self.player.bet<=self.round_.maxbet:
                    self.raise_str(raiseby=math.floor(tmp*self.player.balance))
                elif tmp>=0.3 and self.player.bet<self.round_.maxbet:
                    self.player.call() 
                elif self.player.bet==self.round_.maxbet:
                    self.player.check()
                else:
                    self.player.fold()
                    
        elif self.mode=='usebetmeth1':
            tmp=self.player.probwin
            if self.moveon():
                self.player.check() 
            elif self.player.balance>0:
                self.player.makebet(math.floor((tmp**3)*self.player.balance))
        
        elif self.mode=='usebetmeth2':
            tmp=self.player.probwin
            numpl=len(self.round_.players_r_active)
            pst=tmp*numpl/2 #standardized prob
            if self.moveon():
                self.player.check() 
            elif self.player.balance>0:
                self.player.makebet(math.floor((pst**3)*self.player.balance))
                    
        
        elif self.mode=='human':
            if self.moveon():
                self.player.check() 
                #already all in or all ops all in and our bet is covered
            elif self.player.balance>0:
                cordecide=0
                print(f'##Status:\n\tpot: {self.round_.pot}\n'+
                      f'\tmaxbet: {self.round_.maxbet}\n'+
                      f'\tcurrent bet: {self.player.bet}')
                
                while cordecide==0:
                    if self.player.bet<self.round_.maxbet:
                        text='call/fold/raise/allin'
                    else:
                        text='check/raise/allin'
                    decide=input(f'##Pick one: {text}\n')
                    if decide=='exit':
                        sys.exit(0)
                    elif decide=='probs':
                        print(self.player.probdist)
                    elif decide not in ('call','check','fold','raise','allin'):
                        pass
                    elif (self.player.bet<self.round_.maxbet and decide !='check'
                          ) or (self.player.bet>=self.round_.maxbet and decide 
                                not in ('call', 'fold')):
                        cordecide=1                                
                if decide=='raise':
                    if (self.player.balance<self.round_.minraise+
                        self.round_.maxbet-self.player.bet):
                            self.allin()
                    elif self.player.bet<self.round_.maxbet:
                        print(f'{self.round_.maxbet-self.player.bet} to call')
                    corraise=0
                    while corraise==0:
                        raiseval=input('##Enter amount to raise\n'+
                                       'minimum to raise: '+
                                       f'{self.round_.minraise}\n')
                        if raiseval=='exit':
                            sys.exit(0)
                        elif decide=='probs':
                            print(self.player.probdist)
                        else:
                            try:
                                int(raiseval)
                            except ValueError:
                                pass
                            else:
                                if int(raiseval)>=self.round_.minraise:
                                    corraise=1
                                    self.raise_str(raiseby=int(raiseval))
                                else:
                                    print(f'at least {self.round_.minraise}'
                                          ,'required')
                elif decide=='allin':
                    self.allin() #go all in
                elif decide=='call':
                    self.player.call()
                elif decide=='check':
                    self.player.check()
                elif decide=='fold':
                    self.player.fold()
                else:
                    print('incorrect choice')
                    
        else:
            raise ValueError('incorrect strategy defined for a player')

