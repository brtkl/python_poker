# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:38:10 2021

@author: brtk
"""
import os
os.chdir(r'D:\FX\_GLOBAL\learning\python\poker')
from eval_hand import eval_hand
from calc_probwin import calc_probwin
from Deck import Deck


d1=Deck()
d1.shuffle()

highcheck=[(14,'S'),(14,'H')]
highcheck=[(14,'C'),(13,'C')]
calc_probwin(highcheck,[])

tst=d1.cards


myhand=d1.draw(n=2)
ophand=d1.draw(n=2)

#flop
table=d1.draw(n=3)
#turn
table+=d1.draw()
#river
table+=d1.draw()



eval_hand(myhand+table)
    

#hand.sort(key = operator.itemgetter(0), reverse = True)

calc_probwin(myhand, table)




d1=Deck()
d1.shuffle()

myhand=d1.draw(n=2)
table=d1.draw(n=3)

calc_probwin(myhand, table)