# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:44:33 2021

@author: brtk
"""
from itertools import combinations
from Deck import Deck
from eval_hand import eval_hand
import random

def calc_probwin(hand, table, n=2, type='def', simnum=10000):
    """ calc probability of winning with a given hand.
        Returns probability of winning, drawing and loosing""" 
    
    if table==None:
        table=[]
        
    if len(hand)!=2 or len(table)>5 or isinstance(hand,list) != True:
        raise ValueError('2 cards in hand and between 0 and 5 cards in a table'
                         +' are needed in lists')
    
    if len(hand+table) != len(set(hand+table)):
        raise ValueError('repeating cards in the input data')
    
    if len(table)==5 and type=='def':
        type='exact'
    elif type=='def':
        type='simul'
        
    if not (2<=n<=10):
        raise ValueError('n needs to be between 2 and 10')
        
    if type=='exact':
        tmpdeck=Deck()
        tmpdeck2=[i for i in tmpdeck.cards if i not in hand+table]
        
        nwin=0
        ndra=0
        nlos=0
        ntot=0
        
        comb_op=list(combinations(tmpdeck2, 2))
        
        for i in comb_op:
            tmpdeck3=[j for j in tmpdeck2 if j not in list(i)]
            comb_tab=list(combinations(tmpdeck3, 5-len(table)))
            for i2 in comb_tab:
                tmp_h=eval_hand(hand+table+list(i2))
                tmp_com=eval_hand(list(i)+table+list(i2))
                ntot += 1
                if tmp_h>tmp_com:
                    nwin += 1
                elif tmp_h==tmp_com:
                    ndra += 1
                else:
                    nlos += 1
        
        return [round(nwin/ntot,3), round(ndra/ntot,3), round(nlos/ntot,3), 
                'exact']
    
    if type=='simul':
        tmpdeck=Deck()
        tmpdeck2=[i for i in tmpdeck.cards if i not in hand+table]
        
        nwin=0
        ndra=0
        nlos=0
        ntot=0
        
        for i in range(simnum):
            #random.shuffle(tmpdeck2)
            rand_row=random.sample(tmpdeck2,2*(n-1)+5-len(table))
            #rand_row=tmpdeck2[:9-len(hand+table)]
            tmp_h=eval_hand(hand+table+rand_row[2*(n-1):])
            tmp_comall=[]
            for i in range(n-1):    
                tmp_comall.append(
                    eval_hand(rand_row[i*2:i*2+2]+table+rand_row[2*(n-1):]))
                
            ntot += 1
            if tmp_h>max(tmp_comall):
                nwin += 1
            elif tmp_h==max(tmp_comall):
                ndra += 1
            else:
                nlos += 1
    
        return [round(nwin/ntot,3), round(ndra/ntot,3), round(nlos/ntot,3), 
                'sim']
    
    
    
    
    
    
    
    