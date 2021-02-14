# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:26:14 2021

@author: brtk
"""

import random
import math

class Strategy:  
    """ defining strategy methods that players can use"""
    def __init__(self, player, round_, mode='test'):
        self.player=player
        self.round_=round_
        self.mode=mode
        
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
        """method to be used in strat"""
        checkmaxbal=max([i.balance for i in self.round_.players_r_active
                              if i is not self.player])
        if raiseby<self.round_.minraise:
            raiseby=self.round_.minraise
        if checkmaxbal==0: 
            if self.player.bet < self.round_.maxbet:
                self.player.call() 
                #if all opps made all in it's sufficient to call
            else:
                self.player.check()
        else:
            propos=min(checkmaxbal+self.round_.maxbet
                       -self.player.bet, raiseby+self.round_.maxbet
                       -self.player.bet) 
            if (self.round_.maxbet>=propos+self.player.bet or 
                propos>=self.player.balance):
                    self.player.call() 
                    #call to all in whennot enough money to raise
            else:
                self.player.raise_(propos)
        
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
                    


# %macro opstrat(round=,myvar=_op,opvar=_my);
# %if &round. ne 0 %then %do;
# 	if bettotal&myvar.<=bettotal&opvar. and cap&myvar.>0 then do;
# 	  temp=rand('Uniform');
# 	  /*all in   */
# 	  if temp<0.02 or cap&myvar.<&blind_b. then do;
# 		  bet&myvar.=min(cap&myvar.+bettotal&myvar.,cap&opvar.+bettotal&opvar.)-bettotal&myvar.;
#       bettotal&myvar.=min(cap&myvar.+bettotal&myvar.,cap&opvar.+bettotal&opvar.);
# 		end;
# 		/*raise by x*/
# 		else if (temp<0.43 and bettotal&myvar.<bettotal&opvar.) or (temp<0.5 and bettotal&myvar.=bettotal&opvar.) then do;
# 		  temp2=rand('ERLANG',3);
# 		  bet&myvar.=max(bettotal&opvar.,bettotal&myvar.)+min(ceil(temp2),cap&myvar.,cap&opvar.)-bettotal&myvar.; /*don't raise more than my has*/
#       bettotal&myvar.=max(bettotal&opvar.,bettotal&myvar.)+min(ceil(temp2),cap&myvar.,cap&opvar.);
# 		end;
# 		/*call or check*/
# 		else if (temp<0.83 and bettotal&myvar.<bettotal&opvar.) or (temp>=0.5 and bettotal&myvar.=bettotal&opvar.) then do;
#       bet&myvar.=bettotal&opvar.-bettotal&myvar.;
# 			bettotal&myvar.=bettotal&opvar.;
# 		end;
# 		/* fold*/
# 		else do;
# 		  finish_fl='Y';
# 	  end;
# 	  cap&myvar.=cap&myvar.-bet&myvar.;
# 	end;
# %end;
# %mend;

# %macro mystrat(round=,myvar=_my,opvar=_op);
# %if &round. ne 0 %then %do;
# 	if bettotal&myvar.<=bettotal&opvar. and cap&myvar.>0 then do;
# 	  /*all in   */
# 	  if prob_win>90 or cap&myvar.<&blind_b. then do;
# 		  bet&myvar.=min(cap&myvar.+bettotal&myvar.,cap&opvar.+bettotal&opvar.)-bettotal&myvar.;
#       bettotal&myvar.=min(cap&myvar.+bettotal&myvar.,cap&opvar.+bettotal&opvar.);
# 		end;
# 		/*raise by x*/
# 		else if (prob_win>50 and bettotal&myvar.<=bettotal&opvar.) then do;
# 		  temp2=rand('ERLANG',5);
# 		  bet&myvar.=max(bettotal&opvar.,bettotal&myvar.)+min(ceil(temp2),cap&myvar.,cap&opvar.)-bettotal&myvar.; /*don't raise more than my has*/
#       bettotal&myvar.=max(bettotal&opvar.,bettotal&myvar.)+min(ceil(temp2),cap&myvar.,cap&opvar.);
# 		end;
# 		/*call or check*/
# 		else if (prob_win>30 and bettotal&myvar.<bettotal&opvar.) or (bettotal&myvar.=bettotal&opvar.) then do;
#       bet&myvar.=bettotal&opvar.-bettotal&myvar.;
# 			bettotal&myvar.=bettotal&opvar.;
# 		end;
# 		/* fold*/
# 		else do;
# 		  finish_fl='Y';
# 	  end;
# 	  cap&myvar.=cap&myvar.-bet&myvar.;
# 	end;
# %end;
# %mend;


