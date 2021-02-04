# -*- coding: utf-8 -*-
"""
Created on 2021-02-04

@author: brtk
"""
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from calc_probwin import calc_probwin


class CalcProbwinTestCase(unittest.TestCase):
    """tests for eval_hand function"""
    
    def setUp(self):
        self.test_lesscards=[(5,'H'), (4,'H'), (3,'H'), (2,'H'), (14,'H'), 
                             (5,'H')]
        self.testrep=[(5,'H'), (4,'H'), (3,'H'), (2,'H'), (14,'H'), 
                             (5,'H'), (6,'C')]
        self.testhand_strflush=[(13,'H'), (12,'H'), (11,'H'), (10,'H'), (14,'H'), 
                             (5,'C'), (6,'C')]
        self.testhand_4ofakind=[(10,'H'), (10,'C'), (3,'H'), (10,'S'), (9,'H'), 
                             (5,'C'), (10,'D')]
        self.testhand_fullhouse=[(5,'H'), (5,'C'), (6,'H'), (2,'H'), (14,'H'), 
                             (5,'S'), (6,'C')]
        self.testhand_flush=[(14,'H'), (13,'H'), (3,'H'), (9,'H'), (2,'H'), 
                             (5,'C'), (14,'C')]
        self.testhand_straight=[(5,'H'), (4,'S'), (3,'C'), (2,'H'), (14,'D'), 
                             (12,'C'), (10,'S')]
        self.testhand_3ofakind=[(10,'H'), (10,'C'), (3,'H'), (10,'S'), (9,'H'), 
                             (5,'C'), (11,'D')]
        self.testhand_2pairs=[(12,'H'), (12,'C'), (3,'H'), (11,'S'), (14,'H'), 
                             (5,'C'), (11,'D')]
        self.testhand_1pair=[(2,'H'), (6,'C'), (3,'H'), (11,'S'), (14,'H'), 
                             (13,'C'), (11,'D')]
        self.testhand_highcard=[(13,'H'), (12,'C'), (3,'H'), (11,'S'), (2,'H'), 
                             (5,'C'), (8,'D')]
        self.testhand_2high=[(14,'H'), (14,'C')]
        self.testhand_2low=[(8,'H'), (2,'C')]
        self.testhand_3any=[(8,'H'), (2,'C'), (11,'D')]
        self.testhand_4any=[(8,'H'), (5,'C'), (11,'D'), (14,'D')]
        self.testhand_5any=[(8,'H'), (5,'C'), (11,'D'), (14,'D'), (2,'S')]
        self.testhand_6any=[(8,'H'), (5,'C'), (11,'D'), (14,'D'), (2,'S'), (3,'S')]
        
    
    def test_lessthan7(self):
        self.assertEqual(calc_probwin(self.test_lesscards,[]),
           ['2 cards in hand and between 0 and 5 cards in a table are'
            +' needed in lists'])  
        
    def test_repeating_cards(self):
        self.assertEqual(calc_probwin(self.testrep[:2],self.testrep[2:]),
                        ['repeating cards in the input data'])
    
    def test_cant_lose(self):
        self.assertTrue(calc_probwin(self.testhand_strflush[:2],
                                      self.testhand_strflush[2:])[0]==1)
    def test_cant_lose2(self):
        self.assertTrue(calc_probwin(self.testhand_4ofakind[:2],
                                     self.testhand_4ofakind[2:])[0]==1)
        
    def test_cant_lose2_sim(self):
        self.assertTrue(calc_probwin(self.testhand_4ofakind[:2],
                                     self.testhand_4ofakind[2:],type='simul')[0]==1)
        
    def test_high_prob(self):
        self.assertTrue(calc_probwin(self.testhand_fullhouse[:2],
                                     self.testhand_fullhouse[2:])[0]>0.9)
        
    def test_low_prob(self):
        self.assertTrue(calc_probwin(self.testhand_highcard[:2],
                                     self.testhand_highcard[2:])[0]
                        <calc_probwin(self.testhand_highcard[:2],
                                     self.testhand_highcard[2:])[2])
    def test_low_prob2(self):
        self.assertTrue(calc_probwin(self.testhand_1pair[:2],
                                     self.testhand_1pair[2:])[0]<0.1)
                    
    def test_dif_def_exact(self):
        self.assertTrue(abs(calc_probwin(self.testhand_straight[:2],
                                     self.testhand_straight[2:],type='exact')[0]
                        -calc_probwin(self.testhand_straight[:2],
                                     self.testhand_straight[2:])[0])==0)
                    
    def test_dif_sim_exact(self):
        self.assertTrue(abs(calc_probwin(self.testhand_straight[:2],
                                     self.testhand_straight[2:],type='simul')[0]
                        -calc_probwin(self.testhand_straight[:2],
                                     self.testhand_straight[2:])[0])<0.01)
                    
    def test_dif_sim_exact2(self):
        self.assertTrue(abs(calc_probwin(self.testhand_3ofakind[:2],
                                     self.testhand_3ofakind[2:],type='simul')[0]
                        -calc_probwin(self.testhand_3ofakind[:2],
                                     self.testhand_3ofakind[2:])[0])<0.01)
        
    def test_2card_sim_high(self):
        self.assertTrue(calc_probwin(self.testhand_2high,[],type='simul')[0]
                        >0.8)
        
    def test_2card_sim_low(self):
        self.assertTrue(calc_probwin(self.testhand_2low,[],type='simul')[0]
                        <0.35)
        
    def test_3any(self):
        self.assertTrue(1>calc_probwin(self.testhand_3any[:2],
                                     self.testhand_3any[2:],type='simul')[0]>0)
        
    def test_4any(self):
        self.assertTrue(1>calc_probwin(self.testhand_4any[:2],
                                     self.testhand_4any[2:],type='simul')[0]>0)
        
    def test_5any(self):
        self.assertTrue(1>calc_probwin(self.testhand_5any[:2],
                                     self.testhand_5any[2:],type='simul')[0]>0)
        
    def test_6any(self):
        self.assertTrue(1>calc_probwin(self.testhand_6any[:2],
                                     self.testhand_6any[2:],type='simul')[0]>0)
        
    def test_sumprob(self):
        a=calc_probwin(self.testhand_5any[:2], self.testhand_5any[2:])
        self.assertAlmostEqual(a[0]+a[1]+a[2],1,places=3)



if __name__ == '__main__':
    unittest.main()
