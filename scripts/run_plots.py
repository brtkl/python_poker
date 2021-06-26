
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
comb_all=list(combinations(range(2,15), 2))

df = pd.DataFrame(comb_all, columns =['c1', 'c2'])

combnew=[]
for i1 in range(2,15):
    for i2 in range(i1,15):
        for j in range(2):
            for n in range(2,11):
                if not(i1==i2 and j==1):
                    combnew.append([i1,i2,j,n,calc_probwin([(i1,'D'),(i2,'D' if j==1 else 'S')]
                                                           ,[],n=n,simnum=50000)])
                    print(f'{round((len(combnew)/1521)*100,2)}%')
        
combnew_dict = {f'{combnew[i][0]}_{combnew[i][1]}_{combnew[i][2]}_{combnew[i][3]}': 
                combnew[i][4] for i in range(len(combnew))}

for n in range(4,11):
    start = timer()
    df[f"n{n}"]=[calc_probwin(list(i),[],n=n, simnum=2000)[0] for i in comb_all]
    end = timer()
    print(end - start)


df.to_json('data\\probs\\2cards_prob_all_simnum2000.json', orient='records')
dfr = pd.read_json ('data\\probs\\2cards_prob_all_simnum2000.json')



start = timer()
df["n3"]=[calc_probwin(list(i),[],n=3, simnum=2000)[0] for i in comb_all]
end = timer()
print(end - start)



fig = px.bar(df, x=px.Constant('col'), y=['n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10'])
fig.update_layout(barmode='group')
offline.plot(fig,filename='probs.html')


df5 = pd.melt(df, id_vars=['c1','c2'], value_vars=df.columns[2:])



import plotly.express as px
import plotly.offline as offline
import plotly.graph_objects as go
from ipywidgets import widgets

c1_b = widgets.Dropdown(
    description='card1: ',
    # value="(2,'C')",
    options=df5['c1'].unique().tolist()
)

c2_b = widgets.Dropdown(
    options=df5['c2'].unique().tolist(),
    # value="(3,'C')",
    description='card2: ',
)

from IPython.display import display


# Assign an empty figure widget with two traces
trace1 = go.Bar(x=df5[:10]['variable'],y=df5[:10]['value'])
g = go.FigureWidget(data=[trace1],
                    layout=go.Layout(
                        title=dict(
                            text='probs'
                        )
                    ))



container = widgets.HBox([c1_b, c2_b])
display(widgets.VBox([container, g]))

offline.plot(g,filename='probs2.html')
