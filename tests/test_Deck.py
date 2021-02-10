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
from Deck import Deck


class DeckTestCase(unittest.TestCase):
    """tests for Deck class"""
    
    def setUp(self):
        self.d=Deck()
 
    def test_deck(self):
        tmp=[i[0] for i in self.d.cards]
        tmpc=[i[1] for i in self.d.cards]
        self.assertTrue(min(tmp)==2 and max(tmp)==14 and len(tmp)==52)
        self.assertTrue(set(tmpc) == set(['H','C','S','D']) and len(tmpc)==52)
    
    def test_shuffle(self):
        tmp=self.d.cards[:]
        self.d.shuffle()
        self.assertTrue(tmp != self.d.cards and len(tmp)==len(self.d.cards))

    def test_draw(self):
        tst=self.d.draw(n=5)
        self.assertTrue(len(self.d.cards)==47 and tst not in self.d.cards)
    
    def test_draw_selected(self):
        tst=self.d.draw(cards=[(14,'H'), (13,'C')])
        self.assertTrue(len(self.d.cards)==50 and tst not in self.d.cards 
                        and [(14,'H'), (13,'C')] == tst)
    
    def test_draw_deflt(self):
        tst=self.d.draw()
        self.assertTrue(len(self.d.cards)==51 and tst not in self.d.cards)


    
if __name__ == '__main__':
    unittest.main()
