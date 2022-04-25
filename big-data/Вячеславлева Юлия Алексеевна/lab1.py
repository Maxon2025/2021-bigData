import numpy as np
import pandas as pd
from math  import factorial

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3)))

data = pd.concat([df1, df2], axis=1)

data.columns = [x for x in range(7)]
#print(data.head())
#data.to_csv('vyacheslavleva', sep='\t')
df = pd.read_csv('vyacheslavleva', sep='\t', header=0, index_col=0)
#print(df.head())

df.columns = [x for x in range(7)]
for i in range(100):
    df.at[np.random.randint(0, 9000), 0] /= 2
    df.at[np.random.randint(0, 9000), 1] = None
    df.at[np.random.randint(0, 9000), 5] = -9999999999
    df.at[np.random.randint(0, 9000), 6] = None

df.to_csv('vyacheslavleva_1', sep='\t')
print(df.head())

def fact(x):
    if x < 2:
        return 1
    else:
        return x * fact(x - 1)


df = pd.read_csv('vyacheslavleva_1', sep='\t', header=0, index_col=0)
df.columns = [x for x in range(7)]
print(df)


def process_data(df):
    medium_value = sum(df[4] + df[5] + df[6]) / (len(df[4]) + len(df[5]) + len(df[6]))
    print('Medium 4:6: ', medium_value)
    min_int_value = (sum(df[0]) + sum(df[1]) + sum(df[2]) + sum(df[3])) % 100
    print(min_int_value)
    print('Factorial of min % 100 of 0:4: ', factorial(min_int_value))


def map_data(df):
    # df.isnull
    # df.ge
    # df.dtypes
    # df.empty

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

clearDF = map_data(df)
clearDF.to_csv('vyacheslavleva_2', sep='\t')

process_data(map_data(df))