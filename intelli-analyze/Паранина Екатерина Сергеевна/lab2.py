import pandas as pd

data = pd.read_csv('./flavors_of_cacao.csv', header=0)



all_cl = data['Company Location'].dropna()
all_rating = data['Rating'].dropna()
all_percent = data['Cocoa Percent'].dropna().apply(
    lambda x: float(x.strip('%')))

south_countries=['Argentina','Australia','Bolivia','Brazil','Chile','Colombia','Ecuador','Fiji','Madagascar','New Zealand','Peru','South Africa']

# задание 1

dt = pd.concat([all_cl, all_rating], axis=1)
dt_cl_size = pd.concat([all_cl, all_rating], axis=1).groupby('Company Location').size()
dt_r=dt.where(dt['Rating']>3.1).dropna()
dt_r=dt_r.groupby('Company Location').size()
pa=dt_r.div(dt_cl_size)

print('Априорные вероятности для каждой страны происхождения получения оценки выше 3.1:')
print(pa)

print('------------------------------')

# задание 2

def bayes(pA, pB, pBA):
    return pBA*pA/pB

dt2 = pd.concat([all_cl, all_rating,all_percent], axis=1)
dt_cl_size2 = pd.concat([all_cl, all_rating,all_percent], axis=1).groupby('Company Location').size()

dt_r_and_p=dt2.where((dt2['Rating']>3.1) & (dt2['Cocoa Percent']>73)).dropna()
dt_p=dt2.where(dt2['Cocoa Percent']>73).dropna()

dt_r_and_p=dt_r_and_p.groupby('Company Location').size()
dt_p=dt_p.groupby('Company Location').size()


pa2=pa.loc[south_countries]
pba2=dt_r_and_p.div(dt_cl_size2).loc[south_countries]
pb2=dt_p.div(dt_cl_size2).loc[south_countries]


print('Вероятность того, что новый сорт какао с содержанием выше 73% будет имет оценку выше 3.1 для стран южного полушария:')
print(bayes(pa2, pb2, pba2))

print('------------------------------')

# задание 3

median = data[data['Review Date'] > 2010]['Rating'].median()

pa3 = data[data['Rating'] > median].count()['Rating'] / data['Rating'].count()
pb3 = data[data['Review Date'] > 2014].count()['Review Date'] / data['Review Date'].count()
pba3 = data[(data['Rating'] > median) & (data['Review Date'] > 2014)].count()['Rating'] /  data['Review Date'].count()


print('вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной по всему периоду после 2010 года:')
print(bayes(pa3, pb3, pba3))




