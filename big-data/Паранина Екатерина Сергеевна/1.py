import numpy as np
import pandas as pd
from math import factorial
"""
Создание своего файла:
rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3)))

data = pd.concat([df1, df2], axis=1)
data.columns = [x for x in range(0,7)]
data.to_csv('paranina.csv', sep='\t', index=False)

df = pd.read_csv('paranina.csv', sep='\t')
df.columns = [x for x in range(0,7)]
print(df.head())

Порча файла:
df = pd.read_csv('pavlov.csv', sep='\t')
df.columns = [0, 1, 2, 3, 4, 5, 6, 7]
print(df.head())
for i in range(100):
    df.at[np.random.randint(0, 9000), 0] = None
    df.at[np.random.randint(0, 9000), 6] = -32
    df.at[np.random.randint(0, 9000), 5] = 80000000000000000000000
print(df.head())
#df.to_csv('pavlov-2.csv', sep='\t')
"""
df = pd.read_csv('paranina2', sep='\t',header=0,index_col=0)
df.columns = [x for x in range(0, 7)]
print(df.head())

def fact(x):
    if x<2:
        return 1
    else:
        return x*fact(x-1)

def pr_dt(df):
    medium_v = sum(df[4] + df[5] + df[6]) / (len(df[4]) + len(df[5]) + len(df[6]))
    print('Medium 4:6: ', medium_v)
    min_v = (sum(df[0]) + sum(df[1]) + sum(df[2]) + sum(df[3])) % 100
    print('Min int 0:3: ',min_v)
    print('Factorial min:',fact(min_v))

def map_d(df):
    clear_data = df.where(df.isnull(), df)
    df_int = df[df.isin(range(-1000, 5000))]
    df_int.fillna(value=0, inplace=True)
    df_int.drop(df_int.iloc[:, 4:7], axis=1, inplace=True)
    df_int = df_int.convert_dtypes()

    df_float = df[(df < 1.) & (df > -1.)]
    df_float.fillna(value=0, inplace=True)
    df_float.drop(df_float.iloc[:, :4], axis=1, inplace=True)

    clear_data = pd.concat([df_int, df_float], axis=1)
    print('filtered /----------------/')
    print(clear_data)
    clear_data.to_csv('paranina2_clear', sep='\t')
    return clear_data

pr_dt(map_d(df))
