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


class PlayerTestCase(unittest.TestCase):
    """tests for Player class"""
    
    def setUp(self):
        self.p=Player('playername')
    
    def test_updatebalance(self):
        self.p.updatebalance(-480)
        self.assertTrue(self.p.balance==520 and self.p.bet==480)
    
    def test_updatebalance_only(self):
        self.p.updatebalance(-1000, balanceonly=1)
        self.assertTrue(self.p.balance==0 and self.p.bet==0)
        
    
if __name__ == '__main__':
    unittest.main()
