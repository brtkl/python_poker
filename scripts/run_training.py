
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from Training import Training

t=Training(['20210814_p1_test'
            , '20210814_p2_sasmonkey'
            , '20210814_p3_sassimple'
            , '20210814_p4_usebetmeth1']
           , ngames=1000
           , simnum_prob=10000)
t.train()


