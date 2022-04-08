#%% Function apply
# To apply your own or another library’s functions to pandas objects, 
# you should be aware of the three methods below. 
# The appropriate method to use depends on whether your function expects 
# to operate on an entire DataFrame or Series, row- or column-wise, or elementwise.
    # Tablewise Function Application: pipe()
    # Row or Column-wise Function Application: apply()
    # Aggregation API: agg() and transform()
    # Applying Elementwise Functions: applymap()

# %% Tablewise function application/ pipe
# DataFrames and Series can be passed into functions. 
# However, if the function needs to be called in a chain, consider using the pipe() method.
def extract_city_name(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df["city_name"] = df["city_and_code"].str.split(",").str.get(0)
    return df


def add_country_name(df, country_name=None):
    """
    Chicago -> Chicago-US for city_name column
    """
    col = "city_name"
    df["city_and_country"] = df[col] + country_name
    return df


df_p = pd.DataFrame({"city_and_code": ["Chicago, IL"]})
add_country_name(extract_city_name(df_p), country_name="US")
#   city_and_code	city_name	city_and_country
# 0	Chicago, IL	    Chicago	    ChicagoUS


# 与上面相同的功能，可以用pipe实现
df_p2 = pd.DataFrame({"city_and_code": ["Chicago, IL"]})
# 	city_and_code
# 0	Chicago, IL

df_p2.pipe(extract_city_name)
# 	city_and_code	city_name
# 0	Chicago, IL	    Chicago



df_p2.pipe(extract_city_name).pipe(add_country_name, country_name="US")
#   city_and_code	    city_name	city_and_country
# 0	Chicago, IL	        Chicago	    ChicagoUS

# 推荐全表操作函数应用pip操作。 如果函数的第一个参数不是df，或者第二个参数才是df。
# 使用（callable，data_keyword)元组

# Use .pipe when chaining together functions that expect Series, DataFrames or GroupBy objects. 
# Instead of writing
func(g(h(df), arg1=a), arg2=b, arg3=c)  
# You can write
(df.pipe(h)
   .pipe(g, arg1=a)
   .pipe(func, arg2=b, arg3=c)
)  

#If you have a function that takes the data as (say) the second argument, 
# pass a tuple indicating which keyword expects the data. 
# For example, suppose f takes its data as arg2:
(df.pipe(h)
   .pipe(g, arg1=a)
   .pipe((func, 'arg2'), arg1=a, arg3=c) # 把df传给名为'arg2'的参数。
 )  

# %% Row or column-wise function application

# Arbitrary functions can be applied along the axes of a DataFrame using the apply() method, 
# which, like the descriptive statistics methods, takes an optional axis argument:

df.apply(np.mean) #apply on axis index
# one     -1.014193
# two      0.194797
# three   -0.842590
# dtype: float64

df.apply(np.mean, axis=1)
# a   -1.748551
# b   -0.566185
# c    0.296902
# d   -0.243106
# dtype: float64

df.apply(lambda x: x.max() - x.min())
# one      3.298509
# two      1.854547
# three    1.316836
# dtype: float64

df.apply(np.cumsum)
#   one	        two	        three
# a	-2.660717	-0.836386	NaN
# b	-3.680371	0.181775	-1.697061
# c	-3.042579	0.814916	-2.077286
# d	NaN	        0.779186	-2.527770

df.apply(np.exp)
#     one	        two	        three
# a	0.069898	0.433274	NaN
# b	0.360720	2.768100	0.183221
# c	1.892298	1.883516	0.683707
# d	NaN	        0.964901	0.637320

df.apply("mean")        # 计数时也忽略了nan的值
# one     -1.014193
# two      0.194797
# three   -0.842590
# dtype: float64

df.apply("mean", axis=1)
# a   -1.748551
# b   -0.566185
# c    0.296902
# d   -0.243106
# dtype: float64

# The return type of the function passed to apply() affects the type of the final output from DataFrame.
# apply for the default behaviour:
# If the applied function returns a Series, the final output is a DataFrame. 
# The columns match the index of the Series returned by the applied function.
# If the applied function returns any other type, the final output is a Series.
# This default behaviour can be overridden using the result_type, 
# which accepts three options: reduce, broadcast, and expand. 
# These will determine how list-likes return values expand (or not) to a DataFrame.

# %% extract the date where the maximum value for each column
# apply() combined with some cleverness can be used to answer many questions about a data set. 
# For example, suppose we wanted to extract the date where the maximum value for each column occurred:
tsdf = pd.DataFrame(
        np.random.randn(1000, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=1000),
    )
    
tsdf.apply(lambda x: x.idxmax()) # tsdf.idxmax()

#%% You may also pass additional arguments and keyword arguments to the apply() method. 
# For instance, consider the following function you would like to apply:
def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide

# 减1 除3
df.apply(subtract_and_divide, args=(1,3))  #args必须是一个tuple
#   one	        two	        three
# a	-1.220239	-0.612129	NaN
# b	-0.673218	0.006054	-0.899020
# c	-0.120736	-0.122287	-0.460075
# d	NaN	        -0.345243	-0.483494

df.apply(subtract_and_divide, args=(1,), divide=3) 
#   one	        two	        three
# a	-1.220239	-0.612129	NaN
# b	-0.673218	0.006054	-0.899020
# c	-0.120736	-0.122287	-0.460075
# d	NaN	        -0.345243	-0.483494

df.apply(subtract_and_divide, sub=1 , divide=3)
#   one	        two	        three
# a	-1.220239	-0.612129	NaN
# b	-0.673218	0.006054	-0.899020
# c	-0.120736	-0.122287	-0.460075
# d	NaN	        -0.345243	-0.483494

# %% Another useful feature is the ability to pass Series methods to carry out some Series operation on each column or row:
tsdf = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(2), index=["a", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)
#   one	        two	        three
# a	-0.492571	1.053883	NaN
# b	NaN	        -0.129907	1.657225
# c	0.717138	-0.468582	0.055487
# d	NaN	        0.149485	3.200622

tsdf.apply(pd.Series.interpolate) 
#   one	        two	        three
# a	-0.492571	1.053883	NaN
# b	0.112283	-0.129907	1.657225
# c	0.717138	-0.468582	0.055487
# d	0.717138	0.149485	3.200622


# pandas.Series.interpolate(method='linear', axis=0, limit=None, inplace=False, limit_direction=None, limit_area=None, downcast=None, **kwargs)
# Fill NaN values using an interpolation method.

# %% argument raw
# Finally, apply() takes an argument raw which is False by default, 
# which converts each row or column into a Series before applying the function. When set to True, 
# the passed function will instead receive an ndarray object, 
# which has positive performance implications if you do not need the indexing functionality.

# raw:bool, default False
    # Determines if row or column is passed as a Series or ndarray object:
    # False : passes each row or column as a Series to the function.
    # True : the passed function will receive ndarray objects instead. 
    #        If you are just applying a NumPy reduction function this will achieve much better performance.


#%% aggregation API/ agg
# The aggregation API allows one to express possibly multiple aggregation operations in a single concise way. 
# This API is similar across pandas objects, see groupby API, the window API, and the resample API. 
# The entry point for aggregation is DataFrame.aggregate(), or the alias DataFrame.agg().

tsdf = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=10),
    )
    
