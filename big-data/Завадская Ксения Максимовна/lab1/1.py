import numpy as np
import pandas as pd
from math import factorial

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3)))

data = pd.concat([df1, df2], axis=1) 

data.columns = [x for x in range(7)]

for i in range(2000):
    data.at[np.random.randint(9000), 0] /= 2
    data.at[np.random.randint(9000), 1] = None
    data.at[np.random.randint(9000), 5] /= -9999999999
    data.at[np.random.randint(9000), 6] = None

data.to_csv('zavadskaya1', sep='\t')

df = pd.read_csv('zavadskaya1', sep='\t', header=0, index_col=0)
print('Damaged Dataframe')
print(df.head)
df.columns = [x for x in range(7)]


def process_data(df):
    medium_value = sum(df[4] + df[5] + df[6]) / len(df[4]) + len(df[5]) + len([6])
    print('Medium 4:6: ', medium_value)
    min_int_value = int(sum([df[0].mean(), df[1].mean(), df[2].mean(), df[3].mean()])) % 100
    print('Min % 100 in 0:4 ', min_int_value)
    print('Factorial of min % 100 of 0:4: ', factorial(min_int_value))


def map_data(df):
    df_int = df[df.isin(range(-1000, 5000))]
    df_int.fillna(value=0, inplace=True)
    df_int.drop(df_int.iloc[:, 4:7], axis=1, inplace=True)
    df_int = df_int.convert_dtypes()
    df_float = df[(df < 1.) & (df > -1.)]
    df_float.fillna(value=0, inplace=True)
    df_float.drop(df_float.iloc[:, :4], axis=1, inplace=True)
    df_filtered = pd.concat([df_int, df_float], axis=1)
    print('filtered /----------------/')
    print(df_filtered)

    return df_filtered


filteredData = map_data(df)
filteredData.to_csv('zavadskaya2', sep='\t')

process_data(filteredData)