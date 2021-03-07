# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:26:41 2021

@author: brtk
"""
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import unittest
from eval_hand import eval_hand


class EvalHandTestCase(unittest.TestCase):
    """tests for eval_hand function"""
    
    def setUp(self):
        self.test_lesscards=[(5,'H'), (4,'H'), (3,'H'), (2,'H'), (14,'H'), 
                             (5,'H')]
        self.testrep=[(5,'H'), (4,'H'), (3,'H'), (2,'H'), (14,'H'), 
                             (5,'H'), (6,'C')]
        self.testhand_strflush=[(5,'H'), (4,'H'), (3,'H'), (2,'H'), (14,'H'), 
                             (5,'C'), (6,'C')]
        self.testhand_4ofakind=[(10,'H'), (10,'C'), (3,'H'), (10,'S'), (9,'H'), 
                             (5,'C'), (10,'D')]
        self.testhand_fullhouse=[(5,'H'), (5,'C'), (6,'H'), (2,'H'), (14,'H'), 
                             (5,'S'), (6,'C')]
        self.testhand_flush=[(5,'H'), (7,'H'), (3,'H'), (9,'H'), (14,'H'), 
                             (5,'C'), (14,'C')]
        self.testhand_straight=[(5,'H'), (4,'H'), (3,'C'), (2,'H'), (14,'H'), 
                             (5,'C'), (14,'C')]
        self.testhand_3ofakind=[(10,'H'), (10,'C'), (3,'H'), (10,'S'), (9,'H'), 
                             (5,'C'), (11,'D')]
        self.testhand_2pairs=[(12,'H'), (12,'C'), (3,'H'), (11,'S'), (14,'H'), 
                             (5,'C'), (11,'D')]
        self.testhand_1pair=[(13,'H'), (12,'C'), (3,'H'), (11,'S'), (14,'H'), 
                             (5,'C'), (11,'D')]
        self.testhand_highcard=[(13,'H'), (12,'C'), (3,'H'), (11,'S'), (2,'H'), 
                             (5,'C'), (8,'D')]
    
    def test_lessthan7(self): 
        self.assertRaises(ValueError,eval_hand,self.test_lesscards)
        
    def test_repeating_cards(self):
        self.assertRaises(ValueError,eval_hand,self.testrep)
    
    def test_straight_flush(self):
        self.assertEqual(eval_hand(self.testhand_strflush), [9,5,0,0])
        
    def test_4ofakind(self):
        self.assertEqual(eval_hand(self.testhand_4ofakind), [8,10,9,0])
        
    def test_fullhouse(self):
        self.assertEqual(eval_hand(self.testhand_fullhouse), [7,5,6,0])
        
    def test_flush(self):
        self.assertEqual(eval_hand(self.testhand_flush), [6,0,0,[14,9,7,5,3]])
        
    def test_straight(self):
        self.assertEqual(eval_hand(self.testhand_straight), [5,5,0,0])
        
    def test_3ofakind(self):
        self.assertEqual(eval_hand(self.testhand_3ofakind), [4,10,0,[11,9]])
        
    def test_2pairs(self):
        self.assertEqual(eval_hand(self.testhand_2pairs), [3,12,11,14])
    
    def test_1pair(self):
        self.assertEqual(eval_hand(self.testhand_1pair), [2,11,0,[14,13,12]])
        
    def test_highcard(self):
        self.assertEqual(eval_hand(self.testhand_highcard), [1,0,0,[13,12,11,8,5]])
    

if __name__ == '__main__':
    unittest.main()
