# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:43:21 2021

@author: brtk
"""

from Deck import Deck
from eval_hand import eval_hand
from calc_probwin import calc_probwin
import math
import random

class Round():
    """ round of a game. Game consists of rounds, round consist of stages
    (pre-flop, flop, turn, river) """
    def __init__(self, 
                 cur_game, 
                 bblind=10, 
                 sblind=5
                 ):
        self.deck=Deck()
        self.deck.shuffle()
        self.bblind=bblind
        self.sblind=sblind
        self.stage='pre-flop'
        self.pot=0
        self.maxbet=0
        self.table=[]
        self.players_r_active=cur_game.players_active[:]
        self.players_r_started=cur_game.players_active[:]
        self.button=cur_game.button_idx
        self.minraise=bblind
        self.simnum_prob=cur_game.simnum_prob
        self.cur_game=cur_game
    
    def assigncards(self):
        for p in self.players_r_active:
            if not p.cards_req:
                p.hand=self.deck.draw(2)
            elif p.cards_req:
                p.hand=self.deck.draw(cards=p.cards_req)
            if self.cur_game.mode=='sim' or (self.cur_game.mode=='interactive' 
                                             and p.type=='human'):
                self.cur_game.print_c(f"########{p.name} hand: {p.hand}")
        
    def showroundstatus(self):
        lenact=len(self.players_r_started)
        if lenact==2:
            tmp=0
        else:
            tmp=1
        for p in self.cur_game.players_init:
            status=f'\t{p.name}: '+' '*(15-len(p.name))
            if p not in self.cur_game.players_active:
                status+='inactive'
            else:
                status+=f'bet: {p.bet} '
                if (self.cur_game.players_active.index(p)==(self.button) 
                    % lenact):
                        status+='\t\tbtn'
                if (self.cur_game.players_active.index(p)==(self.button+tmp) 
                    % lenact):
                        status+='\t\tsb'
                elif (self.cur_game.players_active.index(p)==
                      (self.button+tmp+1) % lenact):
                        status+='\t\tbb'
                else:
                    status+='\t\t'
                if p not in self.players_r_active:
                    status+='\t\tfolded'
                if p.balance<=0:
                    status+='\t\tallin'
            self.cur_game.print_c(f'{status}')
        
    def assignblinds(self):
        lenact=len(self.players_r_active)
        if lenact==2:
            tmp=0
        else:
            tmp=1
        sblind=self.sblind
        bblind=self.bblind
        if self.players_r_active[(self.button+tmp) % lenact].balance<sblind:
            sblind=self.players_r_active[(self.button+tmp) % lenact].balance
        if self.players_r_active[(self.button+1+tmp) % lenact].balance<bblind:
            bblind=self.players_r_active[(self.button+1+tmp) % lenact].balance
        self.players_r_active[(self.button+tmp) % lenact].updatebalance(-sblind)
        self.players_r_active[(self.button+1+tmp) % lenact].updatebalance(-bblind)
        self.player_ord_preflop=self.players_r_active[
            (self.button+2+tmp) % lenact:]+self.players_r_active[:(self.button+
                                                               2+tmp) % lenact]
        self.player_ord_postflop=self.players_r_active[
            (self.button+1) % lenact:]+self.players_r_active[:(self.button
                                                               +1) % lenact]
        self.pot=sblind+bblind
        self.maxbet=self.bblind  #self.bblind on purpose - dont remove self 
        
        if self.cur_game.mode=='sim':
            self.cur_game.print_c(
                f'sb: {self.players_r_active[(self.button+tmp) % lenact].name}\n'
              +f'bb: {self.players_r_active[(self.button+tmp+1) % lenact].name}')
        elif self.cur_game.mode=='interactive':
            self.showroundstatus()
                
    
    def betting(self):
        if len(self.players_r_active)>1:
            n=0
            for p in self.players_r_active:
                p.probdist=calc_probwin(p.hand, self.table
                                        , n=len(self.players_r_active)
                                        , simnum=self.simnum_prob)
                p.probwin=round(p.probdist[0],2)
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
            raise ValueError('newstage needs to be flop, turn or river')
        
        if len(self.players_r_active)>1:
            if ((self.stage=='pre-flop' and newstage != 'flop') or 
                (self.stage=='flop' and newstage != 'turn') or
                (self.stage=='turn' and newstage != 'river')):
                    raise ValueError('wrong order of stages')
            self.stage=newstage
            if self.cur_game.mode=='interactive':
                self.showroundstatus()
            if newstage=='flop':
                self.table=self.deck.draw(3, cards=self.cur_game.flop_req)
            elif newstage=='turn':
                self.table+=self.deck.draw(1, cards=self.cur_game.turn_req)
            elif newstage=='river':
                self.table+=self.deck.draw(1, cards=self.cur_game.river_req)
            self.cur_game.print_c(f"{newstage}: {self.table}")
            
    
    def finalizeround(self):
        if len(self.players_r_active)==1:
            self.cur_game.print_c(
                f"{self.players_r_active[0].name} wins, opponents folded")
            self.players_r_active[0].updatebalance(self.pot, balanceonly=1)
            
        else:
            #determine the main pot and side pots
            for p in self.players_r_active:
                p.pot_eligible_tot=sum([min(p.bet, j.bet) for j in 
                                    self.players_r_started])
            distnct_elig=sorted(list(set([i.pot_eligible_tot for i in 
                                          self.players_r_active])))
            pots_all=[x-y for x,y in zip(distnct_elig, [0]+distnct_elig)]
            
            if sum(pots_all) != self.pot:
                raise ValueError('check pots_all calculation')
            
            for p in self.players_r_active:
                for i in range(len(distnct_elig)):
                    if p.pot_eligible_tot >= distnct_elig[i]:
                        p.pots_idx.append(i)
            
            for i in range(len(pots_all)):
                elig_players=[]
                for p in self.players_r_active:
                    if i in p.pots_idx:
                        elig_players.append(p)
                maxhand=max([eval_hand(p.hand+self.table) for p in elig_players])
                winplay=[p for p in elig_players if eval_hand(p.hand+self.table
                                                              )==maxhand]
                if len(winplay)==1:
                    winplay[0].updatebalance(pots_all[i], balanceonly=1)
                    self.cur_game.print_c(
                        f"{winplay[0].name} wins pot {i}, {pots_all[i]} having {maxhand}")
                elif len(winplay)>1:
                    if round(pots_all[i]/len(winplay),2)*len(winplay)==pots_all[i]:
                        valperp=round(pots_all[i]/len(winplay),2)
                        rest=0
                    else:    
                        valperp=round(math.floor((pots_all[i]/len(winplay))
                                                 *100)/100,2)
                        rest=pots_all[i]-valperp*len(winplay)
                        idxrest=random.choice(list(range(len(winplay))))
                        #if not possible to divide penny then give randomly
                    for p in winplay:
                        p.updatebalance(valperp, balanceonly=1)
                        if rest != 0 and winplay.index(p)==idxrest:
                            p.updatebalance(rest, balanceonly=1)
                        self.cur_game.print_c(
                            f"{p.name} drew pot {i}, {valperp} having {maxhand}")
                    
            
        
        
        
        
        