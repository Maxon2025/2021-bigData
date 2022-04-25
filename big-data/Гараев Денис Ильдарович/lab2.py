from os import name
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pandas.core.indexes.multi import MultiIndex

data = pd.read_csv(
    'https://raw.githubusercontent.com/kit8nino/2021-bigData/main/_lab-2/GoT/battles.csv', header=0)

# print( data.groupby(['year', 'defender_1'])['name'].nunique(dropna=True) )

fightsPerYear = data.groupby(['year', 'defender_1'])[
    'name'].nunique(dropna=True)
defenders = pd.Series(data['defender_1'].sort_values(
    ascending=True).dropna().unique(), name='defender_1')
years = pd.Series(data['year'].dropna().unique(), name='year')
defyear = pd.merge(years, defenders, how='cross').sort_values(by='year')
defyeartuple = [tuple(x) for x in defyear.to_numpy()]
defendersSeries = pd.Series(0, MultiIndex.from_tuples(
    defyeartuple, names=['year', 'defender_1']), name='defendersSeries')
defendersSeries = defendersSeries.combine(
    fightsPerYear, (lambda x1, x2: x2 if x2 > x1 else x1))

#print(defendersSeries)

fig, ax = plt.subplots()

x = np.arange(defenders.size)
width = 0.15


rects = []
for i in range(0, years.size):
    rects.append(
        ax.bar(x + width * i , defendersSeries[years[i]], width, label=years[i]))
    ax.bar_label(rects[i], padding=3)

ax.set_ylabel('Fights')
ax.set_xticks(x, defenders)
ax.legend()

fig.tight_layout()

plt.show()