tsdf.iloc[3:7] = np.nan
tsdf
#               A	        B	        C
# 2000-01-01	0.228736	-0.033217	0.853895
# 2000-01-02	-0.261226	2.119026	0.053668
# 2000-01-03	1.424884	1.373974	1.296386
# 2000-01-04	NaN	        NaN	        NaN
# 2000-01-05	NaN	        NaN	        NaN
# 2000-01-06	NaN	        NaN	        NaN
# 2000-01-07	NaN	        NaN	        NaN
# 2000-01-08	-0.331278	-1.752296	-2.346237
# 2000-01-09	-0.426335	1.457909	0.694353
# 2000-01-10	-0.129955	-0.161175	-1.232635

#%% Using a single function is equivalent to apply(). 
# You can also pass named methods as strings. 
# These will return a Series of the aggregated output:
tsdf.agg(np.sum)
# A    0.504826
# B    3.004220
# C   -0.680570
# dtype: float64

tsdf.agg("sum")
# A    0.504826
# B    3.004220
# C   -0.680570
# dtype: float64

# these are equivalent to a ``.sum()`` because we are aggregating
# on a single function
tsdf.sum()
# A    0.504826
# B    3.004220
# C   -0.680570
# dtype: float64

# Single aggregations on a Series this will return a scalar value:
tsdf["A"].agg("sum")
# 0.5048257069373467


