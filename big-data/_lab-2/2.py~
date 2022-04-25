import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('GoT/battles.csv', header=0)

print(data.head())

#data.groupby('year')['name'].nunique().plot(kind='bar')

#plt.show()

y = data.groupby('year')['name'].nunique()
x = data['year'].unique()

k = []

print(len(x))
for i in range(1, len(x)):
    k.append((y.iat[i]-y.iat[i-1])/(x[i]-x[i-1]))

k_m = np.mean(k)

plt.plot(x, y) #comment for test
plt.show()
