#%% 
# There exists a large number of methods for computing descriptive statistics 
# and other related operations on Series, DataFrame. 
# Most of these are aggregations (hence producing a lower-dimensional result) like sum(), mean(), and quantile(), 
# but some of them, like cumsum() and cumprod(), produce an object of the same size. 
# Generally speaking, these methods take an axis argument, just like ndarray.{sum, std, …}, 
# but the axis can be specified by name or integer:
#   Series: no axis argument needed
#   DataFrame: “index” (axis=0, default), “columns” (axis=1) Indicate which axis or axes should be reduced.

import numpy as np
import pandas as pd

# 将Series作为input的参数，广播行为
df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)

#   one	        two	        three
# a	-1.475286	-0.299621	NaN
# b	0.296997	-0.510895	2.029753
# c	-1.231790	-0.855652	0.454500
# d	NaN	        0.049363	0.643194

df.mean(0)
# one     -0.803360
# two     -0.404201
# three    1.042482
# dtype: float64

df.mean(1)
# a    1.682440
# b   -0.694507
# c    0.452549
# d    0.105853
# dtype: float64

#%% skipna option
# All such methods have a skipna option signaling whether to exclude missing data (True by default):
df.sum(axis=0, skipna=False)
# one           NaN
# two      1.939381
# three         NaN
# dtype: float64

df.sum(axis=1, skipna=True)
# a    2.084428
# b   -0.442451
# c    1.491474
# d   -0.239951
# dtype: float64



#%% Combined with the broadcasting / arithmetic behavior 
# Combined with the broadcasting / arithmetic behavior, 
# one can describe various statistical procedures, 
# like standardization (rendering data zero mean and standard deviation of 1), very concisely:

ts_stand = (df - df.mean()) / df.std()
#   one	        two	        three
# a	0.728937	0.055558	NaN
# b	-1.140025	1.392181	-1.084534
# c	0.411088	-0.797261	0.885544
# d	NaN	        -0.650477	0.198990

# DataFrame.mean(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)[source]
# Return the mean of the values over the requested axis.
#   axis:{index (0), columns (1)} Axis for the function to be applied on.


ts_stand.std()
# one      1.0
# two      1.0
# three    1.0
# dtype: float64

xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
#   one	        two	        three
# a	0.707107	-0.707107	NaN
# b	-0.698817	1.145487	-0.446670
# c	0.948944	-1.044234	0.095291
# d	NaN	        -0.707107	0.707107

xs_stand.std(1)
# a    1.0
# b    1.0
# c    1.0
# d    1.0
# dtype: float64

# DataFrame.sub(other, axis='columns', level=None, fill_value=None)
    # axis:{0 or ‘index’, 1 or ‘columns’}
    # Whether to compare by the index (0 or ‘index’) or columns (1 or ‘columns’). 
    # For Series input, axis to match Series index on.

#%% cumsum/sumprod
# Note that methods like cumsum() and cumprod() preserve the location of NaN values. 
# This is somewhat different from expanding() and rolling() 
# since NaN behavior is furthermore dictated by a min_periods parameter.

df
#   one	        two	        three
# a	1.895362	0.189066	NaN
# b	-1.009554	1.265606	-0.698502
# c	1.401331	-0.497810	0.587953
# d	NaN	        -0.379587	0.139635

df.cumsum()
#   one	        two	        three
# a	1.895362	0.189066	NaN
# b	0.885808	1.454672	-0.698502
# c	2.287139	0.956863	-0.110550
# d	NaN	        0.577276	0.029086

df.cumsum(1)
#   one	        two	        three
# a	1.895362	2.084428	NaN
# b	-1.009554	0.256052	-0.442451
# c	1.401331	0.903521	1.491474
# d	NaN	        -0.379587	-0.239951

