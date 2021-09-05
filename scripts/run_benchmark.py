
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from calc_probwin import calc_probwin
from calc_probwin_multi import calc_probwin_multi
import time
import pandas


def checktime(simnum, n=2, cores=16):
    start_time = time.time()
    r1=calc_probwin(a[:2],a[2:],simnum=simnum, n=n)
    res1=time.time() - start_time
    print("calc_probwin \t\t %s, n=%s: %s seconds" % (simnum, n, res1))
    
    start_time = time.time()
    r2=calc_probwin_multi(a[:2],a[2:],simnum=simnum, cores=cores)
    res2=time.time() - start_time
    print("calc_probwin_multi \t %s, n=%s, cores=%s: %s seconds" % 
          (simnum, n, cores, res2))
    
    reslist.append({'simnum':simnum, 'n':n, 'cores':cores, 'res_std':res1
                    ,'res_multi':res2})
    

if __name__ == '__main__':
    
    a=[(8,'H'), (5,'C'), (11,'D'), (14,'D'), (2,'S')]
    
    reslist=[]
    for i in range(2,11):
        for c in [1,2,3,4,6,8]:
            for t in range(1,21):
                # checktime(5000, n=i, cores=c)
                checktime(10000, n=i, cores=c)
                # checktime(20000, n=i, cores=c)
    
    newres=pandas.DataFrame(reslist)
    res_avg=newres.groupby(['simnum','n', 'cores']).mean()