# tags:pandas dtypes,pd dtypes
# tags:pandas 类型,pd 类型

#%%
# For the most part, pandas uses NumPy arrays and dtypes for Series or individual columns of a DataFrame. 
# NumPy provides support for float, int, bool, timedelta64[ns] and datetime64[ns] (note that NumPy does not support timezone-aware datetimes).

# pandas and third-party libraries extend NumPy’s type system in a few places. 
# This section describes the extensions pandas has made internally. 
# See Extension types for how to write your own extension that works with pandas. 
# See Extension data types for a list of third-party libraries that have implemented an extension.

# The following table lists all of pandas extension types. 
# For methods requiring dtype arguments, strings can be specified as indicated. 
# See the respective documentation sections for more on each type.


# pandas has two ways to store strings.
    # object dtype, which can hold any Python object, including strings.
    # StringDtype, which is dedicated to strings.

# Finally, arbitrary objects may be stored using the object dtype, 
# but should be avoided to the extent possible 
# (for performance and interoperability with other libraries and methods. See object conversion).


#%% A convenient dtypes attribute for DataFrame returns a Series with the data type of each column.
dft = pd.DataFrame(
        {
            "A": np.random.rand(3),
            "B": 1,
            "C": "foo",
            "D": pd.Timestamp("20010102"),
            "E": pd.Series([1.0] * 3).astype("float32"),
            "F": False,
            "G": pd.Series([1] * 3, dtype="int8"),
        }
    )
dft
# 	A	B	C	D	E	F	G
# 0	0.415656	1	foo	2001-01-02	1.0	False	1
# 1	0.901877	1	foo	2001-01-02	1.0	False	1
# 2	0.188307	1	foo	2001-01-02	1.0	False	1

dft.dtypes
# A           float64
# B             int64
# C            object
# D    datetime64[ns]
# E           float32
# F              bool
# G              int8
# dtype: object

# On a Series object, use the dtype attribute.
dft["A"].dtype
# dtype('float64')

# %% If a pandas object contains data with multiple dtypes in a single column, 
# the dtype of the column will be chosen to accommodate all of the data types 
# (object is the most general).
pd.Series([1, 2, 3, 4, 5, 6.0])
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# 5    6.0
# dtype: float64

pd.Series([1, 2, 3, 6.0, "foo"])
# 0      1
# 1      2
# 2      3
# 3      6
# 4    foo
# dtype: object

# 不同长度的pd.Series组成DataFrame会被Nan补全，标量会被直接广播成最长的Series。

#%%The number of columns of each type in a DataFrame can be found by calling DataFrame.dtypes.value_counts().
 dft.dtypes.value_counts()

# bool              1
# float64           1
# int8              1
# int64             1
# object            1
# float32           1
# datetime64[ns]    1
# dtype: int64

# %% 
# Numeric dtypes will propagate and can coexist in DataFrames. 
# If a dtype is passed (either directly via the dtype keyword, a passed ndarray, or a passed Series), then it will be preserved in DataFrame operations. 
# Furthermore, different numeric dtypes will NOT be combined. The following example will give you a taste.
df1 = pd.DataFrame(np.random.randn(8, 1), columns=["A"], dtype="float32")
df1
# 	A
# 0	0.378470
# 1	1.087833
# 2	-0.092000
# 3	1.090796
# 4	-0.731623
# 5	-0.005113
# 6	1.212457
# 7	-0.534693

df1.dtypes
# A    float32
# dtype: object


df2 = pd.DataFrame(
        {
            "A": pd.Series(np.random.randn(8), dtype="float16"),
            "B": pd.Series(np.random.randn(8)),
            "C": pd.Series(np.array(np.random.randn(8), dtype="uint8")),
        }
    )

df2
# 	A	        B	        C
# 0	0.479492	1.669035	0
# 1	0.375244	-1.289589	0
# 2	-1.141602	2.575414	255
# 3	1.302734	0.449497	0
# 4	-1.208984	0.653877	0
# 5	0.065796	-0.029874	0
# 6	0.903809	0.539710	0
# 7	-0.154175	-0.500695	0

df2.dtypes
# A    float16
# B    float64
# C      uint8
# dtype: object

