
#%%
import numpy as np
import pandas as pd
# You may wish to take an object and reindex its axes to be labeled the same as another object. 
# While the syntax for this is straightforward albeit verbose, 
# it is a common enough operation that the reindex_like() method is available to make this simpler:
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    }

df1 = pd.DataFrame(d)
df1
# 	one	two
# a	1.0	1.0
# b	2.0	2.0
# c	3.0	3.0
# d	NaN	4.0

df2 = pd.DataFrame(d, index=["d", "b", "a"])
df2
# 	one	two
# d	NaN	4.0
# b	2.0	2.0
# a	1.0	1.0

df1.reindex_like(df2)
# 	one	two
# d	NaN	4.0
# b	2.0	2.0
# a	1.0	1.0


#%% Aligning objects with each other with align
# The align() method is the fastest way to simultaneously align two objects. 
# It supports a join argument (related to joining and merging):
    # join='outer': take the union of the indexes (default)
    # join='left': use the calling object’s index
    # join='right': use the passed object’s index
    # join='inner': intersect the indexes

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# a    0.634075
# b   -1.195871
# c    0.247151
# d    1.536319
# e   -0.343603
# dtype: float64

s1 = s[:4]
# a    0.634075
# b   -1.195871
# c    0.247151
# d    1.536319
# dtype: float64


s2 = s[1:]
# b   -1.195871
# c    0.247151
# d    1.536319
# e   -0.343603
# dtype: float64

s1.align(s2)
# (a    0.928762
#  b    0.294130
#  c    0.369975
#  d   -0.617241
#  e         NaN
#  dtype: float64,
#  a         NaN
#  b    0.294130
#  c    0.369975
#  d   -0.617241
#  e   -0.676423
#  dtype: float64)

s1.align(s2, join="inner")
# (b    0.208375
#  c   -0.651259
#  d   -1.068423
#  dtype: float64,
#  b    0.208375
#  c   -0.651259
#  d   -1.068423
#  dtype: float64)

s1.align(s2, join="left")
# (a   -2.652222
#  b   -0.994974
#  c   -0.635279
#  d   -0.058937
#  dtype: float64,
#  a         NaN
#  b   -0.994974
#  c   -0.635279
#  d   -0.058937
#  dtype: float64)

#%% For DataFrames, 
# the join method will be applied to both the index and the columns by default:
# Returns: (left, right)(DataFrame, type of other)


df3 = pd.DataFrame(d["one"], index=["d", "b", "a"],columns=["one"])
# 	one
# d	NaN
# b	2.0
# a	1.0

df1.align(df3, join="inner")
# (   one
#  a  1.0
#  b  2.0
#  d  NaN,
#     one
#  a  1.0
#  b  2.0
#  d  NaN)

# You can also pass an axis option to only align on the specified axis:
df1.align(df3, join="inner",axis=0)
# (   one  two
#  a  1.0  1.0
#  b  2.0  2.0
#  d  NaN  4.0,
#     one
#  a  1.0
#  b  2.0
#  d  NaN)

df1.align(df3, join="inner",axis=1)
# (   one
#  a  1.0
#  b  2.0
#  c  3.0
#  d  NaN,
#     one
#  d  NaN
#  b  2.0
#  a  1.0)

#%% If you pass a Series to DataFrame.align(), 
# you can choose to align both objects either on the DataFrame’s index or columns using the axis argument:
# %%
df2.iloc[0]
# one    NaN
# two    4.0
# Name: d, dtype: float64

df1.align(df2.iloc[0], axis=1)
# (   one  two
#  a  1.0  1.0
#  b  2.0  2.0
#  c  3.0  3.0
#  d  NaN  4.0,
#  one    NaN
#  two    4.0
#  Name: d, dtype: float64)


#%% Filling while reindexing
# reindex() takes an optional parameter method which is a filling method 
# chosen from the following table:

# Method              Action
# pad / ffill         Fill values forward
# bfill / backfill    Fill values backward
# nearest             Fill from the nearest index value

rng = pd.date_range("1/3/2000", periods=8)
ts = pd.Series(np.random.randn(8), index=rng)
ts2 = ts[[0, 3, 6]]

