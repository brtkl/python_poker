# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:32:25 2021

@author: brtk
"""

import os
os.chdir(r'D:\FX\_GLOBAL\learning\python\poker')

from Round import Round


class Game():
    pass

r1=Round()
r1.assigncards()
r1.assignblinds()

#pre-flop bets
r1.betting()

#flop bets
r1.nextstage('flop')
r1.betting()

#turn bets
r1.nextstage('turn')
r1.betting()

#river bets
r1.nextstage('river')
r1.betting()

r1.finalizeround()
