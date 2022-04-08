# 通过熊猫数据结构之间的二元操作，有两个关键的关注点：
#   高维（例如DataFrame）和低维（例如Series）对象之间的广播行为。
#   计算中缺少数据。
#%%
import numpy as np
import pandas as pd

#%%
# 将Series作为input的参数，广播行为
df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)

df2 = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(4), index=["a", "b", "c","d"]),
        "two": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)


df 
#   one	        two	        three
# a	0.611323	1.373521	NaN
# b	0.600843	-0.187050	-0.597436
# c	2.369744	-1.078043	-0.273361
# d	NaN	        -0.820983	-0.373169

row = df.iloc[1]
# one      0.600843
# two     -0.187050
# three   -0.597436
# Name: b, dtype: float64

column = df["two"]
# a    1.373521
# b   -0.187050
# c   -1.078043
# d   -0.820983
# Name: two, dtype: float64




# %%
# 按列label匹配，即按行广播
df.sub(row, axis="columns")
#   one	        two	        three
# a	0.010479	1.560571	NaN
# b	0.000000	0.000000	0.000000
# c	1.768901	-0.890992	0.324075
# d	NaN	        -0.633933	0.224267

df.sub(row, axis=1)
#   one	        two	        three
# a	0.010479	1.560571	NaN
# b	0.000000	0.000000	0.000000
# c	1.768901	-0.890992	0.324075
# d	NaN	        -0.633933	0.224267

df.sub(column , axis="index")
#   one	        two	three
# a	-0.762198	0.0	NaN
# b	0.787894	0.0	-0.410385
# c	3.447787	0.0	0.804682
# d	NaN	        0.0	0.447815

df.sub(column, axis=0)
#   one	        two	three
# a	-0.762198	0.0	NaN
# b	0.787894	0.0	-0.410385
# c	3.447787	0.0	0.804682
# d	NaN	        0.0	0.447815


# %%
# MultiIndex DataFrame 用Series进行广播
dfmi = df.copy()
dfmi.index = pd.MultiIndex.from_tuples(
   [(1, "a"), (1, "b"), (1, "c"), (2, "a")], names=["first", "second"]
)

dfmi
#               one	        two	        three
# first	second			
# 1	    a	    0.611323	1.373521	NaN
#       b	    0.600843	-0.187050	-0.597436
#       c	    2.369744	-1.078043	-0.273361
# 2	    a	    NaN	        -0.820983	-0.373169

dfmi.sub(column, axis=0, level="second")
#                one        two	        three
# first	second			
# 1	    a	    -0.762198	0.000000	NaN
#       b	    0.787894	0.000000	-0.410385
#       c	    3.447787	0.000000	0.804682
# 2	    a	    NaN	        -2.194504	-1.746690

# 2-a-two: -0.820983 - 1.373521 = -2.194504


# %% Series and Index also support the divmod() builtin. 
s = pd.Series(np.arange(10))
div, rem = divmod(s, 3)
div
# 0    0
# 1    0
# 2    0
# 3    1
# 4    1
# 5    1
# 6    2
# 7    2
# 8    2
# 9    3
# dtype: int32

rem
# 0    0
# 1    1
# 2    2
# 3    0
# 4    1
# 5    2
# 6    0
# 7    1
# 8    2
# 9    0
# dtype: int32


idx = pd.Index(np.arange(5))
div, rem = divmod(idx, 3)
idx     # Int64Index([0, 1,2,3,4], dtype='int64')
div     # Int64Index([0, 0, 0, 1, 1],dtype='int64')
rem     # Int64Index([0, 1, 2, 0, 1],dtype='int64')


# We can also do elementwise(逐元素对应) divmod():
div, rem = divmod(s, s)
div
#  0    NaN
#  1    1.0
#  2    1.0
#  3    1.0
#  4    1.0
#  5    1.0
#  6    1.0
#  7    1.0
#  8    1.0
#  9    1.0
#  dtype: float64,

rem
#  0    NaN
#  1    0.0
#  2    0.0
#  3    0.0
#  4    0.0
#  5    0.0
#  6    0.0
#  7    0.0
#  8    0.0
#  9    0.0
#  dtype: float64



