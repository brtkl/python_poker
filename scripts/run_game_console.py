
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import Game


g=Game.Game([{'name':'brtkl', 'type':'human'}
        , {'name':'c1', 'strat':'sasmonkey'}
        , {'name':'c2', 'strat':'test'}
        , {'name':'c3', 'strat':'usebetmeth1'}
        ]
       , mode='interactive'
       , simnum_prob=2000
       )
g.play()