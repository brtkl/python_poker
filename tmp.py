# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:38:10 2021

@author: brtk
"""
import os
os.chdir(r'D:\FX\_GLOBAL\learning\python\poker')
from eval_hand import eval_hand
from eval_hand_old import eval_hand_old
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



#g=Game([{'name':'brtkl', 'balance':1000, 'cards'=[]},
#        {'name':'c1', 'balance':1000, 'cards'=[]},
#        {'name':'c2', 'balance':1000, 'cards'=[]}],
#       round_req={'flop':[], 'turn':[], 'river':[]})

#g=Game(['brtkl','c1','c2'])
#g.play()





s=Simulation([{'name':'c1', 'strat':'test'}
              , {'name':'c2', 'strat':'sasmonkey'}
              , {'name':'c3', 'strat':'sassimple'}
              , {'name':'c4', 'strat':'usebetmeth1'}]
             , simnum_prob=500
             , maxrounds=20
       )
s.run_sim()
s.summary()

from Player import Player
p1=Player({'name':'20210321_p1_test', 'strat':'test'})
p2=Player({'name':'20210321_p2_sasmonkey', 'strat':'sasmonkey'})
p3=Player({'name':'20210321_p3_sassimple', 'strat':'sassimple'})
p4=Player({'name':'20210321_p4_usebetmeth1', 'strat':'usebetmeth1'})

save_player(p1)
save_player(p2)
save_player(p3)
save_player(p4)


s=Simulation([{'name':'c1', 'strat':'test'}
              , {'name':'c3', 'strat':'sassimple'}]
             , simnum_prob=500
             , maxrounds=20
             , console_print='Y'
       )
s.run_sim()
s.summary()


print(s.players_sim_init[0].__dict__)
print(c1_new.__dict__)

import pickle
with open('data\\players\\c1_20210321.pkl', 'wb') as output:
    pickle.dump(s.players_sim_init[0], output, pickle.HIGHEST_PROTOCOL)


with open('data\\players\\c1_20210321.pkl', 'rb') as input:
    c1_new = pickle.load(input)






import os
os.chdir(r'D:\FX\_GLOBAL\learning\python\poker')
from eval_hand import eval_hand
from eval_hand_old import eval_hand_old
from calc_probwin import calc_probwin
from Deck import Deck

a=Deck()
b=a.draw(7)


for i in range(100000):
    check=eval_hand_new2(b)
    
for i in range(100000):
    check=eval_hand(b)

for i in range(100000):
    check=eval_hand_old(b)



for x in range(10):
    for y in range(10):
        print(x*y)
        if x*y > 90:
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break





