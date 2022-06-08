import pandas as pd
import matplotlib.pyplot as plt

#Завадская Вариант "С"

mainDF = pd.read_csv('./flavors_of_cacao.csv', header=0)
mainDF['Cocoa Percent'] = mainDF['Cocoa Percent'].replace('%', '', regex=True).astype('float64')

tempDF1 = mainDF.query('Rating > 3.1')
tempDF2 = mainDF.groupby('Company Location')
tempDF1 = tempDF1.groupby('Company Location')
tempDF = (tempDF1['Rating'].count() / tempDF2['Rating'].count()).dropna()

print('[1] Вероятность получения оценки выше 3.1')
print(tempDF)


bothAmericas = ['Bolivia', 'Brazil', 'Canada', 'Colombia', 'Ecuador', 'U.S.A.']
tempDF = mainDF.groupby('Company Location')
tempDF1 = mainDF.query('Rating > 3.1 and `Cocoa Percent` > 73')
tempDF1 = tempDF1.groupby('Company Location')
tempDF1 = tempDF1['Rating'].count() / tempDF['Rating'].count()
tempDF2 = mainDF.query('`Cocoa Percent` > 73')
tempDF2 = tempDF2.groupby('Company Location')
tempDF2 = tempDF2['Rating'].count() / tempDF['Rating'].count()
tempDF = tempDF1 / tempDF2
tempDF = tempDF[bothAmericas]
plt.figure(figsize=(16, 7))
plt.title('[2] Вероятность того, что новый сорт с содержанием какао выше 73% будет иметь оценку'
          ' выше 3.1 для стран северного полушария')
plt.bar(tempDF.index, tempDF.array)
plt.show()

tempDF = mainDF.query('`Review Date` > 2014')
medianValue = mainDF.query('`Review Date` > 2010')['Rating'].median()
tempDF = tempDF.query(f'Rating > {medianValue}')['Rating'].count() / tempDF['Rating'].count()
print('[3] Прогноз вероятности, что обзоры после 2014 года будут иметь оценку'
      ' выше медианной по всему периоду 2010 года')
print(tempDF)