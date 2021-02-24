
import os
import Game
os.chdir(r'D:\FX\_GLOBAL\learning\python\poker')


g=Game.Game([{'name':'brtkl', 'type':'human'}
        , {'name':'c1', 'strat':'sasmonkey'}
        , {'name':'c2', 'strat':'test'}
        , {'name':'c3', 'strat':'usebetmeth1'}
        ]
       , mode='interactive'
       , simnum_prob=2000
       )
g.play()