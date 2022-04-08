#%% 
# Format Type	    Data Description	    Reader	        Writer
# text	            CSV	                    read_csv	    to_csv
# text	            Fixed-Width Text File	read_fwf	
# text	            JSON	                read_json	    to_json
# text	            HTML	                read_html	    to_html
# text	            Local clipboard	        read_clipboard	to_clipboard
# binary	        MS Excel	            read_excel	    to_excel
# binary	        OpenDocument	        read_excel	
# binary	        HDF5 Format	            read_hdf	    to_hdf
# binary	        Feather Format	        read_feather	to_feather
# binary	        Parquet Format	        read_parquet	to_parquet
# binary	        ORC Format	            read_orc	
# binary	        Msgpack	                read_msgpack	to_msgpack
# binary	        Stata	                read_stata	    to_stata
# binary	        SAS	                    read_sas	
# binary	        SPSS	                read_spss	
# binary	        Python Pickle Format	read_pickle	    to_pickle
# SQL	            SQL	                    read_sql	    to_sql
# SQL	            Google BigQuery	        read_gbq	    to_gbq


#%% Performance considerations
# This is an informal comparison of various IO methods, using pandas 0.24.2. 
# Timings are machine dependent and small differences should be ignored.
import numpy as np
import pandas as pd
import os
import sqlite3


sz = 1000000
df = pd.DataFrame({'A': np.random.randn(sz), 'B': [1] * sz})
df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000000 entries, 0 to 999999
# Data columns (total 2 columns):
#  #   Column  Non-Null Count    Dtype  
# ---  ------  --------------    -----  
#  0   A       1000000 non-null  float64
#  1   B       1000000 non-null  int64  
# dtypes: float64(1), int64(1)
# memory usage: 15.3 MB

#%% test function
def test_sql_write(df):
    if os.path.exists("test.sql"):
        os.remove("test.sql")
    sql_db = sqlite3.connect("test.sql")
    df.to_sql(name="test_table", con=sql_db)
    sql_db.close()


def test_sql_read():
    sql_db = sqlite3.connect("test.sql")
    pd.read_sql_query("select * from test_table", sql_db)
    sql_db.close()


def test_hdf_fixed_write(df):
    df.to_hdf("test_fixed.hdf", "test", mode="w")


def test_hdf_fixed_read():
    pd.read_hdf("test_fixed.hdf", "test")


def test_hdf_fixed_write_compress(df):
    df.to_hdf("test_fixed_compress.hdf", "test", mode="w", complib="blosc")


def test_hdf_fixed_read_compress():
    pd.read_hdf("test_fixed_compress.hdf", "test")


def test_hdf_table_write(df):
    df.to_hdf("test_table.hdf", "test", mode="w", format="table")


def test_hdf_table_read():
    pd.read_hdf("test_table.hdf", "test")


def test_hdf_table_write_compress(df):
    df.to_hdf(
        "test_table_compress.hdf", "test", mode="w", complib="blosc", format="table"
    )

# %% 
def test_hdf_table_read_compress():
    pd.read_hdf("test_table_compress.hdf", "test")


def test_csv_write(df):
    df.to_csv("test.csv", mode="w")


def test_csv_read():
    pd.read_csv("test.csv", index_col=0)


def test_feather_write(df):
    df.to_feather("test.feather")


def test_feather_read():
    pd.read_feather("test.feather")


def test_pickle_write(df):
    df.to_pickle("test.pkl")


def test_pickle_read():
    pd.read_pickle("test.pkl")


def test_pickle_write_compress(df):
    df.to_pickle("test.pkl.compress", compression="xz")


def test_pickle_read_compress():
    pd.read_pickle("test.pkl.compress", compression="xz")


def test_parquet_write(df):
    df.to_parquet("test.parquet")


def test_parquet_read():
    pd.read_parquet("test.parquet")

#%% When writing, the top three functions in terms of speed are 
# test_feather_write, 
# test_hdf_fixed_write 
# test_hdf_fixed_write_compress.

In [4]: %timeit test_sql_write(df)
3.29 s ± 43.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [5]: %timeit test_hdf_fixed_write(df)
19.4 ms ± 560 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [6]: %timeit test_hdf_fixed_write_compress(df)
19.6 ms ± 308 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [7]: %timeit test_hdf_table_write(df)
449 ms ± 5.61 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [8]: %timeit test_hdf_table_write_compress(df)
448 ms ± 11.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [9]: %timeit test_csv_write(df)
3.66 s ± 26.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [10]: %timeit test_feather_write(df)
9.75 ms ± 117 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [11]: %timeit test_pickle_write(df)
30.1 ms ± 229 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [12]: %timeit test_pickle_write_compress(df)
4.29 s ± 15.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [13]: %timeit test_parquet_write(df)
67.6 ms ± 706 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


#%% When reading, the top three functions in terms of speed are test_feather_read, test_pickle_read and test_hdf_fixed_read.

%timeit test_sql_read()
1.77 s ± 17.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_hdf_fixed_read()
19.4 ms ± 436 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit test_hdf_fixed_read_compress()
19.5 ms ± 222 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit test_hdf_table_read()
38.6 ms ± 857 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit test_hdf_table_read_compress()
38.8 ms ± 1.49 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit test_csv_read()
452 ms ± 9.04 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_feather_read()
12.4 ms ± 99.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit test_pickle_read()
18.4 ms ± 191 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit test_pickle_read_compress()
915 ms ± 7.48 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit test_parquet_read()
24.4 ms ± 146 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)