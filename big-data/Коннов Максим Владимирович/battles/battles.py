import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def tables(data, keys, pred, group, column):
    table = data[pred(data[keys]) == True]
    table = table.groupby(group)[column].nunique()
    none = data[pred(data[keys]) == False][column].count()
    names = [*table.index.array, *['None']]
    values = [*table.tolist(), *[none]]
    return [names, values]

def normal(s,p):
    n = np.array(s)
    return n / (sum(n ** p) ** (1/p))

def draw(values, labels=[], normalize=True):
    fig, ax = plt.subplots()
    ax.pie(values,normalize=normalize)
    ax.legend(labels,loc='upper left', bbox_to_anchor=(1.1,1))
    plt.show()


csv = pd.read_csv('battles.csv',header=0)

names, values = tables(
    csv,
    keys = [f'attacker_{i}' for i in range(1,5)],
    pred = lambda n: n.count(axis='columns') == 1,
    group = 'attacker_1',
    column = 'name'
)

draw(values, names)
draw(normal(values,1), names, normalize=False) #нормолизация вручную
