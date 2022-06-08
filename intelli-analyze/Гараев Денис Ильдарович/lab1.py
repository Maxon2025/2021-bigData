from cProfile import label
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt

data = pd.read_csv(
    './flavors_of_cacao.csv')
ratingByDate = data.groupby(['Review Date'])['Rating']
dates = data['Review Date'].unique()
dates.sort()

fig, task21 = plt.subplots()
fig, task22 = plt.subplots()
fig, task23 = plt.subplots()

x = 0.25
width = 0.1
i = 0

task21.bar(x * i, ratingByDate.mean(), width, color='b',
           edgecolor='k', label='Среднее сгруппированного')
task21.bar(x * i + width, data['Rating'].mean(), width,
           color='c', edgecolor='k', label='Среднее общее')
i += 1

task21.bar(x * i, ratingByDate.median(), width,  color='g',
           edgecolor='k', label='Медианное сгруппированного')
task21.bar(x * i + width, data['Rating'].median(), width,
           color='y', edgecolor='k', label='Медианное общее')

width = 0.5
for j in range(0, len(dates)):
    task22.bar(
        x * j * 2, ratingByDate.get_group(dates[j]).var(), width, edgecolor='k', label=dates[j])
task22.bar(x * j * 2 + width * 2, data['Rating'].var(),
           width,  color='g', edgecolor='k', label='Дисперсия общее')

for j in range(0, len(dates)):
    task23.bar(
        x * j * 2, ratingByDate.get_group(dates[j]).std(), width, edgecolor='k', label=dates[j])
task23.bar(x * j * 2 + width * 2, data['Rating'].std(),
           width,  color='g', edgecolor='k', label='СКО общее')

task21.set_xticks([])
task22.set_xticks([])
task23.set_xticks([])
task21.legend()
task22.legend()
task23.legend()

fig, task3 = plt.subplots()

dataFloatPerc = data
dataFloatPerc['Cocoa Percent'] = dataFloatPerc['Cocoa Percent'].str.strip('%').astype('float')
ratingByPercent = dataFloatPerc[['Rating','Cocoa Percent']].dropna().groupby('Cocoa Percent')
percents = dataFloatPerc['Cocoa Percent'].unique()
percents.sort()

task3.plot(ratingByPercent.min(), label="Минимум")
task3.plot(ratingByPercent.max(), label="Максимум")
task3.plot(ratingByPercent.var(), label="Дисперсия")

task3.set_xlabel('Содержание какао')
task3.set_ylabel('Рейтинг')

task3.legend()

plt.show()
