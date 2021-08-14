# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:44:33 2021

@author: brtk
"""
from calc_probwin import calc_probwin

def calc_probwin_1pos(simnum, n, hand, table, type, lkp, roundnum):
    return calc_probwin(hand=hand, table=table, n=n, type=type, simnum=simnum
                        , lkp=lkp, roundnum=roundnum)
    
    
    
    
    
    
    
    
    