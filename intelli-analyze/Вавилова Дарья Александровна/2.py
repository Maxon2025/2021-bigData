import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('flavors_of_cacao.csv', header=0)
df = data.groupby(by=['Company Location'])['Company Location'].unique()
print(df)
print()

south = ['Australia', 'Argentina', 'Bolivia', 'Peru', 'Brazil', 'Chile', 'Colombia',
         'Ecuador', 'Madagascar', 'New Zealand', 'Sao Tome', 'Fiji']

# задание 1. априорные вероятности рейтинга > 3.7 для всех стран
s = 0
var = 0
pa = pd.DataFrame(columns=['Country', 'Probability', 'All records'])
for i in df.index:
    for n in data['Company Location'].index:
        if data.at[n, 'Company Location'] == df.at[i]:
            s += 1
            if data.at[n, 'Rating'] > 3.7:
                var += 1
    new_row = {'Country': df.at[i], 'Probability': var/s, 'All records': s}
    pa = pa.append(new_row, ignore_index=True)
    s = 0
    var = 0

print()
print('общая вероятность по всем странам, что рейтинг > 3,7')
print(pa)

# задание 2. посчитать вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent)
# будет имет оценку выше 3.7 для стран южного полушария

pa2 = pd.DataFrame(columns=['Country', 'Probability', 'All records'])
for i in south:
    for n in data['Company Location'].index:
        if data.at[n, 'Company Location'] == i:
            s += 1
            if data.at[n, 'Rating'] > 3.2:
                var += 1
    new_row = {'Country': i, 'Probability': var/s, 'All records': s}
    pa2 = pa2.append(new_row, ignore_index=True)
    s = 0
    var = 0
print('вероятность рейтинга > 3.7 для южных стран')
print(pa2)

pb2 = pd.DataFrame(columns=['Country', 'Probability', 'All records'])
for i in south:
    for n in data['Company Location'].index:
        if data.at[n, 'Company Location'] == i:
            s += 1
            if float(data.at[n, 'Cocoa Percent'].strip('%')) > 73.:
                var += 1
    new_row = {'Country': i, 'Probability': var/s, 'All records': s}
    pb2 = pb2.append(new_row, ignore_index=True)
    s = 0
    var = 0
print('вероятность процента какао > 73 для южных стран')
print(pb2)

pba2 = pd.DataFrame(columns=['Country', 'Probability', 'All records'])
for i in south:
    for n in data['Company Location'].index:
        if data.at[n, 'Company Location'] == i:
            s += 1
            if (float(data.at[n, 'Cocoa Percent'].strip('%')) > 73.) & (data.at[n, 'Rating'] > 3.2):
                var += 1
    new_row = {'Country': i, 'Probability': var/s, 'All records': s}
    pba2 = pba2.append(new_row, ignore_index=True)
    s = 0
    var = 0
print('вероятность рейтинга > 3.7 и процента какао > 73 для южных стран')
print(pba2)

n = 0
PAB2 = pd.DataFrame(columns=['Country', 'Probability'])
for i in south:
    new_row = {'Country': i, 'Probability': pa2.loc[n, 'Probability']*pba2.loc[n, 'Probability']/pb2.loc[n, 'Probability']}
    PAB2 = PAB2.append(new_row, ignore_index=True)
    n += 1

print('вероятность что новый сорт какао с содержанием выше 73% (Cocoa Percent) '
      'будет имет оценку выше 3.7 для каждой страны южного полушария')
print(PAB2)

n = data[(data['Rating'] > 3.7) & (data['Company Location'].isin(south))].count()['Rating']
m = data[data['Company Location'].isin(south)].count()['Rating']
paa = n / m

n = data[(data['Cocoa Percent'].str.strip('%').astype('float') > 73) & (data['Company Location'].isin(south))].count()['Rating']
m = data[data['Company Location'].isin(south)].count()['Rating']
pbb = n / m

n = data[(data['Rating'] > 3.7) & (data['Cocoa Percent'].str.strip('%').astype('float') > 73) & (data['Company Location'].isin(south))].count()['Rating']
m = data[data['Company Location'].isin(south)].count()['Rating']
pbaa = n / m

PAB22 = paa*pbaa/pbb
print()
print('вероятность что новый сорт какао с содержанием выше 73% (Cocoa Percent) '
      'будет имет оценку выше 3.7 для всех стран южного полушария')
print(PAB22)

# задание 3. Сделать прогноз, какова вероятность того, что обзоры какао после 2014 года будут иметь
# оценку выше медианной по всему периоду после 2010 года.

median = data[data['Review Date'] > 2010]['Rating'].median()

n = data[data['Rating'] > median].count()['Rating']
m = data['Rating'].count()
pa3 = n / m

n = data[data['Review Date'] > 2014].count()['Review Date']
m = data['Review Date'].count()
pb3 = n / m

n = data[(data['Rating'] > median) & (data['Review Date'] > 2014)].count()['Rating']
m = data['Review Date'].count()
pba3 = n / m

PAB3 = pa3*pba3/pb3
print()
print('Вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной по всему периоду'
      ' после 2010 года.')
print(PAB3)
