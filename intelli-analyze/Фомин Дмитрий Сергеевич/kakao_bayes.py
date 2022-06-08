
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np


data = pd.read_csv('flavors_of_cacao.csv',header=0)

EU_AF = ['Amsterdam', 'Austria', 'Belgium','Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Ghana', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Lithuania', 'Poland', 'Portugal','South Africa', 'Scotland', 'Spain', 'Sweden', 'Switzerland', 'U.K.', 'Wales']

def bayes(pA, pB, pBA):
    return pBA*pA/pB


loc = data['Company Location'].dropna()
rat = data['Rating'].dropna()
per = data['Cocoa Percent'].dropna().apply(lambda x: float(x.strip('%')))
rev = data['Review Date'].dropna()

df = pd.concat([loc, rat], axis=1)
df1 = pd.concat([loc, rat], axis=1).groupby('Company Location').size()
dfper = pd.concat([loc, rat, per], axis=1)
df_rating = df.where(df['Rating']>3.1).groupby('Company Location').size()
df_perc = dfper.where(dfper['Cocoa Percent']>73).groupby('Company Location').size()
dfBoth = dfper.where((dfper['Cocoa Percent']>73)&(dfper['Rating']>3.1)).groupby('Company Location').size()
df_rating_prob = df_rating / df1
df_perc_prob =df_perc / df1
dfBoth_prob= dfBoth / df1 
 
pA = df_rating_prob.loc[EU_AF] 
pB = df_perc_prob.loc[EU_AF]
pBA = dfBoth_prob.loc[EU_AF]
print("Задание1 \n",df_perc_prob)
print("Задание2 \n",bayes(pA,pB,pBA))

med = data[data['Review Date']>2010]['Rating'].median()

pA1 = data[data['Rating'] > med].count()['Rating'] / data['Rating'].count()
pB1 = data[data['Review Date'] > 2014].count()['Review Date'] / data['Review Date'].count()
pBA1 = data[(data['Rating'] > med) & (data['Review Date'] > 2014)].count()['Rating'] / data['Review Date'].count()

print("Задание3 \n",bayes(pA1,pB1,pBA1))
