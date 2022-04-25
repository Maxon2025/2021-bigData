import numpy as np
import pandas as pd
from math import factorial

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3)))

data = pd.concat([df1,df2],  axis=1)

data.columns = [x for x in range(7)]

for i in range(1000):
    data.at[np.random.randint(9000), 0] /= 10
    data.at[np.random.randint(9000), 3] = None
    data.at[np.random.randint(9000), 4] = -99999999999999999999999999999999999999999999999999999999999999999999999999
    data.at[np.random.randint(9000), 6] = np.random.randint(2,10)

data.to_csv('Kruglov_dmgd', sep='\t')
'''
def fact(x):
    if x < 2:
        return 1
    else:
        return x*fact(x-1)
'''
df = pd.read_csv('Kruglov_dmgd', sep='\t', header=0, index_col=0)

df.columns = [x for x in range(7)]
'''
def process_data(df):
    medium_value = sum(df[4] + df[5] + df[6]) / (len(df[4]) + len(df[5]) + len(df[6]))
    print(medium_value)
    min_int_value = int(sum(df[0]) + sum(df[1]) + sum(df[2]) + sum(df[3])) % 100
    print(min_int_value)
    print(factorial(min_int_value))
'''
def map_data(df):
    df1 = df[df.isin(range(-1000, 5000))]
    df1.fillna(value=0, inplace=True)
    df1.drop(df1.iloc[:, 4:7], axis=1, inplace=True)

    df2 = df[(df < 1) & (df > -1)]
    df2.fillna(value=0, inplace=True)
    df2.drop(df2.iloc[:, :4], axis=1, inplace=True)

    df = pd.concat([df1, df2], axis=1)
    return df

new_df = map_data(df)
new_df.to_csv('Kruglov_crrct', sep='\t')