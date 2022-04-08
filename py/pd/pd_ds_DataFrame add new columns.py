#%%
import numpy as np
import pandas as pd

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    }

df1 = pd.DataFrame(d)
df1["three"] = df1["one"] * df1["two"]
df1["flag"] = df1["one"] > 2
df1

# 	one	two	three	flag
# a	1.0	1.0	1.0	    False
# b	2.0	2.0	4.0	    False
# c	3.0	3.0	9.0	    True
# d	NaN	4.0	NaN	    False

# %%
# When inserting a scalar value, it will naturally be propagated to fill the column:
df1["foo"] = "bar"
df1
# one	two	three	flag	foo
# a	1.0	1.0	1.0	    False	bar
# b	2.0	2.0	4.0	    False	bar
# c	3.0	3.0	9.0	    True	bar
# d	NaN	4.0	NaN	    False	bar



# %%
# When inserting a Series that does not have the same index as the DataFrame, 
# it will be conformed to the DataFrame’s index:

df1["one"][:2]
# a    1.0
# b    2.0
# Name: one, dtype: float64
# Name: one_trunc, dtype: float64


df1["one_trunc"] = df1["one"][:2]
df1
# one	two	three	flag	foo	one_trunc
# a	1.0	1.0	1.0	    False	bar	1.0
# b	2.0	2.0	4.0	    False	bar	2.0
# c	3.0	3.0	9.0	    True	bar	NaN
# d	NaN	4.0	NaN	    False	bar	NaN



# %%
# You can insert raw ndarrays but their length must match the length of the DataFrame’s index.

# By default, columns get inserted at the end. 
# The insert function is available to insert at a particular location in the columns:

df1.insert(1,"bar", df1["one"])
# df1
# 	one	bar	two	three	flag	foo	one_trunc
# a	1.0	1.0	1.0	1.0 	False	bar	1.0
# b	2.0	2.0	2.0	4.0	    False	bar	2.0
# c	3.0	3.0	3.0	9.0	    True	bar	NaN
# d	NaN	NaN	4.0	NaN	    False	bar	Na


# DataFrame.insert(loc, column, value, allow_duplicates=False)
# insert column into DataFrame at specified location.
# Raises a ValueError if column is already contained in the DataFrame, 
# unless allow_duplicates is set to True.



# %%
# DataFrame has an assign() method that allows you to easily create new columns 
# that are potentially derived from existing columns.
# assign always returns a copy of the data, leaving the original DataFrame untouched.

df1.assign(sepal_ratio=df1["one"] / df1["two"])
#   one	two	three	flag	sepal_ratio
# a	1.0	1.0	1.0	    False	1.0
# b	2.0	2.0	4.0	    False	1.0
# c	3.0	3.0	9.0	    True	1.0
# d	NaN	4.0	NaN	    False	NaN


df1.assign(sepal_ratio2=lambda x: (x["one"] / x["two"]))
# 	one	two	three	flag	sepal_ratio2
# a	1.0	1.0	1.0	    False	1.0
# b	2.0	2.0	4.0	    False	1.0
# c	3.0	3.0	9.0	    True	1.0
# d	NaN	4.0	NaN	    False	NaN



#%%
# 当您手边没有对DataFrame的引用时，传递一个callable而不是要插入的实际值是很有用的。
# assign在一系列操作中使用时很常见。
# 例如，我们可以将DataFrame限制为Sepal Length大于5的那些观测值，计算比率并绘制：
(
   df1.query("two <= 3")
   .assign(
        SepalRatio=lambda x: x.one / x.two,
        PetalRatio=lambda x: x.one / x.three,
   )
   .plot(kind="scatter", x="SepalRatio", y="PetalRatio")
)

df1.query("two <= 3")
# one	two	three	flag
# a	1.0	1.0	1.0	False
# b	2.0	2.0	4.0	False
# c	3.0	3.0	9.0	True

df1.query("two <= 3")
   .assign(
        SepalRatio=lambda x: x.one / x.two,
        PetalRatio=lambda x: x.one / x.three,
   )
#   one two	three	flag	SepalRatio	PetalRatio
# a	1.0	1.0	1.0	    False	1.0	    1.000000
# b	2.0	2.0	4.0	    False	1.0	    0.500000
# c	3.0	3.0	9.0	    True	1.0	    0.333333

# 上述操作中只在临时的副本中产生了x,y两个字段，原本中没有实际数值插入。



# %%
dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# 	A	B
# 0	1	4
# 1	2	5
# 2	3	6

dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])
# 	A	B	C	D
# 0	1	4	5	6
# 1	2	5	7	9
# 2	3	6	9	12



# %%
