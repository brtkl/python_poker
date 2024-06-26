# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:25:18 2021

@author: brtk
"""

def eval_hand(hand):
    """ evaluate hand - recognize poker hand within 7 cards"""
    if len(hand)!=7 or isinstance(hand,list) != True:
        raise ValueError('Exactly 7 cards in a list should be evaluated')
    
    if len(hand) != len(set(hand)):
        raise ValueError('repeating cards in the input data')
        
    #returning
    #[rank, rank_h1, rank_h2, remain_import]
    #eg 1 [8,5,9,0] describes 4 of a kind (card with rank 5) with the remaining
    #     highest card with rank 9
    #eg 2 [2,14,0,[7,5,2]] describes a pair of aces, with the remaining 3 
    #     highest cards being 7, 5, 2
    
    numhand=sorted(list(set([i[0] for i in hand])), reverse=True)
    colhand=list(set([i[1] for i in hand]))
    
    ##straight flush (9)
    if len(numhand)>=5 and len(colhand)<=3:
        for i9 in numhand:
            if i9==5:
                tmp=14
            elif i9>5:
                tmp=i9-4
            else:
                break
            for k in colhand:
                if set([(i9,k),(i9-1,k),(i9-2,k),(i9-3,k),(tmp,k)]).issubset(set(hand)):
                    rank=9
                    rank_h1=i9
                    return [rank, rank_h1, 0, 0]
        
        
    ##4 of a kind (8)
    if len(numhand)<=4:
        for i8 in numhand:
            if [i[0] for i in hand].count(i8)==4:
                rank=8
                rank_h1=i8
                tmp=[i[0] for i in sorted(hand,reverse=True) if i[0]!=i8]
                return [rank, rank_h1, tmp[0], 0]
    
    ##full house (7)
    if len(numhand)<=4:
        for i7 in numhand:
            if [i[0] for i in hand].count(i7)==3:
                for i7_1 in numhand:
                    if i7_1 != i7 and [i[0] for i in hand].count(i7_1)>=2:
                        rank=7
                        rank_h1=i7
                        rank_h2=i7_1
                        return [rank, rank_h1, rank_h2, 0]

    ##flush (6)
    if len(numhand)>=5 and len(colhand)<=3:
        for i6 in colhand:
            if [i[1] for i in hand].count(i6)>=5:
                rank=6
                tmp=[i[0] for i in sorted(hand,reverse=True) if i[1]==i6]
                return [rank, 0, 0, tmp[0:5]]            
    
    ##straight (5)
    if len(numhand)>=5:
        for i5 in numhand:
            if i5==5:
                tmp=14
            elif i5>5:
                tmp=i5-4
            else: 
                break
            if set([i5,i5-1,i5-2,i5-3,tmp]).issubset(set([i[0] for i in hand])):
                rank=5
                rank_h1=i5
                return [rank, rank_h1, 0, 0]
    
    ##3 of a kind (4)
    if len(numhand)<=5:
        for i4 in numhand:
            if [i[0] for i in hand].count(i4)==3:
                rank=4
                rank_h1=i4
                tmp=[i[0] for i in sorted(hand,reverse=True) if i[0]!=i4]
                return [rank, rank_h1, 0, tmp[0:2]]
    
    ##2 pairs (3)
    if len(numhand)<=5:
        for i3 in numhand:
            if [i[0] for i in hand].count(i3)==2:
                for i3_1 in numhand:
                    if i3_1 != i3 and [i[0] for i in hand].count(i3_1)==2:
                        rank=3
                        rank_h1=i3
                        rank_h2=i3_1
                        tmp=[i[0] for i in sorted(hand,reverse=True) if i[0] 
                             not in [i3, i3_1]]
                        return [rank, rank_h1, rank_h2, tmp[0]]
    
    ##1 pair (2)
    if len(numhand)<=6:
        for i2 in numhand:
            if [i[0] for i in hand].count(i2)==2:
                rank=2
                rank_h1=i2
                tmp=[i[0] for i in sorted(hand,reverse=True) if i[0]!=i2]
                return [rank, rank_h1, 0, tmp[0:3]]

    ##high card (1)
    tmp=[i[0] for i in sorted(hand,reverse=True)]
    return [1, 0, 0, tmp[0:5]]

