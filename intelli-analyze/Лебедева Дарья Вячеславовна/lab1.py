import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)
rating = data['Rating']

reviewDateGroup = data[['Review Date', 'Rating']]
reviewDateGroup = reviewDateGroup.groupby('Review Date')[['Review Date', 'Rating']]

plt.figure(figsize=(15, 7))
сolumn = reviewDateGroup.groups.keys()
array = np.empty(len(reviewDateGroup.groups.values()))

array[...] = rating.var()
plt.subplot(2, 2, 1)
plt.plot(сolumn, reviewDateGroup.var().fillna(0)['Rating'], label='Дисперсия Rating')
plt.plot(сolumn, array, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

array[...] = rating.mean()
plt.subplot(2, 2, 2)
plt.plot(сolumn, reviewDateGroup.mean()['Rating'], label='Среднее Rating')
plt.plot(сolumn, array, label='Общее среднее')
plt.title("Среднее")
plt.legend(fontsize=10)

array[...] = rating.median()
plt.subplot(2, 2, 3)
plt.plot(сolumn, reviewDateGroup.median()['Rating'], label='Медианное Rating')
plt.plot(сolumn, array, label='Общее Медианное')
plt.title("Медианное")
plt.legend(fontsize=10)

array[...] = rating.std()
plt.subplot(2, 2, 4)
plt.plot(сolumn, reviewDateGroup.std()['Rating'], label='СКО Rating')
plt.plot(сolumn, array, label='Общее СКО')
plt.title("СКО")
plt.legend(fontsize=10)

plt.show()

#---------------------------------------------------------------------------

cocoaColumn = data.sort_values(by='Cocoa Percent')['Cocoa Percent'].unique()
cocoaColumn = cocoaColumn.astype(float)
cocoaColumn = np.sort(cocoaColumn)
cocoaColumn = cocoaColumn.astype(str)
cocoaColumn = [i.replace('.0', '') for i in cocoaColumn]
cocoaGroup = data.groupby('Cocoa Percent')['Rating']

plt.figure(figsize=(15, 7))
thirdArray = np.empty(len(cocoaColumn))
thirdArray[...] = cocoaGroup.var().fillna(0)
plt.subplot(2, 1, 1)
plt.plot(cocoaColumn, thirdArray, label='Дисперсия')
thirdArray[...] = rating.var()
plt.plot(cocoaColumn, thirdArray, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

thirdArray[...] = cocoaGroup.max() - cocoaGroup.min()
plt.subplot(2, 1, 2)
plt.plot(cocoaColumn, thirdArray, label='Размах')
thirdArray[...] = rating.max() - rating.min()
plt.plot(cocoaColumn, thirdArray, label='Общий размах')
plt.title("Размах")
plt.legend(fontsize=10)

plt.show()