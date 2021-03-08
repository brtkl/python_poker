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
        
        
    #add assignblinds tests for when balance<sblind or bblind
        
    def test_nextstage_1(self):
        self.assertRaises(ValueError,self.r.nextstage,'abc')
        
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
        self.assertRaises(ValueError,self.r.nextstage,'river')
        
    
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
        self.g.players_active[0].bet=250
        self.g.players_active[1].bet=250
        
        self.r.pot=500
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1500 and 
                        self.g.players_active[0].bet==250 and
                        self.g.players_active[1].balance==1000)
    
    def test_finalizeround_3(self):
        self.r.table=[(14, 'C'), (3, 'H'), (13, 'C'), (6, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(14, 'H'), (12, 'D')]
        self.g.players_active[1].hand=[(13, 'D'), (13, 'H')]
        self.g.players_active[0].bet=300
        self.g.players_active[1].bet=300
        
        self.r.pot=600
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1000 and 
                        self.g.players_active[1].bet==300 and
                        self.g.players_active[1].balance==1600)
    
    
    def test_finalizeround_4(self):
        self.r.table=[(14, 'C'), (13, 'H'), (13, 'C'), (13, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(5, 'H'), (2, 'D')]
        self.g.players_active[1].hand=[(7, 'D'), (2, 'H')]
        self.g.players_active[0].bet=250
        self.g.players_active[1].bet=250
        
        self.r.pot=500
        self.r.finalizeround()
        self.assertTrue(self.g.players_active[0].balance==1250 and 
                        self.g.players_active[1].balance==1250)
        
    def test_finalizeround_5_allin_3plays_draw(self):
        self.g=Game(['p1','p2','p3'])
        self.r=Round(self.g)
        self.r.table=[(14, 'C'), (13, 'H'), (13, 'C'), (13, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(5, 'H'), (2, 'D')]
        self.g.players_active[1].hand=[(7, 'D'), (2, 'H')]
        self.g.players_active[2].hand=[(8, 'D'), (3, 'H')]
        self.g.players_active[0].bet=500
        self.g.players_active[1].bet=500
        self.g.players_active[2].bet=300
        self.g.players_active[0].balance=500
        self.g.players_active[1].balance=500
        self.g.players_active[2].balance=0
        
        self.r.pot=1300
        self.r.finalizeround()
        self.assertTrue(round(self.g.players_active[0].balance,1)==1000 and 
                        round(self.g.players_active[1].balance,1)==1000 and 
                        round(self.g.players_active[2].balance,1)==300
                        and
                        self.g.players_active[0].balance+
                        self.g.players_active[1].balance+
                        self.g.players_active[2].balance == 2300)
        
        
    def test_finalizeround_6_allin_3plays_win(self):
        self.g=Game(['p1','p2','p3'])
        self.r=Round(self.g)
        self.r.table=[(14, 'C'), (10, 'H'), (13, 'C'), (13, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(5, 'H'), (2, 'D')]
        self.g.players_active[1].hand=[(7, 'D'), (2, 'H')]
        self.g.players_active[2].hand=[(13, 'H'), (3, 'H')]
        self.g.players_active[0].bet=500
        self.g.players_active[1].bet=500
        self.g.players_active[2].bet=300
        self.g.players_active[0].balance=500
        self.g.players_active[1].balance=500
        self.g.players_active[2].balance=0
        
        self.r.pot=1300
        self.r.finalizeround()
        
        self.assertTrue(round(self.g.players_active[0].balance,1)==700 and 
                        round(self.g.players_active[1].balance,1)==700 and 
                        round(self.g.players_active[2].balance,1)==900
                        and
                        self.g.players_active[0].balance+
                        self.g.players_active[1].balance+
                        self.g.players_active[2].balance == 2300)
        
    def test_finalizeround_7_allin_4plays_win(self):
        self.g=Game(['p1','p2','p3','p4'])
        self.r=Round(self.g)
        self.r.table=[(14, 'C'), (10, 'H'), (13, 'C'), (14, 'D'), (13, 'S')]
        self.g.players_active[0].hand=[(5, 'H'), (2, 'D')]
        self.g.players_active[1].hand=[(7, 'D'), (2, 'H')]
        self.g.players_active[2].hand=[(13, 'H'), (3, 'H')]
        self.g.players_active[3].hand=[(14, 'H'), (4, 'H')]
        self.g.players_active[0].bet=600
        self.g.players_active[1].bet=600
        self.g.players_active[2].bet=300
        self.g.players_active[3].bet=500
        self.g.players_active[0].balance=400
        self.g.players_active[1].balance=400
        self.g.players_active[2].balance=0
        self.g.players_active[3].balance=0
        
        self.r.pot=2000
        self.r.finalizeround()
        
        self.assertTrue(round(self.g.players_active[0].balance,1)==500 and 
                        round(self.g.players_active[1].balance,1)==500 and 
                        round(self.g.players_active[2].balance,1)==0 and 
                        round(self.g.players_active[3].balance,1)==1800)
        
    def test_finalizeround_7_allin_8plays_win(self):
        self.g=Game(['p1','p2','p3','p4','p5','p6','p7','p8'])
        self.r=Round(self.g)
        self.r.table=[(14, 'C'), (12, 'H'), (10, 'C'), (8, 'D'), (6, 'S')]
        self.g.players_active[0].hand=[(14, 'H'), (2, 'D')]
        self.g.players_active[1].hand=[(12, 'D'), (2, 'H')]
        self.g.players_active[2].hand=[(12, 'C'), (3, 'H')]
        self.g.players_active[3].hand=[(8, 'H'), (4, 'H')]
        self.g.players_active[4].hand=[(6, 'H'), (2, 'C')]
        self.g.players_active[5].hand=[(13, 'D'), (2, 'S')]
        self.g.players_active[6].hand=[(13, 'H'), (3, 'D')]
        self.g.players_active[7].hand=[(9, 'H'), (4, 'C')]
        self.g.players_active[0].bet=300
        self.g.players_active[1].bet=350
        self.g.players_active[2].bet=400
        self.g.players_active[3].bet=500        
        self.g.players_active[4].bet=580
        self.g.players_active[5].bet=700
        self.g.players_active[6].bet=720
        self.g.players_active[7].bet=720
        self.g.players_active[0].balance=0
        self.g.players_active[1].balance=0
        self.g.players_active[2].balance=0
        self.g.players_active[3].balance=0
        self.g.players_active[4].balance=0
        self.g.players_active[5].balance=0
        self.g.players_active[6].balance=0
        self.g.players_active[7].balance=100
        
        #p1 wins, p2 and p3 draw, p4, p5, p6 and p7 draw, p8 
        
        self.r.pot=4270
        self.r.finalizeround()
        
        self.assertTrue(round(self.g.players_active[0].balance,1)==2400 and 
                        round(self.g.players_active[1].balance,1)==175 and 
                        round(self.g.players_active[2].balance,1)==475 and 
                        round(self.g.players_active[3].balance,1)==500 and 
                        round(self.g.players_active[4].balance,1)==320 and 
                        round(self.g.players_active[5].balance,1)==180 and 
                        round(self.g.players_active[6].balance,1)==220 and 
                        round(self.g.players_active[7].balance,1)==100 )
    
            
if __name__ == '__main__':
    unittest.main()



# print(self.g.players_active[0].balance)
# print(self.g.players_active[1].balance)
# print(self.g.players_active[2].balance)
# print(self.g.players_active[0].balance+
#                 self.g.players_active[1].balance+
#                 self.g.players_active[2].balance)