#%% 
# Function    Description
# count       Number of non-NA observations
# sum         Sum of values
# mean        Mean of values
# mad         Mean absolute deviation
# median      Arithmetic median of values
# min         Minimum
# max         Maximum
# mode        Mode
# abs         Absolute Value
# prod        Product of values
# std         Bessel-corrected sample standard deviation
# var         Unbiased variance
# sem         Standard error of the mean
# skew        Sample skewness (3rd moment)
# kurt        Sample kurtosis (4th moment)
# quantile    Sample quantile (value at %)
# cumsum      Cumulative sum
# cumprod     Cumulative product
# cummax      Cumulative maximum
# cummin      Cumulative minimum

# 这些函数的axis参数指定的是被作用的轴：0-index，1-columns，比如sum
# sum(0)的话是对index使用加总，其结果是用columns name作为index的array
# sum(1)的话是对columns使用加总，结果是用index 作为新的index的array

#注意这些函数与sub，add等函数的axis意义是不同的。这里的axis=1是指按columns进行对比。
dm = df.mean(0)
# one      0.762380
# two      0.144319
# three    0.009695
# dtype: float64

df.add(dm,axis=1) # 只能对df进行逐行的相加。则需要对逐行对比axis=1
#   one	        two	        three
# a	2.657742	0.333385	NaN
# b	-0.247175	1.409925	-0.688807
# c	2.163710	-0.353491	0.597648
# d	NaN	        -0.235268	0.149331

df.add(dm,axis=0) #这样做是逐列对比，label不匹配，结果会出乎意料。
# 	    one	two	three
# a	    NaN	NaN	NaN
# b	    NaN	NaN	NaN
# c	    NaN	NaN	NaN
# d	    NaN	NaN	NaN
# one	NaN	NaN	NaN
# three	NaN	NaN	NaN
# two	NaN	NaN	NaN


#%% np.method:some NumPy methods, like mean, std, and sum, will exclude NAs on Series input by default:
# 但在array上却会包含nan
np.mean(df["one"])
# 0.7623796393461131

np.mean(df["one"].to_numpy())
# nan


# %% Series.unique() 
# will return the number of unique non-NA values in a Series:
series = pd.Series(np.random.randn(500))
series[20:500] = np.nan
series[10:20] = 5
series.nunique()
# 11


#%% describe()
# There is a convenient describe() function which computes a variety of summary statistics about a Series 
# or the columns of a DataFrame (excluding NAs of course):
series = pd.Series(np.random.randn(1000))
series[::2] = np.nan
series.describe()
# count    500.000000
# mean       0.024517
# std        0.941586
# min       -2.396460
# 25%       -0.637291
# 50%        0.036443
# 75%        0.654877
# max        2.907870
# dtype: float64


#%%
frame = pd.DataFrame(np.random.randn(1000, 5), columns=["a", "b", "c", "d", "e"])
frame.iloc[::2] = np.nan
frame.describe()
#       a	        b	        c	        d	        e
# count	500.000000	500.000000	500.000000	500.000000	500.000000
# mean	0.011911	0.027628	-0.042661	-0.000924	-0.023784
# std	1.002740	1.006303	0.979744	0.944107	1.047110
# min	-2.635322	-3.177817	-2.743253	-3.247775	-3.387176
# 25%	-0.711605	-0.661534	-0.700286	-0.635292	-0.752221
# 50%	0.023161	-0.012200	-0.086749	0.056364	0.009044
# 75%	0.736766	0.746985	0.654696	0.662249	0.624030
# max	3.247508	2.666041	2.660304	3.795661	3.133822


# You can select specific percentiles to include in the output:
series.describe(percentiles=[0.05, 0.25, 0.75, 0.95])
# count    500.000000
# mean       0.024517
# std        0.941586
# min       -2.396460
# 5%        -1.487793
# 25%       -0.637291
# 50%        0.036443
# 75%        0.654877
# 95%        1.524194
# max        2.907870
# dtype: float64


