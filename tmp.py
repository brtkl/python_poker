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



g=Game([{'name':'brtkl', 'type':'human'}
        , {'name':'c1', 'strat':'sasmonkey'}
        , {'name':'c2', 'strat':'test'}
        , {'name':'c3', 'strat':'usebetmeth1'}
        ]
       , mode='interactive'
       , simnum_prob=2000
       )
g.play()

g=Game([{'name':'brtkl'}
        , {'name':'c1', 'strat':'sasmonkey'}
        , {'name':'c2', 'strat':'test'}
        , {'name':'c3', 'strat':'usebetmeth1'}
        ]
       , mode='sim'
       , simnum_prob=10000
       , maxrounds=100
       )
g.play()

d1=Deck()
d1.shuffle()

table=[(13,'D'),(14,'H'),(14,'C'),(13,'C')]
highcheck=[(14,'S'),(14,'H')]
# highcheck=[(14,'C'),(13,'C')]
calc_probwin(highcheck,table,n=10)
calc_probwin(highcheck,[],n=3)

table=[]
lowcheck=[(2,'S'),(7,'H')]
# highcheck=[(14,'C'),(13,'C')]
calc_probwin(lowcheck,table,n=1)

a=highcheck[:]

a.reverse()

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

class Y:
    def __init__(self,list):
        self.list=list

class X:
    def __init__(self,abc):
        self.abc=abc
        
class Z:
    def __init__(self,insty):
        self.check=insty
    

x1=X(1)
x2=X(2)
y1=Y([x1,x2])
z1=

tmp=[x1,x2]

tmp2=tmp[:]

tmp2[0].abc=7

tmp[0].abc

x1.abc

y1=X()

y1=X()

y1.abc=44
l1=[x1,y1]

l1.remove(y1)

a=1
b=a
a=2

r1.hplayer.balance


d1=Deck()
d1.shuffle()

myhand=d1.draw(n=2)
table=d1.draw(n=3)

calc_probwin(myhand, table)