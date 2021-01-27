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
        
    def draw(self,n=1):
        res=[]
        for i in range(0,n):
            res.append(self.cards.pop(0))
        return res

class Player():
    """ defining a player with attributes"""
    def __init__(self, name, capital=1000, strategy='default'):
        self.capital=capital
        self.strategy=strategy
        self.name=name
    
        
class Round():
    """ round of a game. Game consists of rounds, round consist of stages
    (pre-flop, flop, turn, river) """
    def __init__(self, players=[], bblind=10, sblind=5):
        deck=Deck()
        deck.shuffle()
        self.players=players
        self.bblind=bblind
        self.sblind=sblind
        self.stage='pre-flop'



    