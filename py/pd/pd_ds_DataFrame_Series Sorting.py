# %% 
# pandas supports three kinds of sorting: 
    # sorting by index labels, 
    # sorting by column values,
    # sorting by a combination of both.

#%% By index
# The Series.sort_index() and DataFrame.sort_index() methods 
# are used to sort a pandas object by its index levels.
df = pd.DataFrame(
        {
            "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
            "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
            "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
        }
    )

#   one	        two	        three
# a	0.522878	-0.586556	NaN
# b	-0.179241	-0.468329	-1.642520
# c	-1.859068	1.154922	-0.400818
# d	NaN	        0.130144	-2.021322

unsorted_df = df.reindex(
        index=["a", "d", "c", "b"], columns=["three", "two", "one"]
)

unsorted_df
#   three	    two	        one
# a	NaN	        -0.586556	0.522878
# d	-2.021322	0.130144	NaN
# c	-0.400818	1.154922	-1.859068
# b	-1.642520	-0.468329	-0.179241

unsorted_df.sort_index()
#   three	    two	        one
# a	NaN	        0.454186	-2.191546
# b	1.249464	-0.721815	1.210183
# c	-0.056308	0.797183	1.091687
# d	0.435734	0.457028	NaN

unsorted_df.sort_index(ascending=False)
#   three	    two	        one
# d	0.309644	-0.329164	NaN
# c	-0.530925	-0.014921	1.328842
# b	2.555009	-1.574941	0.363437
# a	NaN	        0.533025	1.267474

unsorted_df.sort_index(axis=1)
# 	one	        three	    two
# a	1.267474	NaN	        0.533025
# d	NaN	        0.309644	-0.329164
# c	1.328842	-0.530925	-0.014921
# b	0.363437	2.555009	-1.574941

unsorted_df["three"].sort_index()
# a         NaN
# b   -0.675978
# c    0.202532
# d    1.450691
# Name: three, dtype: float64


#%% key parameter
# Sorting by index also supports a key parameter that takes a callable function 
# to apply to the index being sorted. 
# For MultiIndex objects, the key is applied per-level to the levels specified by level.

s1 = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3], "c": [2, 3, 4]}).set_index(
        list("ab")
    )
s1
# 		c
# a	b	
# B	1	2
# a	2	3
# C	3	4

s1.sort_index(level="a")
# 		c
# a	b	
# B	1	2
# C	3	4
# a	2	3

s1.sort_index(level="a", key=lambda idx: idx.str.lower())
# 		c
# a	b	
# a	2	3
# B	1	2
# C	3	4

# %% sort by values
# The Series.sort_values() method is used to sort a Series by its values. 
# The DataFrame.sort_values() method is used to sort a DataFrame by its column or row values. 
# The optional by parameter to DataFrame.sort_values() may used to specify one or more columns 
# to use to determine the sorted order.


df1 = pd.DataFrame(
        {"one": [2, 1, 1, 1], "two": [1, 3, 2, 4], "three": [5, 4, 3, 2]}
    )
# 	one	two	three
# 0	2	1	5
# 1	1	3	4
# 2	1	2	3
# 3	1	4	2


df1.sort_values(by="two")
# 	one	two	three
# 0	2	1	5
# 2	1	2	3
# 1	1	3	4
# 3	1	4	2

df1[["one", "two", "three"]].sort_values(by=["one", "two"])
# 	one	two	three
# 2	1	2	3
# 1	1	3	4
# 3	1	4	2
# 0	2	1	5

s[2] = np.nan
# 0       A
# 1       B
# 2    <NA>
# 3    Aaba
# 4    Baca
# 5    <NA>
# 6    CABA
# 7     dog
# 8     cat
# dtype: string

s.sort_values()
# 0       A
# 3    Aaba
# 1       B
# 4    Baca
# 6    CABA
# 8     cat
# 7     dog
# 2    <NA>
# 5    <NA>
# dtype: string

#%% na_position parameter
s.sort_values(na_position="first")
# 2    <NA>
# 5    <NA>
# 0       A
# 3    Aaba
# 1       B
# 4    Baca
# 6    CABA
# 8     cat
# 7     dog
# dtype: string


#%% Series key parameter 
s1 = pd.Series(["B", "a", "C"])
s1.sort_values()
# 0    B
# 2    C
# 1    a
# dtype: object

s1.sort_values(key=lambda x: x.str.lower())
# 1    a
# 0    B
# 2    C
# dtype: object

# key will be given the Series of values and should return a Series or 
# array of the same shape with the transformed values. 
# For DataFrame objects, the key is applied per column, 
# so the key should still expect a Series and return a Series, e.g.

# The name or type of each column can be used to apply different functions to different columns.


#%% sort By indexes and values
# Strings passed as the by parameter to DataFrame.sort_values() 
# may refer to either columns or index level names.

idx = pd.MultiIndex.from_tuples(
        [("a", 1), ("a", 2), ("a", 2), ("b", 2), ("b", 1), ("b", 1)]
    )
