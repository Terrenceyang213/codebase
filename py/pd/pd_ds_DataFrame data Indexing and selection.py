# Operation                       Syntax          Result
# Select column                   df[col]         Series
# Select row by label             df.loc[label]   Series
# Select row by integer location  df.iloc[loc]    Series
# Slice rows                      df[5:10]        DataFrame
# Select rows by boolean vector   df[bool_vec]    DataFrame


#%%
import numpy as np
import pandas as pd

# %%
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    }

df1 = pd.DataFrame(d)
df1
#   one	two
# a	1.0	1.0
# b	2.0	2.0
# c	3.0	3.0
# d	NaN	4.0


# %%
# select row by label and row num

df1.loc["a"]
# one    1.0
# two    1.0
# Name: a, dtype: float64

df1.loc[2]
# Keyerror 2


df1.iloc[2]
# one    3.0
# two    3.0
# Name: c, dtype: float64


# %% 选择特定行之前或者之后的n行
d = {
    "one": pd.Series([1.0, 2.0, 3.0,5]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0]),
    }

df2 = pd.DataFrame(d)
df2
#   one	two
# a	1.0	1.0
# b	2.0	2.0
# c	3.0	3.0
# d	NaN	4.0


def get_n_rows(df, cursor, n, columns=None):
    if columns is None:
        columns = df.columns.values
    return df.loc[min(cursor,(cursor + n)) : max(cursor,(cursor + n)), columns]

get_n_rows(df2, 3, 2, None)
# 	one	two
# 3	5.0	4.0

get_n_rows(df2, 2,-2, None)
#   one	two
# 1	2.0	2.0
# 2	3.0	3.0

get_n_rows(df2, 2,1, None)
# 	one	two
# 2	3.0	3.0
# 3	5.0	4.0

get_n_rows(df2, 2,-1, None)
# 	one	two
# 1	2.0	2.0
# 2	3.0	3.0

get_n_rows(df2, 2,-1, ["one"])
# 	one
# 1	2.0
# 2	3.0
# %%

# %%