#%%defaults
# By default integer types are int64 and float types are float64, regardless of platform (32-bit or 64-bit). The following will all result in int64 dtypes.

pd.DataFrame([1, 2], columns=["a"]).dtypes
# a    int64
# dtype: object

pd.DataFrame({"a": [1, 2]}).dtypes
# a    int64
# dtype: object

pd.DataFrame({"a": 1}, index=list(range(2))).dtypes
# a    int64
# dtype: object

# Note that Numpy will choose platform-dependent types when creating arrays. The following WILL result in int32 on 32-bit platform.
pd.DataFrame(np.array([1, 2])).dtypes
# 0    int32
# dtype: object

# %%
# Types can potentially be upcasted when combined with other types, meaning they are promoted from the current type (e.g. int to float).

df1
# 	A
# 0	0.306202
# 1	0.957222
# 2	-1.026048
# 3	-0.409716
# 4	-0.878180
# 5	-0.052225
# 6	-1.360475
# 7	1.578334

df2
# 	A	        B	        C
# 0	0.936035	-0.158697	1
# 1	-0.694336	-0.201650	0
# 2	-0.076111	-0.719229	0
# 3	-0.560059	0.309199	0
# 4	2.460938	0.566153	1
# 5	0.001599	0.356473	0
# 6	0.428711	-0.047542	0
# 7	-1.880859	0.418634	0

df1.reindex_like(df2)
# 	A	        B	C
# 0	0.306202	NaN	NaN
# 1	0.957222	NaN	NaN
# 2	-1.026048	NaN	NaN
# 3	-0.409716	NaN	NaN
# 4	-0.878180	NaN	NaN
# 5	-0.052225	NaN	NaN
# 6	-1.360475	NaN	NaN
# 7	1.578334	NaN	NaN

df1.reindex_like(df2).fillna(value=0.0)
# 	A	        B	C
# 0	0.306202	0.0	0.0
# 1	0.957222	0.0	0.0
# 2	-1.026048	0.0	0.0
# 3	-0.409716	0.0	0.0
# 4	-0.878180	0.0	0.0
# 5	-0.052225	0.0	0.0
# 6	-1.360475	0.0	0.0
# 7	1.578334	0.0	0.0


df3 = df1.reindex_like(df2).fillna(value=0.0) + df2
# 	A	        B	        C
# 0	1.242237	-0.158697	1.0
# 1	0.262886	-0.201650	0.0
# 2	-1.102159	-0.719229	0.0
# 3	-0.969775	0.309199	0.0
# 4	1.582757	0.566153	1.0
# 5	-0.050626	0.356473	0.0
# 6	-0.931764	-0.047542	0.0
# 7	-0.302525	0.418634	0.0

df3.dtypes
# A    float32
# B    float64
# C    float64
# dtype: object

# DataFrame.to_numpy() will return the lower-common-denominator of the dtypes, 
# meaning the dtype that can accommodate ALL of the types in the resulting homogeneous dtyped NumPy array. This can force some upcasting.
df3.to_numpy().dtype
# dtype('float64')


df3.astype("float32").dtypes
# A    float32
# B    float32
# C    float32
# dtype: object


# Convert a subset of columns to a specified type using astype().
dft = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
# 	a	b	c
# 0	1	4	7
# 1	2	5	8
# 2	3	6	9

dft[["a", "b"]] = dft[["a", "b"]].astype(np.uint8)
dft.dtypes
# a    uint8
# b    uint8
# c    int64
# dtype: object

#%%  convert dtype
# Convert certain columns to a specific dtype by passing a dict to astype().
dft1 = pd.DataFrame({"a": [1, 0, 1], "b": [4, 5, 6], "c": [7, 8, 9]})
# 	a	b	c
# 0	1	4	7
# 1	0	5	8
# 2	1	6	9

dft1 = dft1.astype({"a": np.bool_, "c": np.float64})
# 	a	    b	c
# 0	True	4	7.0
# 1	False	5	8.0
# 2	True	6	9.0

dft1.dtypes
# a       bool
# b      int64
# c    float64
# dtype: object

# %% loc & astype will tiger upcasting
# When trying to convert a subset of columns to a specified type using astype() and loc(), upcasting occurs.

