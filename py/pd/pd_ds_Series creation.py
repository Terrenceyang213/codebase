#%%
import numpy as np
import pandas as pd


#%%
data = [100,200,300,400]
index = ['a','b','c','d']
ser1 = pd.Series(data, index=index)
ser1
# a    100
# b    200
# c    300
# d    400
# dtype: int64

# Here, data can be many different things:
# a Python dict
# an ndarray
# a scalar value (like 5)



# %%
# use ndarray as input to create a Series
# If data is an ndarray, index must be the same length as data. 
# If no index is passed, one will be created having values [0, ..., len(data) - 1].
ser2 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
ser2
# a   -1.165009
# b    0.172845
# c   -0.394353
# d   -1.000572
# e   -0.747551
# dtype: float64

ser2.index
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

pd.Series(np.random.randn(5))
# 0    0.224724
# 1   -0.320617
# 2   -0.329635
# 3    0.159074
# 4    1.809467
# dtype: float64



# %%
# use dict as input to create a Series

d = {"b": 1, "a": 0, "c": 2}
ser3 = pd.Series(d)
ser3

# b    1
# a    0
# c    2
# dtype: int64

#%%
d = {"a": 0.0, "b": 1.0, "c": 2.0}
ser4 = pd.Series(d)
ser4
# a    0.0
# b    1.0
# c    2.0
# dtype: float64


ser5 = pd.Series(d, index=["b", "c", "d", "a"])
ser5
# b    1.0
# c    2.0
# d    NaN
# a    0.0
# dtype: float64


# %%
# create Series From scalar value
ser6 = pd.Series(5.0, index=["a", "b", "c", "d", "e"])
ser6
# a    5.0
# b    5.0
# c    5.0
# d    5.0
# e    5.0
# dtype: float64

# %%
# Series的访问类似ndarry,可以用索引，切片
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
s
# a   -1.866284
# b    1.214087
# c    0.167311
# d   -1.176580
# e    0.130682
# dtype: float64

s[0]
# -1.8662837526385752

s[:3]
# a   -1.866284
# b    1.214087
# c    0.167311
# dtype: float64

s[s > s.median()]
# b    1.214087
# c    0.167311
# dtype: float64

s[[4, 3, 1]]
# e    0.130682
# d   -1.176580
# b    1.214087
# dtype: float64

np.exp(s)
# a    0.154697
# b    3.367220
# c    1.182122
# d    0.308332
# e    1.139605
# dtype: float64

s.dtypes
# dtype('float64')


#%%
# If you need the actual array backing a Series, use Series.array.
s.array
# <PandasArray>
# [-1.8662837526385752,  1.2140873637005767, 0.16731143330909554,
#  -1.1765795132054915, 0.13068193412867427]
# Length: 5, dtype: float64

# Series.array will always be an ExtensionArray. 
# Briefly, an ExtensionArray is a thin wrapper around one or more concrete arrays like a numpy.ndarray. 
# pandas knows how to take an ExtensionArray and store it in a Series or a column of a DataFrame.

# %%
# While Series is ndarray-like, if you need an actual ndarray, then use Series.to_numpy().
s.to_numpy()
# array([-1.86628375,  1.21408736,  0.16731143, -1.17657951,  0.13068193])


# %%
# Series is dict-like
# A Series is like a fixed-size dict in that you can get and set values by index label:

s["a"]
# -1.8662837526385752

s["e"] = 12.0
s
# a    -1.866284
# b     1.214087
# c     0.167311
# d    -1.176580
# e    12.000000
# dtype: float64

"e" in s
# True

"f" in s
# False

s["f"]
# Keyerror "f"

s.get("f")
s.get("f",np.nan)
# nan


# %%
# 用Series进行向量化计算
s+s
# a    -3.732568
# b     2.428175
# c     0.334623
# d    -2.353159
# e    24.000000
# dtype: float64

s*2
# a    -3.732568
# b     2.428175
# c     0.334623
# d    -2.353159
# e    24.000000
# dtype: float64

np.exp(s)
# a         0.154697
# b         3.367220
# c         1.182122
# d         0.308332
# e    162754.791419
# dtype: float64


# %%
# The result of an operation between unaligned Series will have the union of the indexes involved.
# If a label is not found in one Series or the other, the result will be marked as missing NaN.

s[1:] + s[:-1]
# a         NaN
# b    2.428175
# c    0.334623
# d   -2.353159
# e         NaN
# dtype: float64


#%%
# 对Series命名
s2 = pd.Series(np.random.randn(5), name="something")
s2

# 0    0.401521
# 1   -0.712245
# 2    0.655243
# 3   -0.145726
# 4    1.106183
# Name: something, dtype: float64


s2.name
# 'something'

s3 = s2.rename("diff")
s3
# 0   -0.232820
# 1   -0.155863
# 2    0.226485
# 3   -0.057465
# 4    0.299539
# Name: diff, dtype: float64

s3 is s2
# False



# %%
