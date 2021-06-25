
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from itertools import combinations
import pandas as pd
from timeit import default_timer as timer


from Deck import Deck
from calc_probwin import calc_probwin

d1=Deck()
comb_all=list(combinations(d1.cards, 2))

df = pd.DataFrame(comb_all, columns =['c1', 'c2'])


for n in range(4,11):
    start = timer()
    df[f"n{n}"]=[calc_probwin(list(i),[],n=n, simnum=2000)[0] for i in comb_all]
    end = timer()
    print(end - start)


df.to_json('data\\probs\\2cards_prob_all.json', orient='records')




start = timer()
df["n3"]=[calc_probwin(list(i),[],n=3, simnum=2000)[0] for i in comb_all]
end = timer()
print(end - start)
