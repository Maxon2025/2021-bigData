import numpy as np
import pandas as pd

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000,5000, size =(9000,4)))
df2 = pd.DataFrame(rng.random((3000,3)))
data = pd.concat([df1,df2],axis=1)

data.to_csv('fomin',sep='\t')

df = pd.read_csv('fomin',sep='\t')

print(df.head())