# %%
# In Series and DataFrame, the arithmetic functions have the option of inputting a fill_value, 
# namely a value to substitute when at most one of the values at a location are missing. 
df
#   one	        two	        three
# a	0.611323	1.373521	NaN
# b	0.600843	-0.187050	-0.597436
# c	2.369744	-1.078043	-0.273361
# d	NaN	        -0.820983	-0.373169

df2
#     one	        two	        three
# a	1.340693	2.294377	NaN
# b	1.509014	-0.820533	-0.976451
# c	1.714386	0.293330	-1.323291
# d	0.356543	NaN	        -0.213561

df + df2
#   one	        two	        three
# a	1.952016	3.667898	NaN
# b	2.109858	-1.007583	-1.573887
# c	4.084130	-0.784713	-1.596652
# d	NaN	        NaN	        -0.586730

df.add(df2, fill_value=0) 
#fill_value将两个相加数中有一个是nan时，将nan用0替换，但是如果两个都是nan则保留
#   one	        two	        three
# a	1.952016	3.667898	NaN
# b	2.109858	-1.007583	-1.573887
# c	4.084130	-0.784713	-1.596652
# d	0.356543	-0.820983	-0.586730



# %%
# Series and DataFrame have the binary comparison methods eq, ne, lt, gt, le, 
# and ge whose behavior is analogous to the binary arithmetic operations described above:
df.gt(df2)
# 	one	    two	    three
# a	False	False	False
# b	False	True	True
# c	True	False	True
# d	False	False	False

df2.ne(df)
# 	one	    two	    three
# a	True	True	True
# b	True	True	True
# c	True	True	True
# d	True	True	True



# %% Boolean reductions
# You can apply the reductions: empty, any(), all(), and bool() 
# to provide a way to summarize a boolean result.

df>0
#   one	    two	    three
# a	True	True	False
# b	True	False	False
# c	True	False	False
# d	False	False	False

(df > 0).all() #axis=0
# one      False
# two      False
# three    False
# dtype: bool

(df>0).all(axis=1)
# a    False
# b    False
# c    False
# d    False
# dtype: bool

(df > 0).any()
# one       True
# two       True
# three    False
# dtype: bool

(df>0).any().any()
# True

#%% test if the DataFrame is empty
df.empty
# False

pd.DataFrame(columns=list("ABC")).empty
# True


# %% To evaluate single-element pandas objects in a boolean context, 
# use the method bool():
pd.Series([True]).bool()
# True

pd.Series([False]).bool()
#False

pd.DataFrame([[True]]).bool()
#True

pd.DataFrame([[False]]).bool()
#False

# tips
# if df: pass
# or
# df1 and df2:
# These will both raise errors, as you are trying to compare multiple values.:
# ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().



# %% Comparing if objects are equivalent
# Often you may find that there is more than one way to compute the same result. 
# As a simple example, consider df + df and df * 2. 
# To test that these two computations produce the same result, given the tools shown above, 
# you might imagine using (df + df == df * 2).all(). 
# But in fact, this expression is False:

df + df == df * 2
#   one	    two	    three
# a	True	True	False
# b	True	True	True
# c	True	True	True
# d	False	True	True

# Notice that the boolean DataFrame df + df == df * 2 contains some False values! 
# This is because NaNs do not compare as equals:
np.nan == np.nan
#Out[59]: False

df+df
#   one	        two	        three
# a	-1.730587	0.891824	NaN
# b	-3.852011	-1.075136	-3.017860
# c	0.300993	3.602723	-3.599318
# d	NaN	        -0.283489	-1.387996

df*2
#   one	        two	        three
# a	-1.730587	0.891824	NaN
# b	-3.852011	-1.075136	-3.017860
# c	0.300993	3.602723	-3.599318
# d	NaN	        -0.283489	-1.387996


# So, NDFrames (such as Series and DataFrames) have an equals() method for testing equality, 
# with NaNs in corresponding locations treated as equal.
(df + df).equals(df * 2)
# True

(df + df == df * 2).all(axis="index")
# one      False
# two       True
# three    False
# dtype: bool

(df + df == df * 2).all(None)
# False

