#%% 
import numpy as np
import pandas as pd
import dask.dataframe as dd

df = pd.DataFrame({'X': np.arange(10), 
                   'Y': np.arange(10, 20),
                   'Z': np.arange(20, 30)},
                  index=list('abcdefghij'))

ddf = dd.from_pandas(df, 2)

#%%
ddf.columns
ddf.index
ddf.divisions
ddf.npartitions

#%%
ddf.sum()
ddf.sum().compute()