import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float64')


def possibilities(info, condition):
    dataframe = info.query(condition)
    info = info.groupby('Company Location')
    dataframe = dataframe.groupby('Company Location')
    return dataframe['Rating'].count() / info['Rating'].count()


# Посчитать априорные вероятности для каждой страны происхождения (Company Location) получения оценки выше 3.1

temp = possibilities(data, 'Rating > 3.1').dropna()
print('----- №1 Вероятность получения оценки выше 3.1 -----')
print(temp)

# Используя их, посчитать вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent)
# будет иметь оценку выше 3.1 для стран b) северного полушария

northernCountries = ['Amsterdam', 'Belgium', 'Brazil', 'Canada', 'Colombia', 'Ecuador', 'France', 'Israel', 'Italy',
                     'Lithuania', 'Sao Tome', 'Scotland', 'Switzerland', 'U.K.', 'U.S.A.']
temp = possibilities(data, 'Rating > 3.1 and `Cocoa Percent` > 73') / possibilities(data, '`Cocoa Percent` > 73')
temp = temp[northernCountries]
plt.figure(figsize=(16, 7))
plt.title('№2 Вероятность того, что новый сорт с содержанием какао выше 73% будет иметь оценку'
          ' выше 3.1 для стран северного полушария')
plt.bar(temp.index, temp.array)
plt.show()

# Сделать прогноз, какова вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной
# по всему периоду после 2010 года.

df = data.query('`Review Date` > 2014')
medianValue = data.query('`Review Date` > 2010')['Rating'].median()
temp = df.query(f'Rating > {medianValue}')['Rating'].count() / df['Rating'].count()
print('----- №3 Прогноз вероятности, что обзоры после 2014 года будут иметь оценку'
      ' выше медианной по всему периоду 2010 года -----')
print(temp)
