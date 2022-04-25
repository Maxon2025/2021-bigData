import numpy as np
import pandas as pd

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(1000,5000, size =(9000,4)))
df2 = pd.DataFrame(rng.random((9000,3)))
data = pd.concat([df1,df2],axis=1)
#data.columns = [x for x in range(7)]
#data.to_csv('fomin',sep='\t',index = False)

df = pd.read_csv('Fedin',sep='\t')
df.columns = [x for x in range(7)]

print(df.head())


for i in range(100):
    df.at[np.random.randint(0,9000),0]= None
    df.at[np.random.randint(0,9000),6]= -404
    df.at[np.random.randint(0,9000),5]= 1010101010100000000
    
df.to_csv('Fedin1',sep='\t',index = False)
