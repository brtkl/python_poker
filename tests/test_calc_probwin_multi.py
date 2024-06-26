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
from calc_probwin_multi import calc_probwin_multi
from calc_probwin import calc_probwin
import numpy as np

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
        self.testhand_flush2=[(14,'H'), (13,'H'), (3,'H'), (9,'S'), (2,'H'), 
                             (5,'C'), (10,'H')]
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
        with self.assertRaises(ValueError) as er:
            calc_probwin_multi(self.test_lesscards,[],test=True)
        self.assertEqual('2 cards in hand and between 0 and 5 cards in a table'
                         +' are needed in lists',
                         str(er.exception))
        
    def test_repeating_cards(self):
        with self.assertRaises(ValueError) as er:
            calc_probwin_multi(self.testrep[:2],self.testrep[2:], test=True)
        self.assertEqual('repeating cards in the input data',str(er.exception))
        
    def test_wrong_exact(self):
        with self.assertRaises(ValueError) as er:
            calc_probwin_multi(self.testhand_highcard[:2],self.testhand_highcard[2:]
                         , n=3, type='exact', test=True)
        self.assertEqual('exact can be only for n=2 and len(table)=5',str(er.exception))
    
    def test_wrong_exact2(self):
        with self.assertRaises(ValueError) as er:
            calc_probwin_multi(self.testhand_highcard[:2],self.testhand_highcard[2:5]
                         , n=2, type='exact', test=True)
        self.assertEqual('exact can be only for n=2 and len(table)=5',str(er.exception))
    
    def test_wrongn(self):
        with self.assertRaises(ValueError) as er:
            calc_probwin_multi(self.testhand_strflush[:2], [], n=1, test=True)
        self.assertEqual('n needs to be between 2 and 10',str(er.exception))
        with self.assertRaises(ValueError) as er2:
            calc_probwin_multi(self.testhand_strflush[:2], [], n=11, test=True)
        self.assertEqual('n needs to be between 2 and 10',str(er2.exception))
    
    
    def test_multi(self):
        res=calc_probwin_multi(self.testhand_5any[:2], self.testhand_5any[2:]
                               , test=True)
        self.assertTrue(res[3]=='sim_mult')
        
    def test_cant_lose(self):
        self.assertTrue(calc_probwin_multi(self.testhand_strflush[:2],
                                      self.testhand_strflush[2:], test=True)[0]==1)
    def test_cant_lose2(self):
        self.assertTrue(calc_probwin_multi(self.testhand_4ofakind[:2],
                                     self.testhand_4ofakind[2:], test=True)[0]==1)
        
    def test_cant_lose2_sim(self):
        self.assertTrue(calc_probwin_multi(self.testhand_4ofakind[:2],
                                     self.testhand_4ofakind[2:], type='simul'
                                     , test=True)[0]==1)
        
    def test_high_prob(self):
        self.assertTrue(calc_probwin_multi(self.testhand_fullhouse[:2]
                                           , self.testhand_fullhouse[2:]
                                           , test=True)[0]>0.9)
                        
    def test_low_prob(self):
        self.assertTrue(calc_probwin_multi(self.testhand_highcard[:2]
                                           , self.testhand_highcard[2:]
                                           , test=True)[0]<
                        calc_probwin_multi(self.testhand_highcard[:2]
                                           , self.testhand_highcard[2:]
                                           , test=True)[2])
    
    def test_low_prob2(self):
        self.assertTrue(calc_probwin_multi(self.testhand_1pair[:2],
                                     self.testhand_1pair[2:], test=True)[0]<0.1)
                    
    def test_dif_def_exact(self):
        self.assertTrue(abs(calc_probwin_multi(self.testhand_straight[:2],
                                     self.testhand_straight[2:], type='exact', 
                                     test=True)[0]
                        -calc_probwin_multi(self.testhand_straight[:2],
                                     self.testhand_straight[2:], test=True)[0])==0)
                    
    def test_dif_sim_exact(self):
        self.assertTrue(abs(calc_probwin_multi(self.testhand_straight[:2],
                                     self.testhand_straight[2:],type='simul'
                                     , test=True)[0]
                        -calc_probwin_multi(self.testhand_straight[:2],
                                     self.testhand_straight[2:], test=True)[0])<0.01)
                    
    def test_dif_sim_exact2(self):
        self.assertTrue(abs(calc_probwin_multi(self.testhand_3ofakind[:2],
                                     self.testhand_3ofakind[2:],type='simul'
                                     , test=True)[0]
                        -calc_probwin_multi(self.testhand_3ofakind[:2],
                                     self.testhand_3ofakind[2:]
                                     , test=True)[0])<0.01)
        
    def test_dif_sim_lookup1(self):
        self.assertTrue(abs(calc_probwin_multi(self.testhand_3ofakind[:2],[], 
                                               type='lookup', test=True)[0]
                        -calc_probwin_multi(self.testhand_3ofakind[:2],[], 
                                            test=True)[0])==0)
        
    def test_dif_sim_lookup2(self):
        self.assertTrue(abs(calc_probwin_multi(self.testhand_3ofakind[:2],[], 
                                               type='lookup', test=True)[0]
                        -calc_probwin_multi(self.testhand_3ofakind[:2],[],type='simul'
                                            , simnum=50000, test=True)[0])<0.01)
        
    def test_2card_sim_high(self):
        self.assertTrue(calc_probwin_multi(self.testhand_2high,[],type='simul'
                                           , test=True)[0] >0.8)
        self.assertTrue(0.8>calc_probwin_multi(self.testhand_2high,[], 
                                               type='simul',n=3, test=True)[0]>0.7)
        
    def test_2card_sim_low(self):
        self.assertTrue(calc_probwin_multi(self.testhand_2low,[],type='simul'
                                           , test=True, simnum=20000)[0]<0.35)
        
    def test_3any(self):
        self.assertTrue(1>calc_probwin_multi(self.testhand_3any[:2],
                                     self.testhand_3any[2:],type='simul', 
                                     test=True)[0]>0)
        self.assertTrue(1>calc_probwin_multi(self.testhand_3any[:2],
                                     self.testhand_3any[2:],type='simul', 
                                     n=3, test=True)[0]>0)
        
    def test_4any(self):
        self.assertTrue(1>calc_probwin_multi(self.testhand_4any[:2],
                                     self.testhand_4any[2:], type='simul'
                                     , test=True)[0]>0)
        self.assertTrue(1>calc_probwin_multi(self.testhand_4any[:2],
                                     self.testhand_4any[2:], type='simul'
                                     , n=7, test=True)[0]>0)
        
    def test_5any(self):
        self.assertTrue(1>calc_probwin_multi(self.testhand_5any[:2],
                                     self.testhand_5any[2:],type='simul'
                                     , test=True)[0]>0)
        self.assertTrue(1>calc_probwin_multi(self.testhand_5any[:2],
                                     self.testhand_5any[2:],type='simul',n=9
                                     , test=True)[0]>0)
        
    def test_6any(self):
        self.assertTrue(1>calc_probwin_multi(self.testhand_6any[:2],
                                     self.testhand_6any[2:],type='simul'
                                     , test=True)[0]>0)
        self.assertTrue(1>calc_probwin_multi(self.testhand_6any[:2],
                                     self.testhand_6any[2:],type='simul'
                                     , n=10, test=True)[0]>0)
        
    def test_sumprob(self):
        a=calc_probwin_multi(self.testhand_5any[:2], self.testhand_5any[2:]
                             , test=True)
        self.assertAlmostEqual(a[0]+a[1]+a[2],1,places=2)
        
    def test_sumprob_n5(self):
        a=calc_probwin_multi(self.testhand_5any[:2], self.testhand_5any[2:]
                             , n=5, test=True)
        self.assertAlmostEqual(a[0]+a[1]+a[2],1,places=2)
        
    def test_increment_n10(self):
        self.assertTrue(calc_probwin_multi(self.testhand_5any[:2],[],n=2
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=3
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=4
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=5
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=6
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=7
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=8
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=9
                                           , type='lookup', test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=10
                                           , type='lookup', test=True))
        
    
    def test_increment_n10_simul(self):
        self.assertTrue(calc_probwin_multi(self.testhand_5any[:2],[],n=2, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=3, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=4, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=5, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=6, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=7, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=8, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=9, 
                                           type='simul', simnum=50000, test=True)>
                        calc_probwin_multi(self.testhand_5any[:2],[],n=10, 
                                           type='simul', simnum=50000, test=True))


    def test_variance(self):
        standard=[]
        multi=[]
        for i in range(100):
            multi.append(calc_probwin_multi(self.testhand_5any[:2]
                                            , self.testhand_5any[2:],n=3
                                            , simnum=15000, test=True)[0])
            standard.append(calc_probwin(self.testhand_5any[:2]
                                         , self.testhand_5any[2:],n=3
                                         , simnum=10000)[0])

        varmulti=np.var(multi)
        varstandard=np.var(standard)
        self.assertTrue(varmulti<varstandard)
        
        
if __name__ == '__main__':
    unittest.main()
