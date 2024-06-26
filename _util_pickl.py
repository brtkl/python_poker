# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:14:39 2021

@author: brtk
"""
import pickle

def save_player(obj
                , overwrite=False
                , filename=None):    
    if player_exists(filename) and overwrite != True:
            raise ValueError('Player with this name already exists')
    else:
        if filename==None:
            filename=obj.name
        with open(f'data\\players\\{filename}.pkl', 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_player(filename, verify_comp=True):
    try:
        with open(f'data\\players\\{filename}.pkl', 'rb') as input:
            tmp=pickle.load(input)
        if verify_comp==True and tmp.type != 'comp':
            raise ValueError('Only type=\'comp\' players can be loaded')
        return tmp
    except FileNotFoundError:
        print('Player doesn\'t exist')
    
def player_exists(filename):
    try:
        with open(f'data\\players\\{filename}.pkl', 'rb'):
            return 1
    except FileNotFoundError:
        return 0
    