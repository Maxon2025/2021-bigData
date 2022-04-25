import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../_lab-2/GoT/battles.csv', header=0)

df1 = pd.concat([data[['year', 'attacker_king']], data[['year', 'defender_king']]], axis=0, ignore_index=True)
df1['king'] = np.where(df1['attacker_king'].isna(), df1['defender_king'], df1['attacker_king'])
df1 = df1.groupby(['king', 'year'])['king'].count()

datafr = pd.DataFrame(df1)
datafr.columns = ['count']
datafr.to_csv('result', sep=',')

dt = pd.read_csv('result', header=0, sep=',', na_filter=True)
print(dt)

ox_year = dt['year']
oy_king = dt['king']
oz_value = dt['count']*6

colors = np.random.uniform(15, 80, len(ox_year))

fig, ax = plt.subplots()
ax.scatter(ox_year, oy_king, s=oz_value, c=colors, vmin=0, vmax=200)

for x1, y1, s1 in zip(ox_year, oy_king, oz_value):
    label = s1/6
    plt.annotate(label,
                 (x1, y1),
                 textcoords="offset points",
                 xytext=(0, 6),
                 ha='center')

ax.set(xlim=(297, 301), xticks=np.arange(298, 301))
plt.show()
