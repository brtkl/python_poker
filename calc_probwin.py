# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:44:33 2021

@author: brtk
"""
from itertools import combinations
from Deck import Deck
from eval_hand import eval_hand
import random
import json
if 'lkp20210626' not in globals():
    with open(r'data\probs\2cards_simnum50000_lookup.json') as fp:
                lkp20210626=json.load(fp)

def calc_probwin(hand, table, n=2, type='def', simnum=10000, lkp=lkp20210626):
    """ calc probability of winning with a given hand.
        Returns probability of winning, drawing and loosing""" 
    
    if table==None:
        table=[]
        
    if len(hand)!=2 or len(table)>5 or isinstance(hand,list) != True:
        raise ValueError('2 cards in hand and between 0 and 5 cards in a table'
                         +' are needed in lists')
    
    if len(hand+table) != len(set(hand+table)):
        raise ValueError('repeating cards in the input data')
    
    if len(table)==5 and n==2 and type=='def':
        type='exact'
    elif type=='def' and table==[]:
        type='lookup'
    elif type=='def':
        type='simul'
        
    if not (2<=n<=10):
        raise ValueError('n needs to be between 2 and 10')
        
    if type=='lookup':
        
        arg=[min(hand[0][0], hand[1][0]), max(hand[0][0], hand[1][0])
             , 1 if hand[0][1]==hand[1][1] else 0, n]
        return lkp[f'{arg[0]}_{arg[1]}_{arg[2]}_{arg[3]}'][:3]+['lookup']
    
    elif type=='simul':
        tmpdeck=Deck()
        tmpdeck2=[i for i in tmpdeck.cards if i not in hand+table]
        
        nwin=0
        ndra=0
        nlos=0
        ntot=0
        
        for i in range(simnum):
            rand_row=random.sample(tmpdeck2,2*(n-1)+5-len(table))
            tmp_h=eval_hand(hand+table+rand_row[2*(n-1):])
            tmp_max_comall=max([eval_hand(rand_row[i*2:i*2+2]+table+
                                          rand_row[2*(n-1):]) 
                                for i in range(n-1)])
                        
            if tmp_h<tmp_max_comall:
                nlos += 1
            elif tmp_h==tmp_max_comall:
                ndra += 1
            else:
                nwin += 1
                
    
        return [round(nwin/simnum,3), round(ndra/simnum,3)
                , round(nlos/simnum,3), 'sim']
        
    elif type=='exact' and n==2 and len(table)==5:
        tmpdeck=Deck()
        tmpdeck2=[i for i in tmpdeck.cards if i not in hand+table]
        
        nwin=0
        ndra=0
        nlos=0
        ntot=0
        
        comb_op=list(combinations(tmpdeck2, 2*(n-1) + 5-len(table)))
        
        for c in comb_op:
            tmp_h=eval_hand(hand+table+list(c)[2*(n-1):])
            tmp_max_comall=max([eval_hand(list(c)[i*2:i*2+2]+table+
                                          list(c)[2*(n-1):])
                                for i in range(n-1)])
            ntot += 1
            if tmp_h<tmp_max_comall:
                nlos += 1
            elif tmp_h==tmp_max_comall:
                ndra += 1
            else:
                nwin += 1
        
        return [round(nwin/ntot,3), round(ndra/ntot,3), round(nlos/ntot,3), 
                'exact']
    
    elif type=='exact':
        raise ValueError('exact can be only for n=2 and len(table)=5')
    
    
    
    