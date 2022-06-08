import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def getData(data, cond, selecter='Rating', group='Company Location'):
    df = data.query(cond)
    if group is not None:
        data = data.groupby(group)
        df = df.groupby(group)
    return df[selecter].count() / data[selecter].count()


data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
south = ['Australia', 'Argentina', 'Bolivia', 'Peru', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Madagascar',
         'New Zealand', 'Sao Tome', 'Fiji']

# Задание 1.
p1 = getData(data, 'Rating > 3.1').dropna()
plt.subplots(figsize=(15, 9))
ax = sns.barplot(y=p1.index, x=p1.array, palette='deep')
ax.set_title('Вероятность получения оценки выше 3.1')
ax.set_yticklabels(labels=p1.index, rotation=0)
plt.show()

# Задание 2.
p2 = getData(data, 'Rating > 3.7 and `Cocoa Percent` > 73') / getData(data, '`Cocoa Percent` > 73')
p2 = p2[south]
plt.subplots(figsize=(12, 7))
ax = sns.barplot(y=p2.index, x=p2.array, palette='deep')
ax.set_title('Условная вероятность получения оценки выше 3.1 при содержании какао выше 73%')
ax.set_yticklabels(labels=p2.index, rotation=0)
plt.show()

# Задание 3.
data2014 = data.query('`Review Date` > 2014')
med = data.query('`Review Date` > 2010')['Rating'].median()
p3 = getData(data2014, f'Rating > {med}', group=None)
print('Вероятность того, что все обзоры какао после 2014 года будут '
      'иметь оценку выше медианной по всему периоду после 2010: ', p3)
