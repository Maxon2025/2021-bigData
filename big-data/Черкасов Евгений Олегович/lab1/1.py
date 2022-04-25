import numpy as np
import pandas as pd
from math import factorial

rng = np.random.default_rng()


def generate(file_name):
    rng = np.random.default_rng()
    df1 = pd.DataFrame(rng.integers(-1000,5000,size=(9000,4)))
    df2 = pd.DataFrame(rng.random((9000,3))
                      )
    data = pd.concat([df1,df2],axis=1)
    data.columns = [x for x in range(7)]
    
    data.to_csv(file_name,sep='\t', index=False)

def corrupt_the_file(file):
    frame = pd.read_csv(file,sep='\t')
    k = 0
    for i in range(int(len(frame)/100*5)):
        frame.iat[rng.integers(0,len(frame)),rng.integers(0,4)] = rng.random() * 10000 - 5000
        frame.iat[rng.integers(0,len(frame)),rng.integers(4,7)] = None
    frame.to_csv(file + '_corrupted', sep='\t',index=False)

def mask(df,key):
    m = (df[key].isnull() == False) & (np.isnan(df[key]) == False) & (df[key].astype("int") == df[key])
    return df[m]

def float_mask(df,key):
    m = (df[key].isnull() == False) & (np.isnan(df[key]) == False)
    return df[m]

def map_data(df):
    pd.DataFrame.mask = mask
    clear_data = df.mask(0).mask(1).mask(2).mask(3)
    pd.DataFrame.mask = float_mask
    clear_data = clear_data.mask(4).mask(5).mask(6)
    clear_data = clear_data.astype({0 : "int", 1 : "int", 2 : "int", 3 : "int"})
    return clear_data

def process_data(df):
    print("Medium 4:6: ", df.loc[:,4:6].values.sum()/df.loc[:,4:6].shape[0])
    min_int = df.loc[:,0:3].values.sum() % 100
    print("min: ", min_int)
    print("Factorial of min % 100: ", factorial(min_int))


generate('cherkasov')
corrupt_the_file('fomin')
corrupt_the_file('cherkasov')

df = pd.read_csv('cherkasov_corrupted',sep='\t')
df.columns = [x for x in range(7)]
clear_data = map_data(df)
process_data(clear_data)