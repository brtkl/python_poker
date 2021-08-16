# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:48:07 2021

@author: brtk
"""

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import _util_pickl
from Player import Player
from _util_managedb import save_stats,select_all

p1=Player({'name':'20210322_p1_test', 'strat':'test'})
p2=Player({'name':'20210322_p2_sassimple', 'strat':'sassimple'})

_util_pickl.save_player(p1, overwrite='N')
_util_pickl.save_player(p2, overwrite='N')







p1=Player({'name':'20210814_p1_test', 'strat':'test'})
p2=Player({'name':'20210814_p2_sasmonkey', 'strat':'sasmonkey'})
p3=Player({'name':'20210814_p3_sassimple', 'strat':'sassimple'})
p4=Player({'name':'20210814_p4_usebetmeth1', 'strat':'usebetmeth1'})



p5=Player({'name':'20210815_p5_usebetmeth2', 'strat':'usebetmeth2'})
p6=Player({'name':'20210815_p6_tryharder', 'strat':'tryharder'})
p7=Player({'name':'20210816_p7_tryharder2', 'strat':'tryharder2'})
p8=Player({'name':'20210816_p8_potexp', 'strat':'potexp'})

save_stats(p8)