# %% Aggregating with multiple functions
# You can pass multiple aggregation arguments as a list. 
# The results of each of the passed functions will be a row in the resulting DataFrame. 
# These are naturally named from the aggregation function.

# You can pass multiple aggregation arguments as a list. 
# The results of each of the passed functions will be a row in the resulting DataFrame. 
# These are naturally named from the aggregation function.

tsdf.agg(["sum"])
#       A	        B	    C
# sum	0.504826	3.00422	-0.68057

tsdf.agg(["sum", "mean"])
#       A           B	        C
# sum	0.504826	3.004220	-0.680570
# mean	0.084138	0.500703	-0.113428

# On a Series, multiple functions return a Series, indexed by the function names:
tsdf["A"].agg(["sum", "mean"])
# sum     0.504826
# mean    0.084138
# Name: A, dtype: float64

# Passing a lambda function will yield a <lambda> named row:
tsdf["A"].agg(["sum", lambda x: x.mean()])
# sum         0.504826
# <lambda>    0.084138
# Name: A, dtype: float64


# Passing a named function will yield that name for the row:
def mymean(x):
    return x.mean()

tsdf["A"].agg(["sum", mymean])
# sum       0.504826
# mymean    0.084138
# Name: A, dtype: float64

# %% Aggregating with a dict
# Passing a dictionary of column names to a scalar or a list of scalars, 
# to DataFrame.agg allows you to customize which functions are applied to which columns. 
# Note that the results are not in any particular order, 
# you can use an OrderedDict instead to guarantee ordering.

tsdf.agg({"A": "mean", "B": "sum"})
# A    0.084138
# B    3.004220
# dtype: float64


# %% Passing a list-like will generate a DataFrame output. 
# You will get a matrix-like output of all of the aggregators. 
# The output will consist of all unique functions. 
# Those that are not noted for a particular column will be NaN:

tsdf.agg({"A": ["mean", "min"], "B": "sum"})
#       A	        B
# mean	0.084138	NaN
# min	-0.426335	NaN
# sum	NaN	        3.00422

#%% Mixed dtypes
# When presented with mixed dtypes that cannot aggregate, 
# .agg will only take the valid aggregations. This is similar to how .groupby.agg works.
mdf = pd.DataFrame(
        {
            "A": [1, 2, 3],
            "B": [1.0, 2.0, 3.0],
            "C": ["foo", "bar", "baz"],
            "D": pd.date_range("20130101", periods=3),
        }
    )
# 	A	B	C	D
# 0	1	1.0	foo	2013-01-01
# 1	2	2.0	bar	2013-01-02
# 2	3	3.0	baz	2013-01-03

mdf.dtypes
# A             int64
# B           float64
# C            object
# D    datetime64[ns]
# dtype: object

mdf.agg(["min", "sum"])
# 	    A	B	C	        D
# min	1	1.0	bar	        2013-01-01
# sum	6	6.0	foobarbaz	NaT


# %% Custom describe ??
# With .agg() it is possible to easily create a custom describe function, 
# similar to the built in describe function.

