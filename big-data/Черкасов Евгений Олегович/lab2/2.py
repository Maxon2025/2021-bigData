import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def map_data(data, keys, pred, group, column):
    table = data[pred(data[keys]) == True]
    table = table.groupby(group)[column].nunique()
    
    none = data[pred(data[keys]) == False][column].count()
   
    labels = [*table.index.array, *['None']]
    values = [*table.tolist(), *[none]]
    
    return [labels, values]

def drawPie(values, labels=[], normalize=True):
    fig, ax = plt.subplots()
    ax.pie(values,normalize=normalize)
    ax.legend(labels,loc='upper left', bbox_to_anchor=(1.1,1))
    plt.show()
    
def norm(x,p):
    v = np.array(x)
    return v / (sum(v ** p) ** (1/p))
    #return (v - v.min()) / (v.max() - v.min())
    
def toDataFrame(labels, values):
    return pd.DataFrame({'House' : labels, 'Battles': values})

data = pd.read_csv('GoT/battles.csv',header=0)

labels, values = map_data(
    data, 
    keys = [f'attacker_{i}' for i in range(1,5)],
    pred = lambda x: x.count(axis='columns') == 1,
    group = 'attacker_1',
    column = 'name'
)

drawPie(values, labels)
drawPie(norm(values,1), labels, normalize=False) #нормолизация вручную
print(toDataFrame(labels,values))