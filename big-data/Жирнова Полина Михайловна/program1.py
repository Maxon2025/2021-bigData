import numpy as np
import pandas as pd

rng = np.random.default_rng()

df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random(size=(9000, 3)))
df = pd.concat([df1, df2], axis=1)

df.to_csv('zhirnova_1', sep='\t',index=False)

df.columns = [x for x in range(7)]

print(df.head())

for i in range(100):
    df.at[np.random.randint(0,9000), 0] = 0
    df.at[np.random.randint(0,9000), 3] = None
    df.at[np.random.randint(0,9000), 2] = 1

df.to_csv('zhirnova_2', sep='\t',index=False)
print(df.head())
