import numpy as np
import pandas as pd
from math import factorial

rand = np.random.default_rng()
df1 = pd.DataFrame(rand.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rand.random((9000, 3)))

df = pd.concat([df1, df2], axis=1)

df.columns = [x for x in range(7)]
df.to_csv('./Гараев Денис Ильдарович/garaevClean', sep='\t')
print(df.head())

df.columns = [x for x in range(7)]
for i in range(100):
    df.at[rand.integers(9000), 1] *= 0.33
    df.at[rand.integers(9000), 5] = -9999999999
    df.at[rand.integers(9000), 0] = None

df.to_csv('./Гараев Денис Ильдарович/garaevBroken', sep='\t')
print(df.head())

df = pd.read_csv('./Гараев Денис Ильдарович/garaevBroken', sep='\t', header=0, index_col=0)
df.columns = [x for x in range(7)]

def process_df(df):
    medium_value = sum(df[4] + df[5] + df[6]) / (len(df[4]) + len(df[5]) + len(df[6]))
    print('Medium 4:6: ', medium_value)
    min_int_value = (sum(df[0]) + sum(df[1]) + sum(df[2]) + sum(df[3])) % 100
    print(min_int_value)
    print('Factorial of min % 100 of 0:4: ', factorial(min_int_value))

def map_df(df):
    df_int = df[df.isin(range(-1000, 5000))]
    df_int.fillna(value=0, inplace=True)
    df_int.drop(df_int.iloc[:, 4:7], axis=1, inplace=True)
    df_int = df_int.convert_dtypes()

    df_float = df[(df < 1.) & (df > -1.)]
    df_float.fillna(value=0, inplace=True)
    df_float.drop(df_float.iloc[:, :4], axis=1, inplace=True)

    df_filtered = pd.concat([df_int, df_float], axis=1)

    print('filtered /----------------/')
    print(df_filtered.head())

    return df_filtered

clearDF = map_df(df)
clearDF.to_csv('./Гараев Денис Ильдарович/garaevRestored', sep='\t')

process_df(map_df(df))