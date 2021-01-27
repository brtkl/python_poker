# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:38:10 2021

@author: brtk
"""
from eval_hand import eval_hand
from calc_probwin import calc_probwin
from Classes import Deck


d1=Deck()
d1.shuffle()


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
table=d1.draw(n=5)

calc_probwin(myhand, table)