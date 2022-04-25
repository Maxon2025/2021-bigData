import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
rating = data['Rating']
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)
cocoaColumn = data.sort_values(by='Cocoa Percent')['Cocoa Percent'].unique()

cocoaColumn = cocoaColumn.astype(float)
cocoaColumn = np.sort(cocoaColumn)
cocoaColumn = cocoaColumn.astype(str)
cocoaColumn = [i.replace('.0', '') for i in cocoaColumn]
cocoaGroup = data.groupby('Cocoa Percent')['Rating']

# Первый пункт

refGroup = data[['REF', 'Rating']]
i = 0
while i <= len(str(refGroup['REF'].max())):
    i += 1
    refGroup.loc[refGroup['REF'] > 9, 'REF'] //= 10
refGroup = refGroup.groupby("REF")[['REF', 'Rating']]

# Второй пункт

plt.figure(figsize=(15, 7))
сolumn = refGroup.groups.keys()
tempArray = np.empty(9)

tempArray[...] = rating.var()
plt.subplot(2, 2, 1)
plt.plot(сolumn, refGroup.var().fillna(0)['Rating'], label='Дисперсия Rating')
plt.plot(сolumn, tempArray, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

tempArray[...] = rating.mean()
plt.subplot(2, 2, 2)
plt.plot(сolumn, refGroup.mean()['Rating'], label='Среднее Rating')
plt.plot(сolumn, tempArray, label='Общее среднее')
plt.title("Среднее")
plt.legend(fontsize=10)

tempArray[...] = rating.median()
plt.subplot(2, 2, 3)
plt.plot(сolumn, refGroup.median()['Rating'], label='Медианное Rating')
plt.plot(сolumn, tempArray, label='Общее Медианное')
plt.title("Медианное")
plt.legend(fontsize=10)

tempArray[...] = rating.std()
plt.subplot(2, 2, 4)
plt.plot(сolumn, refGroup.std()['Rating'], label='СКО Rating')
plt.plot(сolumn, tempArray, label='Общее СКО')
plt.title("СКО")
plt.legend(fontsize=10)

plt.show()

# Третий пункт

plt.figure(figsize=(15, 7))
tempArray = np.empty(len(cocoaColumn))

tempArray[...] = cocoaGroup.var().fillna(0)
plt.subplot(2, 1, 1)
plt.plot(cocoaColumn, tempArray, label='Дисперсия')
tempArray[...] = rating.var()
plt.plot(cocoaColumn, tempArray, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

tempArray[...] = cocoaGroup.max() - cocoaGroup.min()
plt.subplot(2, 1, 2)
plt.plot(cocoaColumn, tempArray, label='Размах')
tempArray[...] = rating.max() - rating.min()
plt.plot(cocoaColumn, tempArray, label='Общий размах')
plt.title("Размах")
plt.legend(fontsize=10)

plt.show()
