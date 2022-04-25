import numpy as np
import pandas as pd

rng =np.random.default_rng()
df1=pd.DataFrame(rng.integers(-1000,5000, size=(9000,4)))
df2=pd.DataFrame(rng.random((9000,3)))

data = pd.util.testing.makeDataFrame()
data.head()
