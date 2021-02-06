# -*- coding: utf-8 -*-
"""
Created on 20210205

@author: brtk
"""
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from Round import Round
from Game import Game

class RoundTestCase(unittest.TestCase):
    """tests for Round class"""
    
    def setUp(self):
        self.g=Game(['p1','p2'])
        self.r=Round(self.g)
 
    def test_assigncards(self):
        self.r.assigncards()
        tmp=len(self.r.players_r_active)
        self.assertTrue(len(self.r.deck.cards)==52-tmp*2)


    def test_assignblinds_2play_1(self):
        self.r.assignblinds()
        self.assertTrue(self.g.players_active[0].balance==1000-self.r.sblind)
        self.assertTrue(self.r.player_ord_preflop==[self.g.players_active[0]
                                                     ,self.g.players_active[1]])
        self.assertTrue(self.r.player_ord_postflop==[self.g.players_active[1]
                                                     ,self.g.players_active[0]])
        self.assertTrue(self.r.pot==self.r.bblind+self.r.sblind)
        self.assertTrue(self.r.maxbet==self.r.bblind)
        
    def test_assignblinds_2play_2(self):
        self.r.button=1
        self.r.assignblinds()
        self.assertTrue(self.g.players_active[0].balance==1000-self.r.bblind)
        self.assertTrue(self.r.player_ord_preflop==[self.g.players_active[1]
                                                     ,self.g.players_active[0]])
        self.assertTrue(self.r.player_ord_postflop==[self.g.players_active[0]
                                                     ,self.g.players_active[1]])
        
    def test_assignblinds_3play_1(self):
        self.g=Game(['p1','p2','p3'])
        self.r=Round(self.g)
        self.r.assignblinds()
        self.assertTrue(self.g.players_active[0].balance==1000 and
                        self.g.players_active[1].balance==1000-self.r.sblind and
                        self.g.players_active[2].balance==1000-self.r.bblind)
        self.assertTrue(self.r.player_ord_preflop==[self.g.players_active[0]
                                                     ,self.g.players_active[1]
                                                     ,self.g.players_active[2]])
        self.assertTrue(self.r.player_ord_postflop==[self.g.players_active[1]
                                                     ,self.g.players_active[2]
                                                     ,self.g.players_active[0]])
        self.assertTrue(self.r.pot==self.r.bblind+self.r.sblind)
        self.assertTrue(self.r.maxbet==self.r.bblind)
        
    def test_assignblinds_3play_2(self):
        self.g=Game(['p1','p2','p3'])
        self.r=Round(self.g)
        self.r.button=1
        self.r.assignblinds()
        self.assertTrue(self.g.players_active[0].balance==1000-self.r.bblind and
                        self.g.players_active[1].balance==1000 and
                        self.g.players_active[2].balance==1000-self.r.sblind)
        self.assertTrue(self.r.player_ord_preflop==[self.g.players_active[1]
                                                     ,self.g.players_active[2]
                                                     ,self.g.players_active[0]])
        self.assertTrue(self.r.player_ord_postflop==[self.g.players_active[2]
                                                     ,self.g.players_active[0]
                                                     ,self.g.players_active[1]])
        self.assertTrue(self.r.pot==self.r.bblind+self.r.sblind)
        self.assertTrue(self.r.maxbet==self.r.bblind)
        
    def test_assignblinds_3play_3(self):
        self.g=Game(['p1','p2','p3'])
        self.r=Round(self.g)
        self.r.button=2
        self.r.assignblinds()
        self.assertTrue(self.g.players_active[0].balance==1000-self.r.sblind and
                        self.g.players_active[1].balance==1000-self.r.bblind and
                        self.g.players_active[2].balance==1000)
        self.assertTrue(self.r.player_ord_preflop==[self.g.players_active[2]
                                                     ,self.g.players_active[0]
                                                     ,self.g.players_active[1]])
        self.assertTrue(self.r.player_ord_postflop==[self.g.players_active[0]
                                                     ,self.g.players_active[1]
                                                     ,self.g.players_active[2]])
        self.assertTrue(self.r.pot==self.r.bblind+self.r.sblind)
        self.assertTrue(self.r.maxbet==self.r.bblind)
        
    def test_assignblinds_8play_1(self):
        self.g=Game(['p1','p2','p3','p4','p5','p6','p7','p8'])
        self.r=Round(self.g)
        self.r.button=4
        self.r.assignblinds()
        self.assertTrue(self.g.players_active[0].balance==1000 and
                        self.g.players_active[1].balance==1000 and
                        self.g.players_active[2].balance==1000 and
                        self.g.players_active[3].balance==1000 and
                        self.g.players_active[4].balance==1000 and
                        self.g.players_active[5].balance==1000-self.r.sblind and 
                        self.g.players_active[6].balance==1000-self.r.bblind and
                        self.g.players_active[7].balance==1000)
        self.assertTrue(self.r.player_ord_preflop==[self.g.players_active[7]
                                                     ,self.g.players_active[0]
                                                     ,self.g.players_active[1]
                                                     ,self.g.players_active[2]
                                                     ,self.g.players_active[3]
                                                     ,self.g.players_active[4]
                                                     ,self.g.players_active[5]
                                                     ,self.g.players_active[6]])
        self.assertTrue(self.r.player_ord_postflop==[self.g.players_active[5]
                                                     ,self.g.players_active[6]
                                                     ,self.g.players_active[7]
                                                     ,self.g.players_active[0]
                                                     ,self.g.players_active[1]
                                                     ,self.g.players_active[2]
                                                     ,self.g.players_active[3]
                                                     ,self.g.players_active[4]])
        self.assertTrue(self.r.pot==self.r.bblind+self.r.sblind)
        self.assertTrue(self.r.maxbet==self.r.bblind)
        
        
    def test_nextstage_1(self):
        self.assertEqual(self.r.nextstage('abc'), 
                         ['newstage needs to be flop, turn or river'])
        
        self.r.stage='pre-flop'
        self.r.players_r_active=[self.g.players_active[0]]
        self.r.nextstage('flop')
        self.assertEqual(self.r.stage, 'pre-flop')
        
        
    def test_nextstage_2(self):
        self.r.stage='pre-flop'
        self.r.nextstage('flop')
        self.assertEqual(self.r.stage, 'flop')
        self.assertEqual(len(self.r.deck.cards), 52-3)
        self.r.nextstage('turn')
        self.assertEqual(self.r.stage, 'turn')
        self.assertEqual(len(self.r.deck.cards), 52-4)
        self.r.nextstage('river')
        self.assertEqual(self.r.stage, 'river')
        self.assertEqual(len(self.r.deck.cards), 52-5)
        
        self.r.stage='pre-flop'
        self.assertEqual(self.r.nextstage('river'), ['wrong order of stages'])
        
    
    def test_finalizeround_1(self):
        self.r.players_r_active=[self.g.players_active[0]]
        self.r.pot=300
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1300 and 
                        self.g.players_active[0].bet==0)
        
    
    def test_finalizeround_2(self):
        self.r.table=[(14, 'C'), (3, 'H'), (13, 'C'), (6, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(14, 'H'), (13, 'D')]
        self.g.players_active[1].hand=[(2, 'C'), (7, 'S')]
        
        self.r.pot=500
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1500 and 
                        self.g.players_active[0].bet==0 and
                        self.g.players_active[1].balance==1000)
    
    def test_finalizeround_3(self):
        self.r.table=[(14, 'C'), (3, 'H'), (13, 'C'), (6, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(14, 'H'), (12, 'D')]
        self.g.players_active[1].hand=[(13, 'D'), (13, 'H')]
        
        self.r.pot=600
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1000 and 
                        self.g.players_active[1].bet==0 and
                        self.g.players_active[1].balance==1600)
    
    
    def test_finalizeround_4(self):
        self.r.table=[(14, 'C'), (13, 'H'), (13, 'C'), (13, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(5, 'H'), (2, 'D')]
        self.g.players_active[1].hand=[(7, 'D'), (2, 'H')]
        
        self.r.pot=500
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1250 and 
                        self.g.players_active[1].balance==1250)
    
            

    
if __name__ == '__main__':
    unittest.main()
