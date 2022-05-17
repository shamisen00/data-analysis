import numpy as np
import pandas as pd
import cudf

N = 20000000
MERGE_N = 1000000

df = pd.DataFrame([{"Category": np.random.randint(0,100000), "Category2":np.random.randint(0,100000), "Value": np.random.rand()} for _ in range(N)])
right_df = pd.DataFrame([{"Category": np.random.randint(0,100000), "Value2": np.random.rand()} for _ in range(MERGE_N)])
cudf_table = cudf.from_pandas(df)
cudf_right_table = cudf.from_pandas(right_df)
