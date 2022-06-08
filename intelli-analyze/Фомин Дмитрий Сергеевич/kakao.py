import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np


data = pd.read_csv('flavors_of_cacao.csv',header=0)
byYear = data.sort_values(by='Review Date')[['Review Date','Rating']].groupby("Review Date")

fig, axs = plt.subplots(2)

axs[0].plot(byYear.mean(), color = 'y', label = 'Среднее(груп)')

axs[0].axhline(data['Rating'].mean(), color = 'b', label = 'Среднее(общ)')


axs[0].plot(byYear['Rating'].median(), color = 'k', label = 'Медианное (груп)')
axs[0].axhline(data['Rating'].median(), color = 'k',linestyle = '--' ,label = 'Медианное (общ)')


axs[1].plot(byYear['Rating'].var(), color = 'r', label = 'Дисперсия(груп)')
axs[1].axhline(data['Rating'].var(), color = 'b', linestyle = '--', label = 'Дисперсия(общ)')

axs[1].plot(byYear['Rating'].std(), color = 'g', label = 'СКО(груп)')
axs[1].axhline(data['Rating'].std(), color = 'k', linestyle = '--', label = 'СКО(общ)')

print("Дисперсия2 = ", data['Rating'].var())
print("СКО2 = ", data['Rating'].std())

axs[0].set_xlabel('Дата оценки')
axs[0].set_ylabel('Рейтинг')
axs[1].set_xlabel('Дата оценки')
axs[1].set_ylabel('Рейтинг')

axs[0].legend()
axs[1].legend()
plt.show()

r = data['Rating'].dropna()
cp = data['Cocoa Percent'].dropna().apply(lambda x: float(x.strip('%')))

perc = pd.concat([r,cp],axis=1).groupby('Cocoa Percent')
plt.plot(perc.mean(), color = 'b', label = 'Рейтинг')
plt.plot(perc['Rating'].min(), color = 'g', label = 'Мин')
plt.plot(perc['Rating'].max(), color = 'r', label = 'Макс')
plt.plot(perc['Rating'].var(), color = 'k', label = 'Дисперсия')
plt.xlabel('Содержание какао (%)')
plt.ylabel('Рейтинг')
plt.legend()
plt.show()
 
