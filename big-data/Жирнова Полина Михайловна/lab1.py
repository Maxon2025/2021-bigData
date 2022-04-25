import numpy as np
import pandas as pd
from math import factorial

rng = np.random.default_rng()

df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3))) 

df = pd.concat([df1, df2], axis=1) #вдоль колонки

df.to_csv('zhirnova_1', sep='\t',index=False)

df.columns = [x for x in range(7)]
print(df.head())

for i in range(100):
    df.at[np.random.randint(0,9000), 0] = 0
    df.at[np.random.randint(0,9000), 3] = None
    df.at[np.random.randint(0,9000), 2] = 1

df.to_csv('zhirnova_2', sep='\t',index=False)

df.columns = [x for x in range(7)]
print("\n",df.head())

def fact(x):
    if x<2:
        return 1
    else:
        return x*fact(x-1)

def process_data(df):
    medium_value= sum(df[4]+df[5]+df[6])/(len(df[4])+len(df[5])+len(df[6]))
    print('\nMedium 4:6: ', medium_value)
    min_int_value = (sum(df[0]) + sum(df[1]) + sum(df[2]) + sum(df[3])) % 100
    print(min_int_value)
    print('Factorial of min % 100 of 0:4: ', factorial(min_int_value))


def map_data(df):
    #df.isnull
    #df.ge
    #df.dtypes
    #df.empty

    df_int = df[df.isin(range(-1000, 5000))]
    df_int.fillna(value=0, inplace=True)
    df_int.drop(df_int.iloc[:, 4:7], axis=1, inplace=True)
    df_int = df_int.convert_dtypes()

    df_float = df[(df<1.)&(df>-1.)]
    df_float.fillna(value=0, inplace=True)
    df_float.drop(df_float.iloc[:, :4], axis=1, inplace=True)

    df_filtered = pd.concat([df_int, df_float], axis=1)
    df_filtered.to_csv('zhirnova_filtered', sep='\t',index=False)
    print('\nfiltered /----------------/\n')
    print(df_filtered)

    return df_filtered


process_data(map_data(data))
