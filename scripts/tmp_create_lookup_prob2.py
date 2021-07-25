

from calc_probwin import calc_probwin
import json

###for simnum=50000 the below code takes approx 12 hours to run
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

    
combnew_dict2 = {combnew[i][:4]: combnew[i][4] for i in range(len(combnew))}


with open(r'data\probs\2cards_simnum50000_lookup2.json', 'w') as fp:
    json.dump(combnew_dict, fp)
    
    