from functools import partial
q_25 = partial(pd.Series.quantile, q=0.25)
q_25.__name__ = "25%"
q_75 = partial(pd.Series.quantile, q=0.75)
q_75.__name__ = "75%"
tsdf.agg(["count", "mean", "std", "min", q_25, "median", q_75, "max"])
#       A	        B	        C
# count	6.000000	6.000000	6.000000
# mean	0.084138	0.500703	-0.113428
# std	0.695237	1.421054	1.402981
# min	-0.426335	-1.752296	-2.346237
# 25%	-0.313765	-0.129186	-0.911059
# med	-0.195591	0.670378	0.374011
# 75%	0.139064	1.436925	0.814010
# max	1.424884	2.119026	1.296386


#%% Transform API
# The transform() method returns an object that is indexed the same (same size) as the original. 
# This API allows you to provide multiple operations at the same time rather than one-by-one. 
# Its API is quite similar to the .agg API.
In [185]: tsdf = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=10),
    )
tsdf.iloc[3:7] = np.nan
tsdf
#               A	        B	        C
# 2000-01-01	0.228736	-0.033217	0.853895
# 2000-01-02	-0.261226	2.119026	0.053668
# 2000-01-03	1.424884	1.373974	1.296386
# 2000-01-04	NaN	        NaN	        NaN
# 2000-01-05	NaN	        NaN	        NaN
# 2000-01-06	NaN	        NaN	        NaN
# 2000-01-07	NaN	        NaN	        NaN
# 2000-01-08	-0.331278	-1.752296	-2.346237
# 2000-01-09	-0.426335	1.457909	0.694353
# 2000-01-10	-0.129955	-0.161175	-1.232635

# Transform the entire frame. .transform() allows input functions as: 
# a NumPy function, 
# a string function name or 
# a user defined function.

#np.abs(tsdf)
tsdf.transform(np.abs)
tsdf.transform("abs")
tsdf.transform(lambda x: x.abs())  
# A	B	C
# 2000-01-01	0.228736	0.033217	0.853895
# 2000-01-02	0.261226	2.119026	0.053668
# 2000-01-03	1.424884	1.373974	1.296386
# 2000-01-04	NaN	NaN	NaN
# 2000-01-05	NaN	NaN	NaN
# 2000-01-06	NaN	NaN	NaN
# 2000-01-07	NaN	NaN	NaN
# 2000-01-08	0.331278	1.752296	2.346237
# 2000-01-09	0.426335	1.457909	0.694353
# 2000-01-10	0.129955	0.161175	1.232635



# Passing a single function to .transform() with a Series will yield a single Series in return.
tsdf["A"].transform(np.abs)
# 2000-01-01    0.228736
# 2000-01-02    0.261226
# 2000-01-03    1.424884
# 2000-01-04         NaN
# 2000-01-05         NaN
# 2000-01-06         NaN
# 2000-01-07         NaN
# 2000-01-08    0.331278
# 2000-01-09    0.426335
# 2000-01-10    0.129955
# Freq: D, Name: A, dtype: float64


#%% Transform with multiple functions
# Passing multiple functions will yield a column MultiIndexed DataFrame. 
# The first level will be the original frame column names; 
# the second level will be the names of the transforming functions.


tsdf.transform([np.abs, lambda x: x + 1])
# 	            A	                    B	                    C
# absolute	    <lambda>	absolute	<lambda>	absolute	<lambda>
# 2000-01-01	0.228736	1.228736	0.033217	0.966783	0.853895	1.853895
# 2000-01-02	0.261226	0.738774	2.119026	3.119026	0.053668	1.053668
# 2000-01-03	1.424884	2.424884	1.373974	2.373974	1.296386	2.296386
# 2000-01-04	NaN	NaN	                NaN	NaN	                NaN	NaN
# 2000-01-05	NaN	NaN	                NaN	NaN	                NaN	NaN
# 2000-01-06	NaN	NaN	                NaN	NaN	                NaN	NaN
# 2000-01-07	NaN	NaN	                NaN	NaN	                NaN	NaN
# 2000-01-08	0.331278	0.668722	1.752296	-0.752296	2.346237	-1.346237
# 2000-01-09	0.426335	0.573665	1.457909	2.457909	0.694353	1.694353
# 2000-01-10	0.129955	0.870045	0.161175	0.838825	1.232635	-0.232635


