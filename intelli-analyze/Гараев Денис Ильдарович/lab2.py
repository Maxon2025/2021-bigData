from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    './flavors_of_cacao.csv')

dataFloatPerc = data
dataFloatPerc['Cocoa Percent'] = dataFloatPerc['Cocoa Percent'].str.strip('%').astype('float')

task1 = dataFloatPerc.query('Rating > 3.1').groupby('Company Location')['Rating'].count() / dataFloatPerc.groupby('Company Location')['Rating'].count()
task1 = task1.fillna(0)

EuropeAfrica = ['Amsterdam', 'Austria', 'Belgium', 'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Ghana', 'Hungary', 'Iceland',
                'Ireland', 'Italy', 'Lithuania', 'Poland', 'Portugal', 'Scotland', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'U.K.', 'Wales']
EuropeAfricaSeries = pd.Series(0, index=EuropeAfrica)
task2 = dataFloatPerc.query('Rating > 3.1 and `Cocoa Percent` > 73').groupby('Company Location')['Rating'].count() / dataFloatPerc.query('`Cocoa Percent` > 73').groupby('Company Location')['Rating'].count()
task2 = task2.fillna(0)
task2 = task2.combine(EuropeAfricaSeries, max, fill_value=0)
task2 = task2[EuropeAfrica]

data2014 = data.query('`Review Date` > 2014')
med = data.query('`Review Date` > 2010')['Rating'].median()
task3 = data2014.query(f'Rating > {med}').groupby('Company Location')['Rating'].count() / data2014.groupby('Company Location')['Rating'].count()
task3 = task3.fillna(0)

fig, taskPlot = plt.subplots(2)
taskPlot[0].plot(task1, label='Оценка 3.1 для каждой страны')
taskPlot[1].plot(task2, label='Оценка 3.1 и содержание какао > 73% для стран Европы и Африки')
taskPlot[0].legend()
taskPlot[1].legend()

print('Вероятность того, что все обзоры какао после 2014 года будут '
      'иметь оценку выше медианной по всему периоду после 2010: ', task3)
plt.show()
