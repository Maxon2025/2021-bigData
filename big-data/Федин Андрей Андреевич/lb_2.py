import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/kit8nino/2021-bigData/main/_lab-2/GoT/battles.csv', header=0)\

defenderBattlesPerYear = data.groupby(['defender_1','year'])['name'].nunique().unstack()
defenderBattlesPerYear.fillna(0,inplace=True)

size = len(defenderBattlesPerYear.index)
width = 0.4

x = [np.linspace(0,12*1.2+0.2*11,12) + 0.4*i for i in range(3)]
y = [battles[1].array for battles in defenderBattlesPerYear.iteritems()]

fig, ax = plt.subplots(figsize=(12,6))

for x_,y_ in zip(x,y):
    ax.bar(x_,y_,width=0.4)
    
ax.set_xticks(ticks = x[0]+0.6)
ax.set_xticklabels(labels=defenderBattlesPerYear.index, rotation=90)
ax.legend(defenderBattlesPerYear.columns)

plt.show()