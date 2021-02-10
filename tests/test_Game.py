# -*- coding: utf-8 -*-
"""
Created on 20210209

@author: brtk
"""
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from Game import Game
from Round import Round
from Strategy import Strategy


class GameTestCase(unittest.TestCase):
    """tests for Strategy class"""
    
    def setUp(self):
        self.g=Game(['p1','p2','p3'], maxrounds=1)
        self.r=Round(self.g)
        
    
    def test_3p_game_noten_bb(self):
        self.r.players_r_active[0].balance=20
        self.r.players_r_active[1].balance=20
        self.r.players_r_active[2].balance=7 ##bblind pos
        self.r.players_r_active[0].bet=0
        self.r.players_r_active[1].bet=0
        self.r.players_r_active[2].bet=0
        self.r.players_r_active[0].folded=0
        self.r.players_r_active[1].folded=0
        self.r.players_r_active[2].folded=0
        self.r.players_r_active[0].cur_round=self.r
        self.r.players_r_active[1].cur_round=self.r
        self.r.players_r_active[2].cur_round=self.r
        self.r.players_r_active[0].strategy=Strategy(self.r.players_r_active[0], self.r)
        self.r.players_r_active[1].strategy=Strategy(self.r.players_r_active[1], self.r)
        self.r.players_r_active[2].strategy=Strategy(self.r.players_r_active[2], self.r)
        self.r.players_r_active[0].hand=self.r.deck.draw(cards=[(2,'C'),(7,'H')])
        self.r.players_r_active[1].hand=self.r.deck.draw(cards=[(2,'S'),(6,'D')])
        self.r.players_r_active[2].hand=self.r.deck.draw(cards=[(14,'C'),(14,'H')])
        
        self.g.play(test=1,r=self.r)
        
        self.assertTrue(self.g.players_active[0].balance==20 and
                        self.g.players_active[1].balance==15 and
                        self.g.players_active[2].balance==12)
 
    def test_3p_game_noten_sb(self):
        self.r.players_r_active[0].balance=20
        self.r.players_r_active[1].balance=20
        self.r.players_r_active[2].balance=4 ##bblind pos
        self.r.players_r_active[0].bet=0
        self.r.players_r_active[1].bet=0
        self.r.players_r_active[2].bet=0
        self.r.players_r_active[0].folded=0
        self.r.players_r_active[1].folded=0
        self.r.players_r_active[2].folded=0
        self.r.players_r_active[0].cur_round=self.r
        self.r.players_r_active[1].cur_round=self.r
        self.r.players_r_active[2].cur_round=self.r
        self.r.players_r_active[0].strategy=Strategy(self.r.players_r_active[0], self.r)
        self.r.players_r_active[1].strategy=Strategy(self.r.players_r_active[1], self.r)
        self.r.players_r_active[2].strategy=Strategy(self.r.players_r_active[2], self.r)
        self.r.players_r_active[0].hand=self.r.deck.draw(cards=[(2,'C'),(7,'H')])
        self.r.players_r_active[1].hand=self.r.deck.draw(cards=[(2,'S'),(6,'D')])
        self.r.players_r_active[2].hand=self.r.deck.draw(cards=[(14,'C'),(14,'H')])
        
        self.g.play(test=1,r=self.r)
        
        self.assertTrue(self.g.players_active[0].balance==15 and
                        self.g.players_active[1].balance==25 )
    
    
if __name__ == '__main__':
    unittest.main()
