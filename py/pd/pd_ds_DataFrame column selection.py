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
# 	one	two
# a	1.0	1.0
# b	2.0	2.0
# c	3.0	3.0
# d	NaN	4.0



# %%
df1["one"]
# a    1.0
# b    2.0
# c    3.0
# d    NaN
# Name: one, dtype: float64


# %%
df1["three"] = df1["one"] * df1["two"]
df1

#   one	two	three
# a	1.0	1.0	1.0
# b	2.0	2.0	4.0
# c	3.0	3.0	9.0
# d	NaN	4.0	NaN

# %%
df1["flag"] = df1["one"] > 2
df1
#   one	two	three	flag
# a	1.0	1.0	1.0	False
# b	2.0	2.0	4.0	False
# c	3.0	3.0	9.0	True
# d	NaN	4.0	NaN	False

# %% Selecting columns based on dtype
# The select_dtypes() method implements subsetting of columns based on their dtype.

df = pd.DataFrame(
        {
            "string": list("abc"),
            "int64": list(range(1, 4)),
            "uint8": np.arange(3, 6).astype("u1"),
            "float64": np.arange(4.0, 7.0),
            "bool1": [True, False, True],
            "bool2": [False, True, False],
            "dates": pd.date_range("now", periods=3),
            "category": pd.Series(list("ABC")).astype("category"),
        }
    )

# 	string	int64	uint8	float64	bool1	bool2	dates	                    category
# 0	a	    1	    3	    4.0	    True	False	2021-05-04 02:52:58.596856	A
# 1	b	    2	    4	    5.0	    False	True	2021-05-05 02:52:58.596856	B
# 2	c	    3	    5	    6.0	    True	False	2021-05-06 02:52:58.596856	C

df["tdeltas"] = df.dates.diff()
df["uint64"] = np.arange(3, 6).astype("u8")
df["other_dates"] = pd.date_range("20130101", periods=3)
df["tz_aware_dates"] = pd.date_range("20130101", periods=3, tz="US/Eastern")

df
#   string	int64	uint8	float64	bool1	bool2	dates	                    category	tdeltas	uint64	other_dates	tz_aware_dates
# 0	a	    1	    3	    4.0	    True	False	2021-05-04 03:00:15.349170	A	        NaT	    3	    2013-01-01	2013-01-01 00:00:00-05:00
# 1	b	    2	    4	    5.0	    False	True	2021-05-05 03:00:15.349170	B	        1 days	4	    2013-01-02	2013-01-02 00:00:00-05:00
# 2	c	    3	    5	    6.0	    True	False	2021-05-06 03:00:15.349170	C	        1 days	5	    2013-01-03	2013-01-03 00:00:00-05:00

df.dtypes
# string                                object
# int64                                  int64
# uint8                                  uint8
# float64                              float64
# bool1                                   bool
# bool2                                   bool
# dates                         datetime64[ns]
# category                            category
# tdeltas                      timedelta64[ns]
# uint64                                uint64
# other_dates                   datetime64[ns]
# tz_aware_dates    datetime64[ns, US/Eastern]
# dtype: object


# select_dtypes() has two parameters include and exclude 
# that allow you to say “give me the columns with these dtypes” (include) 
# and/or “give the columns without these dtypes” (exclude).

df.select_dtypes(include=[bool])
# bool1	bool2
# 0	True	False
# 1	False	True
# 2	True	False

# You can also pass the name of a dtype in the NumPy dtype hierarchy:
df.select_dtypes(include=["bool"])
#   bool1  bool2
# 0   True  False
# 1  False   True
# 2   True  False

# select_dtypes() also works with generic dtypes as well.
# For example, to select all numeric and boolean columns while excluding unsigned integers:

df.select_dtypes(include=["number", "bool"], exclude=["unsignedinteger"])
# 	int64	float64	bool1	bool2	tdeltas
# 0	1	    4.0	    True	False	NaT
# 1	2	    5.0	    False	True	1 days
# 2	3	    6.0	    True	False	1 days


# To select string columns you must use the object dtype:
df.select_dtypes(include=["object"])
# 	string
# 0	a
# 1	b
# 2	c


# To see all the child dtypes of a generic dtype like numpy.number 
# you can define a function that returns a tree of child dtypes:
def subdtypes(dtype):
    subs = dtype.__subclasses__()
    if not subs:
        return dtype
    return [dtype, [subdtypes(dt) for dt in subs]]

# All NumPy dtypes are subclasses of numpy.generic:
subdtypes(np.generic)
# [numpy.generic,
#  [[numpy.number,
#    [[numpy.integer,
#      [[numpy.signedinteger,
#        [numpy.int8,
#         numpy.int16,
#         numpy.intc,
#         numpy.int32,
#         numpy.int64,
#         numpy.timedelta64]],
#       [numpy.unsignedinteger,
#        [numpy.uint8, numpy.uint16, numpy.uintc, numpy.uint32, numpy.uint64]]]],
#     [numpy.inexact,
#      [[numpy.floating,
#        [numpy.float16, numpy.float32, numpy.float64, numpy.longdouble]],
#       [numpy.complexfloating,
#        [numpy.complex64, numpy.complex128, numpy.clongdouble]]]]]],
#   [numpy.flexible,
#    [[numpy.character, [numpy.bytes_, numpy.str_]],
#     [numpy.void, [numpy.record]]]],
#   numpy.bool_,
#   numpy.datetime64,
#   numpy.object_]]

# pandas also defines the types category, and datetime64[ns, tz], 
# which are not integrated into the normal NumPy hierarchy and won’t show up with the above function.