# DataFrame.all(axis=0, bool_only=None, skipna=True, level=None, **kwargs)
# Return whether all elements are True, potentially over an axis.
# axis:{0 or ‘index’, 1 or ‘columns’, None}, default 0
#     Indicate which axis or axes should be reduced.
#         0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
#         1 / ‘columns’ : reduce the columns, return a Series whose index is the original index.
#         None : reduce all axes, return a scalar.


# Note that the Series or DataFrame index needs to be in the same order for equality to be True:
df1 = pd.DataFrame({"col": ["foo", 0, np.nan]}, index=[0, 1, 2])
df2 = pd.DataFrame({"col": [np.nan, 0, "foo"]}, index=[2, 1, 0])
df1.equals(df2)
# False
df1.equals(df2.sort_index())
# True


# %% Comparing array-like objects: Comparing a pandas data structure with a scalar value
# can conveniently perform element-wise comparisons 
# when comparing a pandas data structure with a scalar value
pd.Series(["foo", "bar", "baz"]) == "foo"
# 0     True
# 1    False
# 2    False
# dtype: bool

pd.Index(["foo", "bar", "baz"]) == "foo"
# array([ True, False, False])


# element-wise comparisons between different array-like objects of the same length:
pd.Series(["foo", "bar", "baz"]) == pd.Index(["foo", "bar", "qux"])
# 0     True
# 1     True
# 2    False
# dtype: bool

pd.Series(["foo", "bar", "baz"]) == np.array(["foo", "bar", "qux"])
# 0     True
# 1     True
# 2    False
# dtype: bool

# Trying to compare Index or Series objects of different lengths will raise a ValueError:
# Note that this is different from the NumPy behavior where a comparison can be broadcast:

pd.Series(['foo', 'bar', 'baz'],index=[0,1,2]) == pd.Series(['foo', 'bar'],index=[0, 1,])
# ValueError: Can only compare identically-labeled Series objects

np.array([1, 2, 3]) == np.array([2])
# array([False,  True, False])

# it can return False if broadcasting can not be done:
np.array([1, 2, 3]) == np.array([1, 2])
# elementwise comparison failed; this will raise an error in the future.
# False

# %% Combining overlapping data sets
# A problem occasionally arising is the combination of two similar data sets 
# where values in one are preferred over the other. 
# An example would be two data series representing a particular economic indicator 
# where one is considered to be of “higher quality”. 
# However, the lower quality series might extend further back in history 
# or have more complete data coverage. 
# As such, we would like to combine two DataFrame objects 
# where missing values in one DataFrame are conditionally filled with like-labeled values 
# from the other DataFrame. 
# The function implementing this operation is combine_first(), which we illustrate:

df1 = pd.DataFrame(
    {
    "A": [1.0, np.nan, 3.0, 5.0, np.nan],
    "B": [np.nan, 2.0, 3.0, np.nan, 6.0],
    }
    )

df2 = pd.DataFrame(
    {
    "A": [5.0, 2.0, 4.0, np.nan, 3.0, 7.0],
    "B": [np.nan, np.nan, 3.0, 4.0, 6.0, 8.0],
    }
)

df1

#      A    B
# 0  1.0  NaN
# 1  NaN  2.0
# 2  3.0  3.0
# 3  5.0  NaN
# 4  NaN  6.0

df2
#    A    B
# 0  5.0  NaN
# 1  2.0  NaN
# 2  4.0  3.0
# 3  NaN  4.0
# 4  3.0  6.0
# 5  7.0  8.0

df1.combine_first(df2)
#     A	B
# 0	1.0	NaN
# 1	2.0	2.0
# 2	3.0	3.0
# 3	5.0	4.0
# 4	3.0	6.0
# 5	7.0	8.0

# General DataFrame combine combine()
# The combine_first() method above calls the more general DataFrame.combine(). 
# This method takes another DataFrame and a combiner function, 
# aligns the input DataFrame and then passes the combiner function pairs of Series 
# (i.e., columns whose names are the same).

def combiner(x, y):
    return np.where(pd.isna(x), y, x)

df1.combine(df2, combiner)
#   A	B
# 0	1.0	NaN
# 1	2.0	2.0
# 2	3.0	3.0
# 3	5.0	4.0
# 4	3.0	6.0
# 5	7.0	8.0

# np.where(condition[, x, y])
# Return elements chosen from x or y depending on condition.
# condition:array_like, bool  Where True, yield x, otherwise yield y.