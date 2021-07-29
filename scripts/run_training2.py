
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from Training import Training

t=Training(['20210322_p1_test'
            , '20210322_p2_sassimple']
           , ngames=100
           , maxrounds=50
           , simnum_prob=5000)
t.train()
