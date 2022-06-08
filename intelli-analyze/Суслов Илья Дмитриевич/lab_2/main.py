import numpy as np
import pandas as pd
from utils.plot import plot_bars

df = pd.read_csv('data/flavors_of_cacao.csv', delimiter=',')
print('\nВыборка для наглядности',df.head(), sep='\n')
print('\nКоличество NaN по столбцам',df.isnull().sum(), sep='\n')
xlabel = 'Страны'
ylabel = 'Вероятности'

#Задание 1. Посчитать априорные вероятности для каждой страны происхождения (Company Locaction) получения оценки выше 3.1
print('\nВыведем список стран, городов и провинций происхождения (Company Location)',df['Company Location'].unique(), sep='\n')
#Посчитаем априорные вероятности по формуле частотной вероятности P(A)=n/N, где N – количество наблюдений (total), а n – количество наступлений события A
def grouped_probability(col, n_flt, grp, **kwargs):
  n = df[n_flt].groupby(grp).count()[col]
  if type(kwargs.get('t_flt')) is pd.Series:
    total = df[kwargs['t_flt']].groupby(grp).count()[col]
  else:
    total = df.groupby(grp).count()[col]
  return (n / total).dropna()
def simple_probability(col, n_flt, **kwargs):
  n = df[n_flt].count()[col] 
  if type(kwargs.get('t_flt')) is pd.Series:
    total = df[kwargs['t_flt']].count()[col]
  else:
    total = df.count()[col]
  return n / total
def probability(col, n_flt, **kwargs):
  if (kwargs.get('grp')):
    return grouped_probability(col, n_flt, kwargs.pop('grp'), **kwargs)
  else:
    return simple_probability(col, n_flt, **kwargs)
#Рассчитаем априорные вероятности получения оценки выше 3.1 для всех стран
n_flt = df['Rating'] > 3.1
pa = probability('Rating', n_flt, grp='Company Location')
title = 'Априорные вероятности получения оценки выше 3.1 для всех стран'
plot_bars(np.array_split(pa, 3), title, xlabel, ylabel)

#Задание 2. Используя их, посчитать вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent) будет иметь оценку выше 3.1 для стран Европы плюс Африки
europe_and_africa = ['Amsterdam', 'Austria', 'Belgium', 'Denmark', 'France', 'Germany', 'Hungary', 'Iceland', 'Italy', 'Lithuania', 'Madagascar', 'Poland', 'Sao Tome', 'Scotland', 'Spain', 'Switzerland', 'U.K.']
# Посчитаем вероятности по формуле Байеса P(A|B) = P(B|A) * P(A)/P(B)
def grouped_bayes(a, b, a_flt, b_flt, grp):
  pa = probability(a, a_flt, grp=grp)
  pb = probability(b, b_flt, grp=grp)
  pba = probability(a, a_flt & b_flt, t_flt=a_flt, grp=grp)
  pab = pba * pa / pb
  return pab.dropna()
def simple_bayes(a, b, a_flt, b_flt):
  pa = probability(a, a_flt)
  pb = probability(b, b_flt)
  pba = probability(a, a_flt & b_flt, t_flt=a_flt)
  pab = pba * pa / pb
  return pab
def bayes(a, b, a_flt, b_flt, **kwargs):
  if kwargs.get('grp'):
    return grouped_bayes(a, b, a_flt, b_flt, kwargs['grp'])
  else:
    return simple_bayes(a, b, a_flt, b_flt)
a_flt = df['Rating'] > 3.1
b_flt = df['Cocoa Percent'].str[:-1].astype(float) > 73
pab = bayes('Rating', 'Cocoa Percent', a_flt, b_flt, grp='Company Location')
ixs = pab.index.intersection(europe_and_africa)
title = 'Вероятности, что новый сорт какао с содержанием более 73% какао-бобов\nбудет иметь оценку выше 3.1 баллов, для стран Европы и Африки'
plot_bars(pab.loc[ixs], title, xlabel, ylabel)

print('\nЗадание 3. Сделать прогноз, какова вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной по всему периоду после 2010 года')
#Рассчитаем медианную оценку для обзоров какао периода после 2010 года
median = df[df['Review Date'] > 2010]['Rating'].median()
print(f'\nМедианная оценка для обзоров какао периода после 2010 года составляет {round(median, 2)} баллов')
#Сделаем прогноз, рассчитав вероятности по формуле Байеса
a_flt = df['Rating'] > median
b_flt = df['Review Date'] > 2014
pab = bayes('Rating', 'Review Date', a_flt, b_flt)
print(f'\nВероятность, что обзоры какао после 2014 года будут иметь оценку выше медианной по периоду после 2010 года, составляет {round(pab, 2)}')