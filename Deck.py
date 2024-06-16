# -*- coding: utf-8 -*-
"""
Created on 25JAN2021

@author: brtk

deck class
"""
import random

class Deck():
    """ Deck of cards class. 
    Methods: Shuffling and drawing cards from a deck."""
    
    def __init__(self):
        self.cards=[]
        for i in ['C','D','H','S']:
            for j in range (2,15):
                self.cards.append((j,i)) #f"{j:02d}_{i}"
                
    def shuffle(self,times=1):
        for i in range(0,times):
            random.shuffle(self.cards)
        
    def draw(self,n=1,cards=[]):
        if not cards:
            res=[]
            for i in range(0,n):
                res.append(self.cards.pop(0))
            return res
        elif cards:
            for i in cards:
                self.cards.remove(i)
            return cards

    def add(self,cards,top=True):
        for i in cards:
            if i in self.cards:
                raise ValueError('repeating cards in the input data')
        if top:
            self.cards=cards+self.cards
        else:
            self.cards=self.cards+cards


    