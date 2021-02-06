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
from Strategy import Strategy


class StrategyTestCase(unittest.TestCase):
    """tests for Strategy class"""
    
    def setUp(self):
        self.s=Strategy()
 
    
    
if __name__ == '__main__':
    unittest.main()