# loc() tries to fit in what we are assigning to the current dtypes, 
# while [] will overwrite them taking the dtype from the right hand side. 
# Therefore the following piece of code produces the unintended result.

dft = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
# a    int64
# b    int64
# c    int64
# dtype: object

dft.loc[:, ["a", "b"]].astype(np.uint8).dtypes
# a    uint8
# b    uint8
# dtype: object

dft.loc[:, ["a", "b"]] = dft.loc[:, ["a", "b"]].astype(np.uint8)
dft.dtypes
# a    int64
# b    int64
# c    int64
# dtype: object


#%% object conversion
# pandas offers various functions to try to force conversion of types from the object dtype to other types. 
# In cases where the data is already of the correct type, but stored in an object array, 
# the DataFrame.infer_objects() and Series.infer_objects() methods can be used to soft convert to the correct type.

import datetime

df = pd.DataFrame(
        [
            [1, 2],
            ["a", "b"],
            [datetime.datetime(2016, 3, 2), datetime.datetime(2016, 3, 2)],
        ]
    )
    
# 	0	1
# 0	1	2
# 1	a	b
# 2	2016-03-02 00:00:00	2016-03-02 00:00:00

df.T
# 	0	1	2
# 0	1	a	2016-03-02
# 1	2	b	2016-03-02

df.T.dtypes
# 0            object
# 1            object
# 2    datetime64[ns]
# dtype: object

# Because the data was transposed the original inference stored all columns as object, which infer_objects will correct.
df.T.infer_objects().dtypes
# 0             int64
# 1            object
# 2    datetime64[ns]
# dtype: object

# %%  The following functions are available for one dimensional object arrays or scalars to perform hard conversion of objects to a specified type:
# to_numeric() (conversion to numeric dtypes)

m = ["1.1", 2, 3]
pd.to_numeric(m)
# array([1.1, 2. , 3. ])

# to_datetime() (conversion to datetime objects)
import datetime
m = ["2016-07-09", datetime.datetime(2016, 3, 2)]
pd.to_datetime(m)
# DatetimeIndex(['2016-07-09', '2016-03-02'], dtype='datetime64[ns]', freq=None)

# to_timedelta() (conversion to timedelta objects)
m = ["5us", pd.Timedelta("1day")]
pd.to_timedelta(m)
# TimedeltaIndex(['0 days 00:00:00.000005', '1 days 00:00:00'], dtype='timedelta64[ns]', freq=None)

# %% 
# To force a conversion, we can pass in an errors argument, 
# which specifies how pandas should deal with elements that cannot be converted to desired dtype or object. 
# By default, errors='raise', meaning that any errors encountered will be raised during the conversion process. 
# However, if errors='coerce', these errors will be ignored  and pandas will convert problematic elements to pd.NaT (for datetime and timedelta) or np.nan (for numeric). 
# This might be useful if you are reading in data which is mostly of the desired dtype (e.g. numeric, datetime), 
# but occasionally has non-conforming elements intermixed that you want to represent as missing:

import datetime

m = ["apple", datetime.datetime(2016, 3, 2)]
pd.to_datetime(m, errors="coerce")
# DatetimeIndex(['NaT', '2016-03-02'], dtype='datetime64[ns]', freq=None)


m = ["apple", 2, 3]
pd.to_numeric(m, errors="coerce")
# array([nan,  2.,  3.])

m = ["apple", pd.Timedelta("1day")]
pd.to_timedelta(m, errors="coerce")
# TimedeltaIndex([NaT, '1 days'], dtype='timedelta64[ns]', freq=None)

# %% 
# The errors parameter has a third option of errors='ignore', 
# which will simply return the passed in data 
# if it encounters any errors with the conversion to a desired data type:

import datetime
m = ["apple", datetime.datetime(2016, 3, 2)]
pd.to_datetime(m, errors="ignore")
# Index(['apple', 2016-03-02 00:00:00], dtype='object')

m = ["apple", 2, 3]
pd.to_numeric(m, errors="ignore")
# array(['apple', 2, 3], dtype=object)

m = ["apple", pd.Timedelta("1day")]
pd.to_timedelta(m, errors="ignore")
# array(['apple', Timedelta('1 days 00:00:00')], dtype=object)


