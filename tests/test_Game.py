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
from Player import Player


class GameTestCase(unittest.TestCase):
    """tests for Strategy class"""
    
    def setUp(self):   
        pass
        
    def test_1player(self):
        with self.assertRaises(ValueError) as er:
            Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]}],
                    maxrounds=1, console_print=False)
        self.assertEqual('between 2 and 10 valid players need to be defined',
                    str(er.exception))

    def test_3p_game_noten_bb(self):
        self.g=Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                     {'name':'p2', 'balance':20, 'cards':[(2,'S'),(6,'D')]},
                     {'name':'p3', 'balance':7, 'cards':[(14,'C'),(14,'H')]}],
                    round_req={'flop':[(6, 'S'), (8, 'H'), (3, 'S')],
                               'turn':[(5, 'D')], 'river':[(5,'S')]},
                    maxrounds=1, console_print=False)
        self.g.play()
        self.assertTrue(self.g.players_active[0].balance==20 and
                        self.g.players_active[1].balance==15 and
                        self.g.players_active[2].balance==12)
 
    def test_3p_game_noten_sb(self):
        self.g=Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                     {'name':'p2', 'balance':20, 'cards':[(2,'S'),(6,'D')]},
                     {'name':'p3', 'balance':4, 'cards':[(14,'C'),(14,'H')]}],
                    round_req={'flop':[(6, 'S'), (8, 'H'), (3, 'S')],
                               'turn':[(5, 'D')], 'river':[(5,'S')]},
                    maxrounds=1, console_print=False)
        self.g.play()
        self.assertTrue(self.g.players_active[0].balance==15 and
                        self.g.players_active[1].balance==25 and
                        self.g.players_init[2] not in self.g.players_active)
        
    def test_2p_game_noten_sb(self):
        with self.assertRaises(ValueError) as er:
            Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                  {'name':'p2', 'balance':4, 'cards':[(14,'C'),(14,'H')]}],
                  maxrounds=1, console_print=False)
        self.assertEqual('between 2 and 10 valid players need to be defined',
                         str(er.exception))
        
    def test_2p_game_assign_players(self):
        self.g=Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                  {'name':'p2', 'balance':20, 'cards':[(14,'C'),(14,'H')]}],
                  maxrounds=1, console_print=False)
        self.p=Player('testplayer')
        with self.assertRaises(ValueError) as er:
            self.g.assign_players(self.p)
        self.assertEqual('Some players already defined for a game',
                         str(er.exception))
        
    def test_2p_game_assign_players2(self):
        self.g=Game(None, maxrounds=1, console_print=False)
        self.p1=Player({'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]})
        self.p2=Player({'name':'p2', 'balance':4, 'cards':[(14,'C'),(14,'H')]})
        with self.assertRaises(ValueError) as er:
            self.g.assign_players([self.p1])
        self.assertEqual('between 2 and 10 valid players need to be assigned',
                         str(er.exception))
 
    def test_3p_game_noten_sb_2(self):
        self.g=Game([{'name':'p1', 'balance':20, 'cards':[(2,'C'),(7,'H')]},
                     {'name':'p2', 'balance':20, 'cards':[(2,'S'),(6,'D')]},
                     {'name':'p3', 'balance':4, 'cards':[(14,'C'),(14,'H')]}],
                    round_req={'flop':[(6, 'S'), (8, 'H'), (3, 'S')],
                               'turn':[(5, 'D')], 'river':[(5,'S')]},
                    maxrounds=1, button_idx=2, console_print=False)
        self.g.play()
        self.assertTrue(self.g.players_active[0].balance==15 and
                        self.g.players_active[1].balance==17 and
                        self.g.players_active[2].balance==12 )
    
    def test_issue_wrongsidepot_minusraise(self):
        self.g=Game([{'name':'p1', 'balance':1985, 'cards':[(12, 'S'), (9, 'S')]},
                     {'name':'p2', 'balance':1015, 'cards':[(9, 'H'), (3, 'H')]}],
                    round_req={'flop':[(7, 'S'), (10, 'C'), (9, 'C')],
                               'turn':[(5, 'S')], 'river':[(10,'H')]},
                    maxrounds=1, button_idx=0, console_print=False)

        self.g.play()
        self.assertTrue(self.g.players_init[0].balance==3000 and
                        self.g.players_init[1].balance==0 )
    
    def test_issue_raise0(self):
        self.g=Game([{'name':'p1', 'balance':1100, 'cards':[(10, 'H'), (13, 'S')]
                      ,'strat':'sassimple'},
                     {'name':'p2', 'balance':1900, 'cards':[(4, 'C'), (4, 'H')]}],
                    round_req={'flop':[(3, 'S'), (4, 'D'), (8, 'H')],
                               'turn':[(12, 'S')], 'river':[(8,'C')]},
                    maxrounds=1, button_idx=1, console_print=False)

        self.g.play()
        self.assertTrue(self.g.players_init[0].balance==0 and
                        self.g.players_init[1].balance==3000 )
    
    
if __name__ == '__main__':
    unittest.main()