# For a non-numerical Series object, describe() will give a simple summary of the number of unique values 
# and most frequently occurring values:
s = pd.Series(["a", "a", "b", "b", "a", "a", np.nan, "c", "d", "a"])
s.describe()
# count     9
# unique    4
# top       a
# freq      5
# dtype: object


# Note that on a mixed-type DataFrame object, 
# describe() will restrict the summary to include only numerical columns or, 
# if none are, only categorical columns:
frame = pd.DataFrame({"a": ["Yes", "Yes", "No", "No"], "b": range(4)})
frame.describe()
#       b
# count	4.000000
# mean	1.500000
# std	1.290994
# min	0.000000
# 25%	0.750000
# 50%	1.500000
# 75%	2.250000
# max	3.000000


# This behavior can be controlled by providing a list of types as include/exclude arguments. 
# The special value all can also be used:
frame.describe(include=["object"])
#           a
# count	    4
# unique	2
# top	    Yes
# freq	    2

frame.describe(include=["number"])
#       b
# count	4.000000
# mean	1.500000
# std	1.290994
# min	0.000000
# 25%	0.750000
# 50%	1.500000
# 75%	2.250000
# max	3.000000

frame.describe(include="all")
#           a	b
# count	    4	4.000000
# unique	2	NaN
# top	    Yes	NaN
# freq	    2	NaN
# mean	    NaN	1.500000
# std	    NaN	1.290994
# min	    NaN	0.000000
# 25%	    NaN	0.750000
# 50%	    NaN	1.500000
# 75%	    NaN	2.250000
# max	    NaN	3.000000

# %% Index of min/max values
s1 = pd.Series(np.random.randn(5))
# 0    0.590577
# 1   -0.774532
# 2    0.717777
# 3   -0.288138
# 4    0.029970
# dtype: float64

s1.idxmin(), s1.idxmax()
# (4, 0)


df1 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
#   A	        B	        C
# 0	0.516521	-1.119324	0.705472
# 1	-0.656740	-0.716302	-0.714804
# 2	0.741136	-2.230926	1.216567
# 3	-0.555118	0.303454	-0.418367
# 4	1.038309	-0.047302	1.379095

df1.idxmin(axis=0) #在index方向上寻求最大值。在列方向上。
# A    3
# B    3
# C    4
# dtype: int64


df1.idxmax(axis=1) #在columns方向上寻求最大值。在行方向上。
# 0    A
# 1    C
# 2    A
# 3    C
# 4    C
# dtype: object


# When there are multiple rows (or columns) matching the minimum or maximum value, 
# idxmin() and idxmax() return the first matching index:
df3 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=["A"], index=list("edcba"))

#   A
# e	2.0
# d	1.0
# c	1.0
# b	3.0
# a	NaN

df3["A"].idxmin()
# 'd'

#%% Value counts (histogramming) / mode
# The value_counts() Series method and top-level function computes a histogram of a 1D array of values. 
# It can also be used as a function on regular arrays:

data = np.random.randint(0, 7, size=50)
s = pd.Series(data)

# pd.value_counts(data)
s.value_counts()
# 5    9
# 1    9
# 0    9
# 2    8
# 4    7
# 6    4
# 3    4
# dtype: int64

# %% The value_counts() method can be used to count combinations across multiple columns. 
# By default all columns are used but a subset can be selected using the subset argument.
data = {"a": [1, 2, 3, 4], "b": ["x", "x", "y", "y"]}
frame = pd.DataFrame(data)
frame.value_counts()
#    a    b
# 4  y    1
# 3  y    1
# 2  x    1
# 1  x    1
# dtype: int64


# Similarly, you can get the most frequently occurring value(s), 
# i.e. the mode, of the values in a Series or DataFrame:
s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
s5.mode()
# 0    3
# 1    7
# dtype: int64

