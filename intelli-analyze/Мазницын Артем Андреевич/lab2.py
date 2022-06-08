import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
north = ['Amsterdam', 'Belgium', 'Brazil', 'Canada', 'Colombia', 'Ecuador', 'France', 'Israel', 'Italy',
                     'Lithuania', 'Sao Tome', 'Scotland', 'Switzerland', 'U.K.', 'U.S.A.']
def getData(data, cond, selecter='Rating', group='Company Location'):
    df = data.query(cond)
    if group is not None:
        data = data.groupby(group)
        df = df.groupby(group)
    return df[selecter].count() / data[selecter].count()

datR = getData(data, 'Rating > 3.1').dropna()
plt.subplots(figsize=(14, 9))
ax = sns.barplot(y=datR.index, x=datR.array, palette='deep')
ax.set_title('Вероятность получения оценки выше 3.1')
ax.set_yticklabels(labels=datR.index, rotation=0)
plt.show()
datP = getData(data, 'Rating > 3.7 and `Cocoa Percent` > 73') / getData(data, '`Cocoa Percent` > 73')
datP = datP[north]
plt.subplots(figsize=(10, 6))
ax = sns.barplot(y=datP.index, x=datP.array, palette='deep')
ax.set_title('Условная вероятность получения оценки выше 3.1 при содержании какао выше 73% в странах северного полушария')
ax.set_yticklabels(labels=datP.index, rotation=0)
plt.show()

datY = data.query('`Review Date` > 2014')
datM = data.query('`Review Date` > 2010')['Rating'].median()
datF = getData(datY, f'Rating > {datM}', group=None)
print('Вероятность того, что все обзоры какао после 2014 года будут '
      'иметь оценку выше медианной по всему периоду после 2010: ', datF)
