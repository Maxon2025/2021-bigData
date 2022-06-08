import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)


all_bbo = data['Broad Bean Origin'].dropna()
all_rating = data['Rating'].dropna()
all_percent = data['Cocoa Percent'].dropna().apply(
    lambda x: float(x.strip('%')))
dt1 = pd.concat([all_bbo, all_rating], axis=1).groupby('Broad Bean Origin')
dt3 = pd.concat([all_percent, all_rating], axis=1).groupby('Cocoa Percent')

plt.figure("1,2", figsize=[16, 9])
plt.xlabel('Происхождение')
plt.ylabel('Рейтинг')
plt.plot(dt1.mean(), color='b')
plt.axhline(all_rating.mean(), color='darkblue')

plt.plot(dt1['Rating'].median(), color='r', linestyle='-.')
plt.axhline(all_rating.median(), color='firebrick')
plt.plot(dt1['Rating'].var(), color='g')
plt.axhline(all_rating.var(), color='darkgreen')
plt.plot(dt1['Rating'].std(), color='y')
plt.axhline(all_rating.std(), color='gold')
plt.subplots_adjust(top=0.98, bottom=0.30, left=0.05, right=0.98)
plt.xticks(rotation='vertical')
plt.legend(['Среднее', 'Среднее общ.', 'Медианное', 'Медианное общ.',
            'Дисперсия', 'Дисперсия общ.', 'СКО', 'СКО общ.'])


plt.figure("3", figsize=[16, 9])
plt.xlabel('Процент')
plt.ylabel('Рейтинг')
plt.plot(dt3.mean(), color='g')
plt.plot(dt3.var(), color='y')
plt.plot(dt3.max(), color='b', linestyle='--')
plt.plot(dt3.min(), color='gold', linestyle='-.')
plt.legend(['Среднее', 'Дисперсия', 'Max', 'Min'])
plt.show()
