import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flavors_of_cacao.csv")
df = df.dropna()
df['Cocoa Percent'] = df['Cocoa Percent'].dropna().str.strip('%').astype(float) / 100
print(df)
print(df.info())

print('Посчитать априорные вероятности для каждой страны происхождения (Company Location) получения оценки выше 3.1;')
df['Rating>3.1'] = df['Rating'] > 3.1
print(df.groupby('Company Location')['Rating>3.1'].mean())
print('--------------------------------------------------')

print('Используя их, посчитать вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent)'
      'будет имет оценку выше 3.1 для стран:'
      'a) Европы плюс Африки;')
EU_AF = ['Amsterdam', 'Austria', 'Belgium', 'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Ghana',
         'Hungary', 'Iceland', 'Ireland', 'Italy', 'Lithuania', 'Poland', 'Portugal', 'South Africa', 'Scotland',
         'Spain', 'Sweden', 'Switzerland', 'U.K.', 'Wales']

mask_CL = df['Company Location'].isin(EU_AF)
mask_CP = df['Cocoa Percent'] > .73
mask = mask_CL & mask_CP
print(mask.sum())
print(df[mask].groupby('Company Location')["Rating>3.1"].mean())
print('--------------------------------------------------')

print('Сделать прогноз, какова вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной'
      ' по всему периоду после 2010 года.')

print((df[df['Review Date'] > 2014]['Rating'] > df[df['Review Date'] > 2010]['Rating'].median()).mean())

