
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from Game import Game


if __name__ == '__main__':
    g=Game([{'name':'brtkl', 'strat':'sassimple'}
            , {'name':'c1', 'strat':'sasmonkey'}
            , {'name':'c2', 'strat':'test'}
            , {'name':'c3', 'strat':'usebetmeth1'}
            ]
           , mode='sim'
           , simnum_prob=10000
           , log=True
           , logsql=False
           , maxrounds=3
           )
    g.play()
    