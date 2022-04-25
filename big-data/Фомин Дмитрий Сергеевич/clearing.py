import numpy as np
import pandas as pd
from math import factorial
rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000,5000, size =(9000,4)))
df2 = pd.DataFrame(rng.random((9000,3)))
data = pd.concat([df1,df2],axis=1)
#data.columns = [x for x in range(7)]
#data.to_csv('fomin',sep='\t',index = False)

df = pd.read_csv('fomin_corrupted',sep='\t')
df.columns = [x for x in range(7)]

def process_data(df):
    med = (sum(df[4])+sum(df[5])+sum(df[6]))/(len(df[4])+len(df[5])+len(df[6]))
    print("medium ",med)

    min1 = (sum(df[0]) + sum(df[1]) +sum(df[2])+ sum(df[3]))%100
    print("min ",min1)
    print ("factorial ",factorial(min1))

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

    print('filtered /----------------/')
    print(df_filtered)
    df_filtered.to_csv('fomin_cleared',sep='\t',index = False)
    return df_filtered

process_data(map_data(df))
        



