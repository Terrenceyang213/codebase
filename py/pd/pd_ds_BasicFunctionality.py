#%%
index = pd.date_range("1/1/2000", periods=8)
# DatetimeIndex(['2000-01-01',
#                '2000-01-02',
#                '2000-01-03',
#                '2000-01-04',
#                '2000-01-05',
#                '2000-01-06',
#                '2000-01-07',
#                '2000-01-08'],
#               dtype='datetime64[ns]', freq='D')

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
# a    0.833348
# b    0.493236
# c   -0.675634
# d   -1.194484
# e    1.680506
# dtype: float64

df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
# 	            A	        B	        C
# 2000-01-01	-0.281538	-1.045262	-0.994248
# 2000-01-02	0.322001	2.035505	-0.835076
# 2000-01-03	-0.053428	-0.370241	-0.782967
# 2000-01-04	-1.921556	0.146207	-0.268431
# 2000-01-05	-0.389671	0.686339	-0.492837
# 2000-01-06	0.878126	-0.431972	0.867529
# 2000-01-07	1.764296	0.223925	-0.307580
# 2000-01-08	1.247205	-0.428400	-0.839825

# %% Head and tail
long_series = pd.Series(np.random.randn(1000))
# 0      0.801595
# 1     -0.557119
# 2      0.379259
# 3     -0.205530
# 4     -1.555741
#          ...   
# 995   -0.849836
# 996    0.555044
# 997    0.074653
# 998    1.748515
# 999   -0.816404
# Length: 1000, dtype: float64

long_series.head()
# 0    0.801595
# 1   -0.557119
# 2    0.379259
# 3   -0.205530
# 4   -1.555741
# dtype: float64

long_series.tail(3)
# 997    0.074653
# 998    1.748515
# 999   -0.816404
# dtype: float64




# %% Attributes and underlying data
# pandas objects have a number of attributes enabling you to access the metadata
#   shape: gives the axis dimensions of the object, consistent with ndarray
#   Axis labels:
#       Series: index (only axis)
#       DataFrame: index (rows) and columns

index.shape     #(8,)
s.shape         #(5,)
df.shape        #(8, 3)

s.index         #label
df.index        #row label
df.columns      #column label

df[:2]
#               A	        B   	    C
# 2000-01-01	-0.281538	-1.045262	-0.994248
# 2000-01-02	0.322001	2.035505	-0.835076

df.columns
# Index(['A',
#        'B',
#        'C'],
#       dtype='object')

df.columns = [x.lower() for x in df.columns]
df.head(3)
#               a	        b	        c
# 2000-01-01	0.616500	0.919208	-0.765728
# 2000-01-02	-0.008712	-1.329322	-0.094411
# 2000-01-03	-1.397970	-1.190174	-2.096755




# %% To get the actual data inside a Index or Series, use the .array property

# pandas objects (Index, Series, DataFrame) can be thought of as containers for arrays, 
# which hold the actual data and do the actual computation. 
# For many types, the underlying array is a numpy.ndarray. 
# However, pandas and 3rd party libraries 
# may extend NumPy’s type system to add support for custom arrays (see dtypes).

s.array #这个返回的是精确的数值，s直接返回的是有截取的数值。
# <PandasArray>
# [  -1.671448960690658,
#    1.8103168332896575,
#    0.8962154773886986,
#  -0.00431447056631793,
#   0.05505989735250155]
# Length: 5, dtype: float64

s.index.array
# <PandasArray>
# ['a',
#  'b',
#  'c',
#  'd',
#  'e']
# Length: 5, dtype: object

# array will always be an ExtensionArray.





# %% If you know you need a NumPy array, use to_numpy() or numpy.asarray().
# Series 使用这个是没问的。
s.to_numpy()
# array([-1.67144896,  1.81031683,  0.89621548, -0.00431447,  0.0550599 ])

np.asarray(s)
# array([-1.67144896,  1.81031683,  0.89621548, -0.00431447,  0.0550599 ])

# array返回的精度要小于ExtensionArray




# %% DataFrame中可以包含带时区的日期时间，to_numpy如何处理。
# numpy中没有dtype可以识别带时区的日期时间，可用以下两种方式：
#   An object-dtype numpy.ndarray with Timestamp objects, each with the correct tz
#   A datetime64[ns] -dtype numpy.ndarray, where the values have been converted to UTC 
#       and the timezone discarded

ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))
# 0   2000-01-01 00:00:00+01:00
# 1   2000-01-02 00:00:00+01:00
# dtype: datetime64[ns, CET]

ser.to_numpy(dtype=object)
# array([Timestamp('2000-01-01 00:00:00+0100', tz='CET', freq='D'),
#        Timestamp('2000-01-02 00:00:00+0100', tz='CET', freq='D')],
#       dtype=object)

ser.to_numpy(dtype="datetime64[ns]")
# array(['1999-12-31T23:00:00.000000000', '2000-01-01T23:00:00.000000000'],
    #   dtype='datetime64[ns]')




# %%
# 从DataFrame中获取底层数据(Raw Data)更加复杂
# 如果是单一的数据类型

df.to_numpy()
# array([[ 0.61649967,  0.91920831, -0.76572789],
#        [-0.00871228, -1.32932158, -0.09441114],
#        [-1.39797032, -1.19017445, -2.09675532],
#        [-0.11476329, -1.67720891,  0.85795822],
#        [-0.40084123, -0.87541749,  0.10081511],
#        [-1.25144903,  0.82932813, -0.81152576],
#        [ 0.36959386, -0.47090405, -0.2275912 ],
#        [-0.78426252, -1.83768936, -0.35130934]])


# If a DataFrame contains homogeneously-typed data, 
# the ndarray can actually be modified in-place, 
# and the changes will be reflected in the data structure. For heterogeneous data 
# (e.g. some of the DataFrame’s columns are not all the same dtype), 
# this will not be the case. 
# The values attribute itself, unlike the axis labels, cannot be assigned to.


# When working with heterogeneous data, 
# the dtype of the resulting ndarray will be chosen to accommodate all of the data involved. 
# For example, if strings are involved, the result will be of object dtype. 
# If there are only floats and integers, the resulting array will be of float dtype.


# In the past, pandas recommended Series.values or DataFrame.values 
# for extracting the data from a Series or DataFrame. 
# You’ll still find references to these in old code bases and online. 
# Going forward, we recommend avoiding .values and using .array or .to_numpy(). 

# .values has the following drawbacks:
#   1 When your Series contains an extension type, 
#       it’s unclear whether Series.values returns a NumPy array or the extension array. 
#       Series.array will always return an ExtensionArray, and will never copy data. 
#       Series.to_numpy() will always return a NumPy array, 
#       potentially at the cost of copying / coercing values.

#   2 When your DataFrame contains a mixture of data types, 
#       DataFrame.values may involve copying data and coercing values to a common dtype, 
#       a relatively expensive operation. 
#       DataFrame.to_numpy(), being a method, makes it clearer 
#       that the returned NumPy array may not be a view on the same data in the DataFrame.
