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


class GameTestCase(unittest.TestCase):
    """tests for Strategy class"""
    
    def setUp(self):   
        pass
        
    def test_3p_game_noten_bb(self):
        self.g=Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                     {'name':'p2', 'balance':20, 'cards':[(2,'S'),(6,'D')]},
                     {'name':'p3', 'balance':7, 'cards':[(14,'C'),(14,'H')]}],
                    maxrounds=1)
        self.g.play()
        self.assertTrue(self.g.players_active[0].balance==20 and
                        self.g.players_active[1].balance==15 and
                        self.g.players_active[2].balance==12)
 
    def test_3p_game_noten_sb(self):
        self.g=Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                     {'name':'p2', 'balance':20, 'cards':[(2,'S'),(6,'D')]},
                     {'name':'p3', 'balance':4, 'cards':[(14,'C'),(14,'H')]}],
                    maxrounds=1)
        self.g.play()
        self.assertTrue(self.g.players_active[0].balance==15 and
                        self.g.players_active[1].balance==25 )
    
    
if __name__ == '__main__':
    unittest.main()