# %%  In addition to object conversion, to_numeric() provides another argument downcast, which gives the option of downcasting the newly (or already) numeric data to a smaller dtype, which can conserve memory:
m = ["1", 2, 3]
pd.to_numeric(m, downcast="integer") # smallest signed int dtype
# array([1, 2, 3], dtype=int8)

pd.to_numeric(m, downcast="signed") # same as 'integer'
# array([1, 2, 3], dtype=int8)

pd.to_numeric(m, downcast="unsigned") # smallest unsigned int dtype
# array([1, 2, 3], dtype=uint8)

pd.to_numeric(m, downcast="float") # smallest float dtype
# array([1., 2., 3.], dtype=float32)

#%% dtype conversion with DataFrame: apply
# As these methods apply only to one-dimensional arrays, lists or scalars; they cannot be used directly on multi-dimensional objects such as DataFrames. However, with apply(), we can “apply” the function over each column efficiently:

import datetime
df = pd.DataFrame([["2016-07-09", datetime.datetime(2016, 3, 2)]] * 2, dtype="O")
df
#  	0	        1
# 0	2016-07-09	2016-03-02 00:00:00
# 1	2016-07-09	2016-03-02 00:00:00

df.apply(pd.to_datetime)
# 	0	        1
# 0	2016-07-09	2016-03-02
# 1	2016-07-09	2016-03-02

df = pd.DataFrame([["1.1", 2, 3]] * 2, dtype="O")
# 	0	1	2
# 0	1.1	2	3
# 1	1.1	2	3

df.apply(pd.to_numeric)
# 	0	1	2
# 0	1.1	2	3
# 1	1.1	2	3

df = pd.DataFrame([["5us", pd.Timedelta("1day")]] * 2, dtype="O")
df
# 	0	1
# 0	5us	1 days 00:00:00
# 1	5us	1 days 00:00:00

df.apply(pd.to_timedelta)
# 	0	                    1
# 0	0 days 00:00:00.000005	1 days
# 1	0 days 00:00:00.000005	1 days


# %% gotchas
# Performing selection operations on integer type data can easily upcast the data to floating. The dtype of the input data will be preserved in cases where nans are not introduced. See also Support for integer NA.

dfi = df3.astype("int32")
dfi
# 	A	B	C
# 0	1	0	1
# 1	0	0	0
# 2	-1	0	0
# 3	0	0	0
# 4	1	0	1
# 5	0	0	0
# 6	0	0	0
# 7	0	0	0

dfi["E"] = 1
# 	A	B	C	E
# 0	1	0	1	1
# 1	0	0	0	1
# 2	-1	0	0	1
# 3	0	0	0	1
# 4	1	0	1	1
# 5	0	0	0	1
# 6	0	0	0	1
# 7	0	0	0	1

dfi.dtypes
# A    int32
# B    int32
# C    int32
# E    int64
# dtype: object

casted = dfi[dfi > 0]
casted
# 	A	B	C	E
# 0	1.0	NaN	1.0	1
# 1	NaN	NaN	NaN	1
# 2	NaN	NaN	NaN	1
# 3	NaN	NaN	NaN	1
# 4	1.0	NaN	1.0	1
# 5	NaN	NaN	NaN	1
# 6	NaN	NaN	NaN	1
# 7	NaN	NaN	NaN	1

dfi[dfi.A>0] # 注意二者区别
# 	A	B	C	E
# 0	1	0	1	1
# 4	1	0	1	1

casted.dtypes
# A    float64
# B    float64
# C    float64
# E      int64
# dtype: object


# While float dtypes are unchanged.
dfa = df3.copy()

dfa["A"] = dfa["A"].astype("float32")

dfa.dtypes


casted = dfa[df2 > 0]
casted
# 	A	        B	        C
# 0	1.242237	NaN	        1.0
# 1	NaN	        NaN	        NaN
# 2	NaN	        NaN	        NaN
# 3	NaN	        0.309199	NaN
# 4	1.582757	0.566153	1.0
# 5	-0.050626	0.356473	NaN
# 6	-0.931764	NaN	        NaN
# 7	NaN	        0.418634	NaN

casted.dtypes
# A    float32
# B    float64
# C    float64
# dtype: object