df5 = pd.DataFrame(
    {
    "A": np.random.randint(0, 7, size=10),
    "B": np.random.randint(-10, 15, size=10),
    }
)
# 	A	B
# 0	6	-6
# 1	3	-2
# 2	4	-4
# 3	2	0
# 4	0	-8
# 5	6	-6
# 6	3	14
# 7	2	-9
# 8	3	-4
# 9	3	12

df5.mode() 
# The mode of a set of values is the value that appears most often. 
# It can be multiple values. 返回每一列频率最高的数字。

# 	A	B
# 0	3.0	-6
# 1	NaN	-4
# 这个结果中A，B列要分开看，A列中nan无意义。A列中最频繁的是3，B列中最频繁的是-6，-4.


# %% Discretization and quantiling/ cut()
arr = np.random.randn(20)
# array([ 0.23081747, -0.62635315,  0.34228668, -0.67566446, -0.83923784,
#        -0.8346708 , -0.82830756,  0.53848094,  0.02584404, -0.62551277,
#        -0.49124558, -0.02715545, -1.26577288,  0.78175691,  0.69851957,
#         0.68091892, -1.94799946,  1.54236483, -0.19802713, -0.44593459])

factor = pd.cut(arr, 4)
# [    (-0.663, 0.18], (0.18, 1.022], (-1.508, -0.663], (-1.508, -0.663], (-0.663, 0.18], 
# ..., (-0.663, 0.18], (-1.508, -0.663], (1.022, 1.864], (-0.663, 0.18], (0.18, 1.022]]
# Length: 20
# Categories (4, interval[float64]): [(-1.508, -0.663] < (-0.663, 0.18] < (0.18, 1.022] < (1.022, 1.864]]

factor = pd.cut(arr, 1)
# [    (-1.635, 1.803], (-1.635, 1.803], (-1.635, 1.803], (-1.635, 1.803], (-1.635, 1.803], 
# ..., (-1.635, 1.803], (-1.635, 1.803], (-1.635, 1.803], (-1.635, 1.803], (-1.635, 1.803]]
# Length: 20
# Categories (1, interval[float64]): [(-1.635, 1.803]]

factor1 = pd.cut(arr, [-5, -1, 0, 1, 5])
# [    (1, 5], (0, 1], (0, 1], (-1, 0], (-1, 0], 
# ..., (-1, 0], (-5, -1], (-1, 0], (-5, -1], (0, 1]]
# Length: 20
# Categories (4, interval[int64]): [(-5, -1] < (-1, 0] < (0, 1] < (1, 5]]

# %% qcut() computes sample quantiles.

# For example, we could slice up some normally distributed data into equal-size quartiles like so:
arr = np.random.randn(30)
factor = pd.qcut(arr, [0, 0.25, 0.5, 0.75, 1])
factor
# [    (-1.386, -1.054], (0.765, 2.749], (0.765, 2.749], (-1.054, -0.0211], (0.765, 2.749], 
# ..., (-0.0211, 0.765], (-1.054, -0.0211], (-0.0211, 0.765], (-1.386, -1.054], (-0.0211, 0.765]]
# Length: 30
# Categories (4, interval[float64]): [(-1.386, -1.054] < (-1.054, -0.0211] < (-0.0211, 0.765] < (0.765, 2.749]]

pd.value_counts(factor)
# (0.765, 2.749]       8
# (-1.386, -1.054]     8
# (-0.0211, 0.765]     7
# (-1.054, -0.0211]    7
# dtype: int64

# %% pass infinite values to define the bins:
arr = np.random.randn(20)

factor = pd.cut(arr, [-np.inf, 0, np.inf])

factor
# [    (0.0, inf], (0.0, inf], (-inf, 0.0], (-inf, 0.0], (-inf, 0.0], 
# ..., (0.0, inf], (0.0, inf], (-inf, 0.0], (-inf, 0.0], (-inf, 0.0]]
# Length: 20
# Categories (2, interval[float64]): [(-inf, 0.0] < (0.0, inf]]