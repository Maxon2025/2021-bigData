import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

#по первой цифре поля REF

data.loc[(data.REF >=1), 'REF'] = data['REF'].astype(str).str[:1]

data1 = data.sort_values(by='REF').groupby("REF")

print(data.REF)

#1 график

plt.figure(num="1 пункт")
plt.plot(data1['Rating'].mean())
plt.axhline(data['Rating'].mean(), color='r')
plt.show()

#2 график

data2 = data.sort_values(by='REF').groupby("REF")

plt.figure(num="2 пункт",figsize=(10,10))

plt.subplot(2, 2, 1)
plt.plot(data2['Rating'].var())
plt.axhline(data['Rating'].var(), color='r')
plt.gca().set_xticklabels(data2['REF'].max(), rotation=90)
plt.title("Дисперсия")

plt.subplot(2, 2, 2)
plt.plot(data2['Rating'].mean())
plt.axhline(data['Rating'].mean(), color='r')
plt.gca().set_xticklabels(data2['REF'].min(), rotation=90)
plt.title("Среднее")

plt.subplot(2, 2, 3)
plt.plot(data2['Rating'].median())
plt.axhline(data['Rating'].median(), color='g')
plt.axhline(data2['REF'].median().median(), color='r')
plt.gca().set_xticklabels(data2['REF'].max(), rotation=90)
plt.title("Медианное")

plt.subplot(2, 2, 4)
plt.plot(data2['Rating'].std())
plt.axhline(data['Rating'].std(), color='r')
plt.gca().set_xticklabels(data2['REF'].max(), rotation=90)
plt.title("СКО")
plt.show()

#3 график

data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)

datasort = data.sort_values(by='Cocoa Percent')['Cocoa Percent'].unique().astype(float)

datasort = np.sort(datasort)
datasort = datasort.astype(str)
datasort= [i.replace('.0', '%') for i in datasort]
datasort= [i.replace('.5', '.5%') for i in datasort]
data3 = data.groupby('Cocoa Percent')

plt.figure(num="3 пункт",figsize=(20,20))
plt.plot(data3['Rating'].var())
plt.axhline(data['Rating'].var(), color='r')
plt.gca().set_xticklabels(datasort, rotation=90)
plt.title("Дисперсия")
plt.show()

plt.figure(num="3 пункт (Размах)",figsize=(20,20))
plt.plot(data3['Rating'].max()-data3['Rating'].min())
plt.axhline(data['Rating'].max()-data['Rating'].min(), color='r')
plt.gca().set_xticklabels(datasort, rotation=90)
plt.title("Размах")
plt.show()
