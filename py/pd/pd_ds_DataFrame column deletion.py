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
# 删除列: del / pop
del df1["two"]
three = df1.pop("three")
df1

# 	one	flag
# a	1.0	False
# b	2.0	False
# c	3.0	True
# d	NaN	False

three
# a    1.0
# b    4.0
# c    9.0
# d    NaN
# Name: three, dtype: float64




#%%
# 删除列：drop配合列名

df1 = df1.drop(["one"], axis=1)             # drop不会就地修改，创建副本返回
df1
# two	three	flag
# a	1.0	1.0	    False
# b	2.0	4.0	    False
# c	3.0	9.0	    True
# d	4.0	NaN	    False

df1.drop(['three'], axis=1, inplace=True)      # inplace=True会就地修改
df1
# 	two	flag
# a	1.0	False
# b	2.0	False
# c	3.0	True
# d	4.0	False




# %%
# 删除列：drop配合列号

df1["one"] = df1["two"]
df1["thr"] = df1["one"]*df1["two"]
df1["foo"] = df1["one"]>2
#   two	flag	one	thr	    foo
# a	1.0	False	1.0	1.0	    False
# b	2.0	False	2.0	4.0	    False
# c	3.0	True	3.0	9.0	    True
# d	4.0	False	4.0	16.0	True

df1.columns[0]
# 'two'

df1.drop(df1.columns[0], axis=1, inplace=True)       # 删除第1列
#   flag	one	thr	foo
# a	False	1.0	1.0	False
# b	False	2.0	4.0	False
# c	True	3.0	9.0	True
# d	False	4.0	16.0	True

df.drop(df.columns[0:3], axis=1, inplace=True)     # 删除前3列
# 	foo
# a	False
# b	False
# c	True
# d	True

df1.drop(df1.columns[[0, 2]], axis=1, inplace=True)  # 删除第1第3列

