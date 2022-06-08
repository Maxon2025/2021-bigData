import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def lowNums(x):
  while len(str(x['REF'].max())) >= 2:
        x.loc[x['REF'] > 9, 'REF'] //= 10

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
rating = data['Rating']
ref = data[['REF', 'Rating']]
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
cocoa = data[['Cocoa Percent', 'Rating']].sort_values(by="Cocoa Percent").groupby('Cocoa Percent')


lowNums(ref)
ref = ref.groupby(by="REF")[['REF', 'Rating']]

plt.figure(1, figsize=[12,9])
plt.subplot(2,2,1)

plt.plot(ref.mean()['Rating'], label='Усредненный график')
plt.axhline(rating.mean(), linestyle='--',color='r', label='Общее среднее')
plt.xlabel("REF")
plt.ylabel("Reting")
plt.legend()

plt.subplot(2,2,2)
plt.plot(ref.var()['Rating'], label='Усредненный график')
plt.axhline(rating.var(), linestyle='--',color='r', label='Общее среднее')
plt.xlabel("REF")
plt.ylabel("Reting")
plt.legend()

plt.subplot(2,2,3)
plt.plot(ref.std()['Rating'], label='Усредненный график')
plt.axhline(rating.std(), linestyle='--',color='r', label='Общее среднее')
plt.xlabel("REF")
plt.ylabel("Reting")
plt.legend()

plt.subplots_adjust(bottom=0.3)
plt.legend()

plt.show()

plt.figure(2, figsize=[12, 5])

plt.plot(cocoa.mean(), color='g')
plt.plot(cocoa['Rating'].max(), color='b')
plt.plot(cocoa['Rating'].min(), color='r')
plt.plot(cocoa['Rating'].var(), color='black')

plt.legend(['Средний рейтинг', 'Максимальный', 'Минимальный', 'Дисперсия'])
plt.show()
