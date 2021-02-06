# -*- coding: utf-8 -*-
"""
Created on 20210204

@author: brtk
"""
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from Player import Player
from Round import Round
from Game import Game


class PlayerTestCase(unittest.TestCase):
    """tests for Player class"""
    
    def setUp(self):
        self.p=Player('playername')
        self.g=Game(['test1','test2'])    
        self.r=Round(self.g)
        self.p.prepare_for_round(self.r)
        self.g.players_active[0].prepare_for_round(self.r)
        
    def test_updatebalance(self):
        self.p.updatebalance(-480)
        self.assertTrue(self.p.balance==520 and self.p.bet==480)
        
    def test_updatetable(self):
        self.r.pot=410
        self.r.minraise=100
        self.r.maxbet=300
        self.g.players_active[0].bet=310
        self.g.players_active[0].updatetable(200)
        self.assertTrue(self.r.pot==610 and self.r.minraise==100 and 
                        self.r.maxbet==310)
        
        self.g.players_active[0].bet=510
        self.g.players_active[0].updatetable(200,raise_='Y',raisval=200)
        self.assertTrue(self.r.pot==810 and self.r.minraise==200 and 
                        self.r.maxbet==510)
    
    def test_updatebalance_only(self):
        self.p.updatebalance(-1000, balanceonly=1)
        self.assertTrue(self.p.balance==0 and self.p.bet==0)
    
    def test_prepare_for_round(self): 
        self.p.prepare_for_round(self.r)
        self.assertTrue(self.p.hand==[] and self.p.bet==0 and self.p.probwin==0
                        and self.p.folded==0 and self.p.cur_round is self.r)
    
    def test_call(self):
        self.p.bet=5
        self.p.balance=995
        self.r.maxbet=10
        self.r.pot=15
        self.p.call()
        self.assertTrue(self.p.balance==990 and self.p.bet==10 and 
                        self.r.pot==20 and self.r.maxbet==10)
        self.p.balance=100
        self.p.bet=200
        self.r.maxbet=400
        self.r.pot=600
        self.p.call()
        self.assertTrue(self.p.balance==0 and self.p.bet==300 and 
                        self.r.pot==700 and self.r.maxbet==400)
        
    def test_raise_(self):
        self.p.bet=5
        self.p.balance=995
        self.r.maxbet=10
        self.r.pot=15
        self.p.raise_(50)
        self.assertTrue(self.p.balance==945 and self.p.bet==55 and 
                        self.r.pot==65 and self.r.maxbet==55
                        and self.r.minraise==45)
        self.p.bet=250
        self.p.balance=400
        self.r.maxbet=300
        self.r.minraise=100
        self.r.pot=550
        self.p.raise_(450)
        self.assertTrue(self.p.balance==0 and self.p.bet==650 and 
                        self.r.pot==950 and self.r.maxbet==650
                        and self.r.minraise==350)
        
    def test_fold(self):
        self.g.players_active[0].fold()
        self.assertTrue(self.g.players_active[0].folded==1 and 
                        self.g.players_active[0] not in self.r.players_r_active)
    
if __name__ == '__main__':
    unittest.main()
