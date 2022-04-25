import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('flavors_of_cacao.csv', header=0)
df = data.groupby("Broad Bean Origin")['Rating']
df2 = data.sort_values(by='Broad Bean Origin').groupby("Broad Bean Origin")

print(data.head())
print(df2.head())

meandf2 = df2['Rating'].mean().mean()
mediandf2 = df2['Rating'].median()
meanRating = data['Rating'].mean()
medianRating = data['Rating'].median()

#var = [meandf2, meanRating, mediandf2, medianRating]
#tit = ["mean of df2", "mean of all", "median of df2", "median of all"]
#print(meanRating)
#print(meandf2)
#print(medianRating)
#print(mediandf2)

plt.subplot(2, 2, 1)
plt.plot(df2['Rating'].mean())
#plt.axhline(df2['Rating'].mean().mean(), color='r')
plt.axhline(data['Rating'].mean(), color='r')
plt.gca().set_xticklabels(df2['Broad Bean Origin'].min(), rotation=40, horizontalalignment='center', fontsize=7)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=50, hspace=None)
plt.xticks(np.arange(0, len(df2['Broad Bean Origin'].max()), 5))
plt.title("Среднее значение", fontsize=12)

plt.subplot(2, 2, 3)
plt.plot(df2['Rating'].median())
plt.axhline(data['Rating'].median(), color='g')
plt.axhline(df2['Rating'].median().median(), color='r')
plt.gca().set_xticklabels(df2['Broad Bean Origin'].max(), rotation=40, horizontalalignment='center', fontsize=7)
plt.xticks(np.arange(0, len(df2['Broad Bean Origin'].max()), 5))
plt.title("Медианное значение", fontsize=12)

plt.subplot(2, 2, 2)
plt.plot(df2['Rating'].var())
plt.axhline(data['Rating'].var(), color='r')
plt.gca().set_xticklabels(df2['Broad Bean Origin'].max(), rotation=40, horizontalalignment='center', fontsize=7)
plt.xticks(np.arange(0, len(df2['Broad Bean Origin'].max()), 5))
plt.title("Дисперсия", fontsize=12)

plt.subplot(2, 2, 4)
plt.plot(df2['Rating'].std())
plt.axhline(data['Rating'].std(), color='r')
plt.gca().set_xticklabels(df2['Broad Bean Origin'].max(), rotation=40, horizontalalignment='center', fontsize=7)
plt.xticks(np.arange(0, len(df2['Broad Bean Origin'].max()), 5))
plt.title("Средне-квадратичное отклонение", fontsize=12)
plt.subplots_adjust(top=0.9, bottom=0.18, left=0.06, right=0.95, hspace=0.7, wspace=0.2)
plt.show()

df3 = data.sort_values(by='Cocoa Percent').groupby("Cocoa Percent")
plt.subplot(1, 1, 1)
plt.plot(df3['Rating'].mean(), label='среднее содержание какао')
plt.plot(df3['Rating'].var(), color='r', label='дисперсия')
plt.plot(df3['Rating'].max(), color='g', label='максимальное')
plt.plot(df3['Rating'].min(), color='y', label='минимальное')
plt.gca().set_xticklabels(df3['Cocoa Percent'].max(), rotation=90, horizontalalignment='center')
plt.xticks(np.arange(0, len(df3['Cocoa Percent'].max()), 2))
plt.title("Изменение значений рейтинга для различного содержания какао в процентах", fontsize=14)
plt.legend(loc='upper left')
plt.show()