#%%
ts
# 2000-01-03    1.587551
# 2000-01-04    1.970441
# 2000-01-05    0.550381
# 2000-01-06   -0.473532
# 2000-01-07   -0.318168
# 2000-01-08   -0.621705
# 2000-01-09    1.917432
# 2000-01-10    0.618173
# Freq: D, dtype: float64


ts2
# 2000-01-03    1.587551
# 2000-01-06   -0.473532
# 2000-01-09    1.917432
# Freq: 3D, dtype: float64


ts2.reindex(ts.index)
# 2000-01-03    1.587551
# 2000-01-04         NaN
# 2000-01-05         NaN
# 2000-01-06   -0.473532
# 2000-01-07         NaN
# 2000-01-08         NaN
# 2000-01-09    1.917432
# 2000-01-10         NaN
# Freq: D, dtype: float64

ts2.reindex(ts.index, method="ffill")
# 2000-01-03    1.587551
# 2000-01-04    1.587551
# 2000-01-05    1.587551
# 2000-01-06   -0.473532
# 2000-01-07   -0.473532
# 2000-01-08   -0.473532
# 2000-01-09    1.917432
# 2000-01-10    1.917432
# Freq: D, dtype: float64


ts2.reindex(ts.index, method="bfill")
# 2000-01-03    1.587551
# 2000-01-04   -0.473532
# 2000-01-05   -0.473532
# 2000-01-06   -0.473532
# 2000-01-07    1.917432
# 2000-01-08    1.917432
# 2000-01-09    1.917432
# 2000-01-10         NaN
# Freq: D, dtype: float64

ts2.reindex(ts.index, method="nearest")
# 2000-01-03    1.587551
# 2000-01-04    1.587551
# 2000-01-05   -0.473532
# 2000-01-06   -0.473532
# 2000-01-07   -0.473532
# 2000-01-08    1.917432
# 2000-01-09    1.917432
# 2000-01-10    1.917432
# Freq: D, dtype: float64


# %%
# These methods require that the indexes are ordered increasing or decreasing.
# Note that the same result could have been achieved using fillna 
# (except for method='nearest') or interpolate:

ts2.reindex(ts.index).fillna(method="ffill")
# 2000-01-03    1.587551
# 2000-01-04    1.587551
# 2000-01-05    1.587551
# 2000-01-06   -0.473532
# 2000-01-07   -0.473532
# 2000-01-08   -0.473532
# 2000-01-09    1.917432
# 2000-01-10    1.917432
# Freq: D, dtype: float64

# reindex() will raise a ValueError if the index is not monotonically increasing or decreasing. 
# fillna() and interpolate() will not perform any checks on the order of the index.

#%% Limits on filling while reindexing
# The limit and tolerance arguments provide additional control over filling while reindexing. 
# Limit specifies the maximum count of consecutive matches:

ts2.reindex(ts.index, method="ffill", limit=1)
# 2000-01-03    1.587551
# 2000-01-04    1.587551
# 2000-01-05         NaN
# 2000-01-06   -0.473532
# 2000-01-07   -0.473532
# 2000-01-08         NaN
# 2000-01-09    1.917432
# 2000-01-10    1.917432
# Freq: D, dtype: float64

# In contrast, tolerance specifies the maximum distance between the index and indexer values:
ts2.reindex(ts.index, method="ffill", tolerance="1 day")
# 2000-01-03    1.587551
# 2000-01-04    1.587551
# 2000-01-05         NaN
# 2000-01-06   -0.473532
# 2000-01-07   -0.473532
# 2000-01-08         NaN
# 2000-01-09    1.917432
# 2000-01-10    1.917432
# Freq: D, dtype: float64


# Notice that when used on a DatetimeIndex, TimedeltaIndex or PeriodIndex, 
# tolerance will coerced into a Timedelta if possible. 
# This allows you to specify tolerance with appropriate strings.

# %% Dropping labels from an axis
# A method closely related to reindex is the drop() function. It removes a set of labels from an axis:
df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)
df
# 	one	        two	        three
# a	1.934121	-1.301842	NaN
# b	0.473749	-0.686555	-0.604451
# c	0.882832	-0.447030	-0.987118
# d	NaN	        0.191644	0.193153

