
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from Training import Training

if __name__ == '__main__':
    t=Training(['20210814_p1_test'
                , '20210814_p2_sasmonkey'
                , '20210814_p3_sassimple'
                , '20210814_p4_usebetmeth1' 
                , '20210815_p5_usebetmeth2' 
                , '20210815_p6_tryharder' ]
               , ngames=100
               , maxrounds = 50
               , simnum_prob=10000)
    t.train()
    
    
