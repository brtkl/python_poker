
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from Training import Training

t=Training(['20210321_p1_test'
            , '20210321_p2_sasmonkey'
            , '20210321_p3_sassimple'
            , '20210321_p4_usebetmeth1']
           , ngames=1000
           , simnum_prob=500)
t.train()
