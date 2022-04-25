import numpy as np

import pandas as pd

rng = np.random.default_rng()

df1 = pd.DataFrame(rng.integers(-1000,5000,size = (9000,4)))
df2 = pd.DataFrame(rng.random((9000,3)))
df = pd.concat([df1,df2],axis = 1)

df.to_csv('beresnev_1', sep='\t',index=False)

df = pd.read_csv('beresnev_1', sep='\t')

df.columns = [x for x in range(0,7)]

#print(df.head())

for i in range(150):
    df.at[np.random.randint(0,9000),0] = 0
    df.at[np.random.randint(0,9000),3] = None

#print(df.head())

df.to_csv('beresnev_2', sep='\t', index=False)