# Passing multiple functions to a Series will yield a DataFrame. 
# The resulting column names will be the transforming functions.
tsdf["A"].transform([np.abs, lambda x: x + 1])
# 	            absolute	<lambda>
# 2000-01-01	0.228736	1.228736
# 2000-01-02	0.261226	0.738774
# 2000-01-03	1.424884	2.424884
# 2000-01-04	NaN	        NaN
# 2000-01-05	NaN	        NaN
# 2000-01-06	NaN	        NaN
# 2000-01-07	NaN	        NaN
# 2000-01-08	0.331278	0.668722
# 2000-01-09	0.426335	0.573665
# 2000-01-10	0.129955	0.870045

# %% Transforming with a dict
tsdf.transform({"A": np.abs, "B": lambda x: x + 1})
# 	            A	        B
# 2000-01-01	0.228736	0.966783
# 2000-01-02	0.261226	3.119026
# 2000-01-03	1.424884	2.373974
# 2000-01-04	NaN	NaN
# 2000-01-05	NaN	NaN
# 2000-01-06	NaN	NaN
# 2000-01-07	NaN	NaN
# 2000-01-08	0.331278	-0.752296
# 2000-01-09	0.426335	2.457909
# 2000-01-10	0.129955	0.838825

# Passing a dict of lists will generate a MultiIndexed DataFrame with these selective transforms.
tsdf.transform({"A": np.abs, "B": [lambda x: x + 1, "sqrt"]})
# 	            A	        B
#               absolute	<lambda>	sqrt
# 2000-01-01	0.228736	0.966783	NaN
# 2000-01-02	0.261226	3.119026	1.455687
# 2000-01-03	1.424884	2.373974	1.172166
# 2000-01-04	NaN	NaN	NaN
# 2000-01-05	NaN	NaN	NaN
# 2000-01-06	NaN	NaN	NaN
# 2000-01-07	NaN	NaN	NaN
# 2000-01-08	0.331278	-0.752296	NaN
# 2000-01-09	0.426335	2.457909	1.207439
# 2000-01-10	0.129955	0.838825	NaN


# %% Applying elementwise functions
# Since not all functions can be vectorized (accept NumPy arrays and return another array or value), 
# the methods applymap() on DataFrame and analogously map() on Series 
# accept any Python function taking a single value and returning a single value. For example:
df
# 	one	        two	        three
# a	-2.660717	-0.836386	NaN
# b	-1.019654	1.018161	-1.697061
# c	0.637792	0.633140	-0.380225
# d	NaN	        -0.035730	-0.450483


def f(x):
    return len(str(x))

def s(x):
    return str(x)

df["one"].map(f)
# a    19
# b    19
# c    18
# d     3
# Name: one, dtype: int64

df['one'].map(s)
# a    -2.6607167927762654
# b    -1.0196537304836464
# c     0.6377919710624219
# d                    nan
# Name: one, dtype: object

# df.map(s)
# AttributeError: 'DataFrame' object has no attribute 'map'

df.applymap(f)
# 	one	two	three
# a	19	19	3
# b	19	18	18
# c	18	17	20
# d	3	21	20


# %% Series.map() has an additional feature; 
# it can be used to easily “link” or “map” values defined by a secondary series. 
# This is closely related to merging/joining functionality:
s = pd.Series(
        ["six", "seven", "six", "seven", "six"], index=["a", "b", "c", "d", "e"]
    )
t = pd.Series({"six": 6.0, "seven": 7.0})
s
# a      six
# b    seven
# c      six
# d    seven
# e      six
# dtype: object
s.map(t)
# a    6.0
# b    7.0
# c    6.0
# d    7.0
# e    6.0
# dtype: float64