df.drop(["a", "d"], axis=0)
#   one	        two	        three
# b	1.297676	-1.460888	-0.865545
# c	1.433992	1.048674	1.194646

df.drop(["one"], axis=1)
# 	two	        three
# a	1.485136	NaN
# b	0.259594	1.021467
# c	-0.119547	-0.196131
# d	0.011754	0.681929

df.reindex(df.index.difference(["a", "d"]))
#   one	        two	        three
# b	0.352059	2.505695	-1.834786
# c	0.461183	0.542281	-0.574149

# %% Renaming / mapping labels
# The rename() method allows you to relabel an axis based on some mapping (a dict or Series) 
# or an arbitrary function.
s
# a   -2.652222
# b   -0.994974
# c   -0.635279
# d   -0.058937
# e    0.404010
# dtype: float64

s.rename(str.upper)
# A   -2.652222
# B   -0.994974
# C   -0.635279
# D   -0.058937
# E    0.404010
# dtype: float64


# %% If you pass a function, it must return a value when called with any of the labels 
# (and must produce a set of unique values). A dict or Series can also be used:
df.rename(
        columns={"one": "foo", "two": "bar"},
        index={"a": "apple", "b": "banana", "d": "durian"},
    )
# 	        foo	        bar	        three
# apple	    -0.975881	0.441712	NaN
# banana	0.352059	2.505695	-1.834786
# c	        0.461183	0.542281	-0.574149
# durian	NaN	        1.602172	1.452904


# %% 
# If the mapping doesn’t include a column/index label, 
# it isn’t renamed. Note that extra labels in the mapping don’t throw an error.

# %% DataFrame.rename() also supports an “axis-style” calling convention, 
# where you specify a single mapper and the axis to apply that mapping to.
df.rename({"one": "foo", "two": "bar"}, axis="columns")
#   foo	        bar	        three
# a	-0.975881	0.441712	NaN
# b	0.352059	2.505695	-1.834786
# c	0.461183	0.542281	-0.574149
# d	NaN	        1.602172	1.452904

df.rename({"a": "apple", "b": "banana", "d": "durian"}, axis="index")
# 	        one	        two	        three
# apple	    -0.975881	0.441712	NaN
# banana	0.352059	2.505695	-1.834786
# c	        0.461183	0.542281	-0.574149
# durian	NaN	        1.602172	1.452904



# %% 
# The rename() method also provides an inplace named parameter 
# that is by default False and copies the underlying data. Pass inplace=True to rename the data in place.
# Finally, rename() also accepts a scalar or list-like for altering the Series.name attribute.
s
# a   -2.652222
# b   -0.994974
# c   -0.635279
# d   -0.058937
# e    0.404010
# dtype: float64

s.rename("scalar-name")
# a   -2.652222
# b   -0.994974
# c   -0.635279
# d   -0.058937
# e    0.404010
# Name: scalar-name, dtype: float64

# %% multiindex rename
# The methods DataFrame.rename_axis() and Series.rename_axis() allow specific names of a MultiIndex 
# to be changed (as opposed to the labels).
df = pd.DataFrame(
        {"x": [1, 2, 3, 4, 5, 6], "y": [10, 20, 30, 40, 50, 60]},
        index=pd.MultiIndex.from_product(
            [["a", "b", "c"], [1, 2]], names=["let", "num"]
        ),
    )
df
# 	    x	y
#       let	num		
# a	1	1	10
#   2	2	20
# b	1	3	30
#   2	4	40
# c	1	5	50
#   2	6	60


df.rename_axis(index={"let": "abc"})
# 	    x	y
#abc num		
# a	1	1	10
#   2	2	20
# b	1	3	30
#   2	4	40
# c	1	5	50
#   2	6	60


df.rename_axis(index={"num": "cba"})
# 		x	y
#let cba		
# a	1	1	10
#   2	2	20
# b	1	3	30
#   2	4	40
# c	1	5	50
#   2	6	60

df.rename_axis(index=str.upper)
# 	    x	y
#LET NUM		
# a	1	1	10
#   2	2	20
# b	1	3	30
#   2	4	40
# c	1	5	50
#   2	6	60

