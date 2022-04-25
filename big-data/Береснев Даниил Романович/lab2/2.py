import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def drawCall(ds,percSymb):
    fig, ax = plt.subplots()
    ds.plot(kind='bar', ax=ax)
    for p in ax.patches:
        ax.annotate(str(p.get_height())+percSymb, (p.get_x(), p.get_height()))
    ds.plot().set_xlabel("Год")
    ds.plot().set_ylabel("Суммарная длина")
    return None

def map():
    data = pd.read_csv('battles.csv',header=0)
    years = pd.Series(data=data['year'].unique())
    return data,years

data,years = map()
count=[]

for year in years:
    tmp = 0 
    names = data.loc[data['year'] == year]['attacker_king'].dropna()
    for name in names:
        tmp += len(name)
    count.append(tmp)

percents = []
for num in count:
    percents.append(round((num/sum(count))*100,2))

ds_c = pd.Series(data=count, index=years)
drawCall(ds_c,"")

ds_p = pd.Series(data=percents, index=years)
drawCall(ds_p,"%")

df = pd.DataFrame(data=None)
df = pd.concat([ds_p,ds_c], axis=1,ignore_index=True)
df.columns = {"perc","num of symb"}
# По какой-то причине порядок названия столбцов рандомится от запуска к запуску

print(df)
plt.show()