# MultiIndex([('a', 1),
#             ('a', 2),
#             ('a', 2),
#             ('b', 2),
#             ('b', 1),
#             ('b', 1)],
#            names=['first', 'second'])

idx.names = ["first", "second"]

df_multi = pd.DataFrame({"A": np.arange(6, 0, -1)}, index=idx)
# 		        A
# first	second	
# a	    1	    6
#       2	    5
#       2	    4
# b	    2	    3
#       1	    2
#       1	    1

df_multi.sort_values(by=["second", "A"])
# 	            A
# first	second	
# b	    1	    1
#       1	    2
# a	    1	    6
# b	    2	    3
# a	    2	    4
#       2	    5

# If a string matches both a column name and an index level name then a warning is issued and the column takes precedence. This will result in an ambiguity error in a future version.

#%% searchsorted

# Series has the searchsorted() method, which works similarly to numpy.ndarray.searchsorted().
# searchsorted(): Find indices where elements should be inserted to maintain order.

ser = pd.Series([1, 2, 3])
ser.searchsorted([0, 3])
# array([0, 2])

ser.searchsorted(4)
# 3

ser.searchsorted([0, 4])
# array([0, 3])

ser.searchsorted([1, 3], side='left')
# array([0, 2])

ser.searchsorted([1, 3], side='right')
# array([1, 3])

ser = pd.Series(pd.to_datetime(['3/11/2000', '3/12/2000', '3/13/2000']))
ser
# 0   2000-03-11
# 1   2000-03-12
# 2   2000-03-13
# dtype: datetime64[ns]


ser.searchsorted('3/14/2000')
# 3

ser = pd.Categorical(
    ['apple', 'bread', 'bread', 'cheese', 'milk'], ordered=True
)
ser
# ['apple', 'bread', 'bread', 'cheese', 'milk']
# Categories (4, object): ['apple' < 'bread' < 'cheese' < 'milk']


ser.searchsorted('bread')
# 1

ser.searchsorted(['bread'], side='right')
# array([3], dtype=int64)


# %% If the values are not monotonically sorted, wrong locations may be returned:
ser = pd.Series([2, 1, 3])
ser
# 0    2
# 1    1
# 2    3
# dtype: int64

ser.searchsorted(1)  
# 0

ser = pd.Series([3, 1, 2])
ser.searchsorted([0, 3], sorter=np.argsort(ser))
# array([0, 2])

#%% smallest / largest values
# Series has the nsmallest() and nlargest() methods which return the smallest or largest n values. 
# For a large Series this can be much faster than sorting the entire Series and calling head(n) on the result.
s = pd.Series(np.random.permutation(10))
s
# 0    0
# 1    9
# 2    5
# 3    4
# 4    1
# 5    6
# 6    3
# 7    2
# 8    8
# 9    7
# dtype: int32

s.sort_values()
# 7    0
# 9    1
# 5    2
# 6    3
# 1    4
# 0    5
# 8    6
# 2    7
# 4    8
# 3    9
# dtype: int32

s.nsmallest(3)
# 8    0
# 5    1
# 6    2
# dtype: int32

s.nlargest(3)
# 2    9
# 0    8
# 9    7
# dtype: int32


#%% DataFrame also has the nlargest and nsmallest methods.
df = pd.DataFrame(
        {
            "a": [-2, -1, 1, 10, 8, 11, -1],
            "b": list("abdceff"),
            "c": [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0],
        }
    )
df
# 	a	b	c
# 0	-2	a	1.0
# 1	-1	b	2.0
# 2	1	d	4.0
# 3	10	c	3.2
# 4	8	e	NaN
# 5	11	f	3.0
# 6	-1	f	4.0

df.nlargest(3, "a")
# 	a	b	c
# 5	11	f	3.0
# 3	10	c	3.2
# 4	8	e	NaN

df.nlargest(5, ["a", "c"])
# 	a	b	c
# 5	11	f	3.0
# 3	10	c	3.2
# 4	8	e	NaN
# 2	1	d	4.0
# 6	-1	f	4.0

df.nsmallest(3, "a")
# 	a	b	c
# 0	-2	a	1.0
# 1	-1	b	2.0
# 6	-1	f	4.0

df.nsmallest(5, ["a", "c"])
# 	a	b	c
# 0	-2	a	1.0
# 1	-1	b	2.0
# 6	-1	f	4.0
# 2	1	d	4.0
# 4	8	e	NaN

#%% Sorting by a MultiIndex column
df1.columns = pd.MultiIndex.from_tuples(
        [("a", "one"), ("a", "two"), ("b", "three")]
    )
# 	a	b
# one	two	three
# 0	2	1	5
# 1	1	3	4
# 2	1	2	3
# 3	1	4	2
df1.sort_values(by=("a", "two"))
# a	b
# one	two	three
# 0	2	1	5
# 2	1	2	3
# 1	1	3	4
# 3	1	4	2