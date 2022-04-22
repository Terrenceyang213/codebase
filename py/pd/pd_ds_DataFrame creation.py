#%%
import numpy as np
import pandas as pd


#%%
# Like Series, DataFrame accepts many different kinds of input:
#   Dict of 1D ndarrays, lists, dicts, or Series
#   2-D numpy.ndarray
#   Structured or record ndarray
#   A Series
#   Another DataFrame

# Along with the data, you can optionally pass index (row labels) 
# and columns (column labels) arguments. 

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
#   one	two
# d	NaN	4.0
# b	2.0	2.0
# a	1.0	1.0

df3 = pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])
df3
#	two	three
# d	4.0	NaN
# b	2.0	NaN
# a	1.0	NaN




#%%
# 	one	two
# a	1.0	1.0
# b	2.0	2.0
# c	3.0	3.0
# d	NaN	4.0

df.index
# Index(['a', 'b', 'c', 'd'], dtype='object')

df.columns
# Index(['one', 'two'], dtype='object')

#%%
# create a DataFrame from dict of ndarrays / lists
# The ndarrays must all be the same length. 
# If an index is passed, it must clearly also be the same length as the arrays. 
# If no index is passed, the result will be range(n), where n is the array length.

d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
pd.DataFrame(d)
#	one	two
# 0	1.0	4.0
# 1	2.0	3.0
# 2	3.0	2.0
# 3	4.0	1.0

pd.DataFrame(d, index=["a", "b", "c", "d"])
#	one	two
# a	1.0	4.0
# b	2.0	3.0
# c	3.0	2.0
# d	4.0	1.0

er_d = {"one": [1.0, 2.0, 3.0], "two": [4.0, 3.0, 2.0, 1.0]}
pd.DataFrame(er_d)
# ValueError: arrays must all be same length 




#%%
# Create a DataFrame from structured or record array
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")]) #创建一个空的"模板"
data[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]
pd.DataFrame(data)
#	A	B	C
# 0	1	2.0	b'Hello'
# 1	2	3.0	b'World

pd.DataFrame(data, index=["first", "second"])
#           A	B	C
# first	    1	2.0	b'Hello'
# second	2	3.0	b'World'

pd.DataFrame(data, columns=["C", "A", "B"])
#   C	        A	B
# 0	b'Hello'	1	2.0
# 1	b'World'	2	3.0




#%%
# Create a DataFrame from a list of dict
data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
pd.DataFrame(data2)
#   a	b	c
# 0	1	2	NaN
# 1	5	10	20.0

pd.DataFrame(data2, index=["first", "second"])
#           a	b	c
# first	    1	2	NaN
# second	5	10	20.0

pd.DataFrame(data2, columns=["a", "b"])
# 	    a	b
# 0	    1	2
# 1	    5	10




#%%
# You can automatically create a MultiIndexed frame by passing a tuples dictionary.
pd.DataFrame(
   {
   ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
   ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
   ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
   ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
   ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
   }
   )

#	    a	        b
#       b	a	c	a	b
# A	B	1.0	4.0	5.0	8.0	10.0
#   C	2.0	3.0	6.0	7.0	NaN
#   D	NaN	NaN	NaN	NaN	9.0


# %%
# creating from a Series
# The result will be a DataFrame with the same index as the input Series, 
# and with one column whose name is the original name of the Series 
# (only if no other column name provided).

ser = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"], name = "ser")
pd.DataFrame(ser)
#   ser
# a	0.359214
# b	-1.321570
# c	1.320319
# d	0.303538
# e	1.189191

# %%
# create DataFrame from a list of namedtuples
from collections import namedtuple
Point = namedtuple("Point", "x y")
pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)])
#	x	y
# 0	0	0
# 1	0	3
# 2	2	3

Point3D = namedtuple("Point3D", "x y z")
pd.DataFrame([Point3D(0, 0, 0), Point3D(0, 3, 5), Point(2, 3)])

#    x  y    z
# 0  0  0  0.0
# 1  0  3  5.0
# 2  2  3  NaN

#%%
# create DataFrame from a list of dataclasses


#%%
# from_dict 创建DataFrame
pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]))
#	A	B
# 0	1	4
# 1	2	5
# 2	3	6

# If you pass orient='index', the keys will be the row labels. 
# In this case, you can also pass the desired column names:
pd.DataFrame.from_dict(
   dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]),
        orient="index",
        columns=["one", "two", "three"],
    )

#     one  two  three
# A    1    2      3
# B    4    5      6



# from_records 创建DataFrame
# DataFrame.from_records接受具有结构化dtype的元组或ndarray的列表。
# 它与普通的DataFrame构造函数相似，除了所得的DataFrame索引可能是结构化dtype的特定字段。
data
# array([(1, 2., b'Hello'), (2, 3., b'World')],dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])

pd.DataFrame.from_records(data, index="C")
#           A    B
# C               
# b'Hello'  1  2.0
# b'World'  2  3.0


#%% tags:pandas;pd;create empty dataframe with cols;
MLA_columns = ['MLA Name', 'MLA Parameters','MLA Train Accuracy Mean', 'MLA Test Accuracy Mean', 'MLA Test Accuracy 3*STD' ,'MLA Time']
MLA_compare = pd.DataFrame(columns = MLA_columns)