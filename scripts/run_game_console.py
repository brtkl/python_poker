
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import Game, random

_gc_numplays=0
while _gc_numplays not in ('1','2','3'):
    _gc_numplays=input('##Specify number of opponents (1-3) \n')
    if _gc_numplays=='exit':
        sys.exit(0)              

_gc_allplayers=[{'name':'c1', 'strat':'sasmonkey'}
            , {'name':'c2', 'strat':'test'}
            , {'name':'c3', 'strat':'usebetmeth1'}
            ]
random.shuffle(_gc_allplayers)
_gc_selplayers=_gc_allplayers[:int(_gc_numplays)]

g=Game.Game([{'name':'brtkl', 'type':'human'}]+_gc_selplayers
       , mode='interactive'
       , simnum_prob=10000
       )
g.play()