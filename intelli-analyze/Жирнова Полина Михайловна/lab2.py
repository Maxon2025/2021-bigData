import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r'flavors_of_cacao.csv', header=0)
df=data.groupby(by=['Company Location'])['Company Location'].unique()

#Посчитать априорные вероятности для каждой страны происхождения (Company Location) получения оценки выше 3.1

zadanie1 = pd.DataFrame(columns=['Country', 'Probability'])

i=0
j=0
kolvo=0
kolvo31=0

while i < len(df.index):
    for j in data['Company Location'].index:
        if df[i]==data['Company Location'][j]:
            kolvo+=1
            if data.at[j, 'Rating'] > 3.1:
                kolvo31+=1
        j+=1
    new_row = {'Country': df[i], 'Probability': kolvo31/kolvo}
    zadanie1 = zadanie1.append(new_row, ignore_index=True)
    kolvo=0
    kolvo31=0
    i+=1
    
print('1. Априорные вероятности для каждой страны происхождения получения оценки выше 3.1')
print(zadanie1)

#Используя их, посчитать вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent) будет имет оценку выше 3.1 для стран: b) северного полушария

north = ['Austria', 'Belgium', 'Canada', 'Czech Republic', 'Denmark', 'Domincan Republic',
         'Finland', 'France', 'Germany', 'Sweden', 'Switzerland','U.K.', 'U.S.A.']

data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float64')
zadanie2 = pd.DataFrame(columns=['Countries of the northern hemisphere', 'Probability','Cocoa Percent'])

i=0
j=0

while i < len(north):
    for j in data['Company Location'].index:
        if data['Cocoa Percent'][j]>73.0 and north[i]==data['Company Location'][j]:
         new_row = {'Countries of the northern hemisphere': north[i], 'Probability': zadanie1['Probability'][i],'Cocoa Percent': data['Cocoa Percent'][j]}
         j+=1
    zadanie2 = zadanie2.append(new_row, ignore_index=True)
    i+=1
    
zadanie2=zadanie2.drop_duplicates()

plt.figure(num="2 задание",figsize=(20, 8))
plt.title('Вероятность того, что новый сорт с содержанием какао выше 73% будет иметь оценку выше 3.1 для b) стран северного полушария')
plt.bar(zadanie2['Countries of the northern hemisphere'], zadanie2['Probability'])
plt.gca().set_xticklabels(zadanie2['Countries of the northern hemisphere'], rotation=90,horizontalalignment='center', fontsize=8)
plt.show()

#Сделать прогноз, какова вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной по всему периоду после 2010 года.

data['Review Date']=data['Review Date'].astype('float64')

median = data[data['Review Date'] > 2010]['Rating'].median()
after = data[data['Review Date'] > 2014]

rez1 = after[after['Rating'] > median]['Rating'].count() 
rez2 = after['Rating'].count()

rezult=rez1/rez2

print('3. Прогноз: какова вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной по всему периоду после 2010 года.')
print(rezult)
