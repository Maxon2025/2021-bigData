import pandas as pd
import numpy as np
from utils.plot import plot_bars

df = pd.read_csv('data/flavors_of_cacao.csv', delimiter=',')
print('\nВыборка для наглядности',df.head(), sep='\n')
print('\nКоличество NaN по столбцам',df.isnull().sum(), sep='\n')

#Задание 1. Сгруппировать оценки по годам проведения дегустации (Review Date)
group_filter = lambda x: len(x) > 1
review_grouped_rating = df.groupby('Review Date').filter(group_filter).groupby('Review Date')['Rating']
print('\nЗадание 1. Сгруппировать оценки по годам проведения дегустации (Review Date)', review_grouped_rating.describe(), sep = '\n')

#Задание 2. Оценить: дисперсию, среднее, медианное, и СКО поля "Rating" для каждого поля отдельно. Сравнить с аналогичными показателями общего поля "Rating" (по всему списку).
measures = ['var', 'std', 'mean', 'median']
review_basis_measure = review_grouped_rating.agg(measures)
print('\nЗадание 2. Оценить: дисперсию, среднее, медианное, и СКО поля "Rating" для каждого поля отдельно. Сравнить с аналогичными показателями общего поля "Rating" (по всему списку).','\nРассчитаем показатели рейтинга (Rating)',review_basis_measure.round(2).head(), sep='\n')
rating_measure = df["Rating"].agg(measures)
print('\nРассчитаем общие дисперсию (var), среднее (mean), медиану (median) и СКО (std) рейтинга (Rating)',rating_measure.round(2), sep= '\n')
review_basis_delta = review_basis_measure - rating_measure
review_basis_delta.columns = ['delta var', 'delta std', 'delta mean', 'delta median']
print('\nСравним показатели сгруппированного рейтинга (Rating) с общими показателями рейтинга', review_basis_delta.round(2).head(), sep='\n')

#Задание 3. Оценить величины дисперсии и размаха (max-min) рейтинга (Rating) для различного содержания какао в процентах (Cocoa Percent)
cocoa_grouped_rating = df.groupby("Cocoa Percent").filter(group_filter).groupby("Cocoa Percent")["Rating"]
perc_sort = lambda x: x.str.slice(stop=-1).astype(float)
#Рассчитаем дисперсию рейтинга (Rating) для различного содержания какао в процентах (Cocoa Percent)
cocoa_basis_var = cocoa_grouped_rating.var().sort_index(key = perc_sort)
title = 'Дисперсия рейтинга для различного содержания какао в процентах\n'
xlabel = 'Содержание какао в процентах'
ylabel = 'Дисперсия'
plot_bars(np.array_split(cocoa_basis_var.round(2), 2), title, xlabel, ylabel)
#Рассчитаем размах рейтинга (Rating) для различного содержания какао в процентах (Cocoa Percent)
cocoa_basis_range = (cocoa_grouped_rating.max() - cocoa_grouped_rating.min()).sort_index(key = perc_sort)
title = 'Размах рейтинга для различного содержания какао в процентах\n'
xlabel = 'Содержание какао в процентах'
ylabel = 'Размах'
plot_bars(np.array_split(cocoa_basis_range.round(2), 2), title, xlabel, ylabel)
