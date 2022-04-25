import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../_lab-2/GoT/battles.csv', usecols=['attacker_king', 'year'])

print("\nИсходные данные:\n")
print(data)

length = []

for year in data['year']:
    namelength = 0 
    names = data.loc[data['year'] == year]['attacker_king'].dropna()
    for name in names:
        namelength += len(name)
    length.append(namelength)

data['year2']=data['year']
data['name_length']=length


fig, ax = plt.subplots()
index = data['year2']
values = data['name_length']
plt.bar(index,values)
plt.title('Абсолютные значения')
plt.xlabel("Год")
plt.ylabel("Сумма длин имен")
ax.set(xlim=(297, 301), xticks=np.arange(298, 301))

length2=[]
length3 = list(set(length))
sum=np.sum(length3)

for year in data['year']:
    namelength = 0 
    names = data.loc[data['year'] == year]['attacker_king'].dropna()
    for name in names:
        namelength += (len(name)*100)
        size=namelength/sum
    length2.append(size)

data['%']=length2

fig, ax = plt.subplots()
index = data['year2']
values = data['%']
plt.bar(index,values)
plt.title('Нормированные значения')
plt.xlabel("Год")
plt.ylabel("Сумма длин имен")
ax.set(xlim=(297, 301), xticks=np.arange(298, 301))

print("\nТаблица с данными для графика:\n")
print(data)

print("\nГрафик:\n")

plt.show()
