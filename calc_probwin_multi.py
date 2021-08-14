# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:44:33 2021

@author: brtk
"""
import multiprocessing as mp
from calc_probwin import calc_probwin
from calc_probwin_1pos import calc_probwin_1pos
from _util_managedb import load_lkp


if 'lkp20210626' not in globals():
    lkp20210626=load_lkp()
    
def calc_probwin_multi(hand, table, n=2, type='def', simnum=10000
                       , lkp=lkp20210626, roundnum=10):
    if __name__ == '__main__' and table:
        mp.freeze_support()
        
        np=mp.cpu_count()
        part_count=round(simnum/np)
        arg_tmp=(part_count, n, hand, table, type, lkp, roundnum)
        res1=mp.Pool().starmap(calc_probwin_1pos, [arg_tmp]*np)
        r_pwin=0
        r_pdraw=0
        for r1 in res1:
            r_pwin+=r1[0]
            r_pdraw+=r1[1]
        
        return [round(r_pwin/np,roundnum), round(r_pdraw/np,roundnum)
              , round(1-r_pwin/np-r_pdraw/np, roundnum), 'sim_mult' ]
        
    else:
        return calc_probwin(hand, table, n=n, type=type, simnum=simnum
                            , lkp=lkp, roundnum=roundnum)
    
    
    
    
    
    
    
    
    
    