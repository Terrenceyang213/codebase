# %% Parsing options
# read_csv() accepts the following common arguments:

# %% Basic
# filepath_or_buffer:   various
# Either a path to a file (a str, pathlib.Path, or py._path.local.LocalPath), URL (including http, ftp, and S3 locations), or any object with a read() method (such as an open file or StringIO).

# sep:  str, defaults to ',' for read_csv(), \t for read_table()
# Delimiter to use. If sep is None, the C engine cannot automatically detect the separator, but the Python parsing engine can, meaning the latter will be used and automatically detect the separator by Python’s builtin sniffer tool, csv.Sniffer. In addition, separators longer than 1 character and different from '\s+' will be interpreted as regular expressions and will also force the use of the Python parsing engine. Note that regex delimiters are prone to ignoring quoted data. Regex example: '\\r\\t'.

# delimiter:    str, default None
# Alternative argument name for sep.

# delim_whitespace: boole
# Specifies whether or not whitespace (e.g. ' ' or '\t') will be used as the delimiter. Equivalent to setting sep='\s+'. If this option is set to True, nothing should be passed in for the delimiter parameter.

#%% Column and index locations and names

# header:   int or list of ints, default 'infer'
# Row number(s) to use as the column names, and the start of the data. Default behavior is to infer the column names: if no names are passed the behavior is identical to header=0 and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to header=None. Explicitly pass header=0 to be able to replace existing names.
# The header can be a list of ints that specify row locations for a MultiIndex on the columns e.g. [0,1,3]. Intervening rows that are not specified will be skipped (e.g. 2 in this example is skipped). Note that this parameter ignores commented lines and empty lines if skip_blank_lines=True, so header=0 denotes the first line of data rather than the first line of the file.

# names:    array-like, default None
# List of column names to use. If file contains no header row, then you should explicitly pass header=None. Duplicates in this list are not allowed.

# index_col:    int, str, sequence of int / str, or False, default None
# Column(s) to use as the row labels of the DataFrame, either given as string name or column index. If a sequence of int / str is given, a MultiIndex is used.
# Note: index_col=False can be used to force pandas to not use the first column as the index, e.g. when you have a malformed file with delimiters at the end of each line.
# The default value of None instructs pandas to guess. If the number of fields in the column header row is equal to the number of fields in the body of the data file, then a default index is used. If it is one larger, then the first field is used as an index.

# usecols:  list-like or callable, default None
# Return a subset of the columns. If list-like, all elements must either be positional (i.e. integer indices into the document columns) or strings that correspond to column names provided either by the user in names or inferred from the document header row(s). For example, a valid list-like usecols parameter would be [0, 1, 2] or ['foo', 'bar', 'baz'].
# Element order is ignored, so usecols=[0, 1] is the same as [1, 0]. To instantiate a DataFrame from data with element order preserved use pd.read_csv(data, usecols=['foo', 'bar'])[['foo', 'bar']] for columns in ['foo', 'bar'] order or pd.read_csv(data, usecols=['foo', 'bar'])[['bar', 'foo']] for ['bar', 'foo'] order.

# If callable, the callable function will be evaluated against the column names, returning names where the callable function evaluates to True:

pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ["COL1", "COL3"])
#   col1  col3
# 0    a     1
# 1    a     2
# 2    c     3

# squeeze:    boolean, default False
# If the parsed data only contains one column then return a Series.

# prefix:     str, default None
# Prefix to add to column numbers when no header, e.g. ‘X’ for X0, X1, …

# mangle_dupe_cols:   boolean, default True
# Duplicate columns will be specified as ‘X’, ‘X.1’…’X.N’, rather than ‘X’…’X’. Passing in False will cause data to be overwritten if there are duplicate names in the columns.


#%% General parsing configuration

# dtype:    Type name or dict of column -> type, default None
# Data type for data or columns. E.g. {'a': np.float64, 'b': np.int32} (unsupported with engine='python'). Use str or object together with suitable na_values settings to preserve and not interpret dtype.

# engine:   {'c', 'python'}
# Parser engine to use. The C engine is faster while the Python engine is currently more feature-complete.

# converters:   dict, default None
# Dict of functions for converting values in certain columns. Keys can either be integers or column labels.

# true_values:  list, default None
# Values to consider as True.

# false_values: list, default None
# Values to consider as False.

# skipinitialspace:     boolean, default False
# Skip spaces after delimiter.

# skiprows:     list-like or integer, default None
# Line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file.

# If callable, the callable function will be evaluated against the row indices, returning True if the row should be skipped and False otherwise:

data = "col1,col2,col3\na,b,1\na,b,2\nc,d,3"

pd.read_csv(StringIO(data))
# col1 col2  col3
# 0    a    b     1
# 1    a    b     2
# 2    c    d     3
pd.read_csv(StringIO(data), skiprows=lambda x: x % 2 != 0)
# col1 col2  col3
# 0    a    b     2


# skipfooter:     int, default 0
# Number of lines at bottom of file to skip (unsupported with engine=’c’).

# nrows:      int, default None
# Number of rows of file to read. Useful for reading pieces of large files.

# low_memory:     boolean, default True
# Internally process the file in chunks, resulting in lower memory use while parsing, but possibly mixed type inference. To ensure no mixed types either set False, or specify the type with the dtype parameter. Note that the entire file is read into a single DataFrame regardless, use the chunksize or iterator parameter to return the data in chunks. (Only valid with C parser)

# memory_map:     boolean, default False
# If a filepath is provided for filepath_or_buffer, map the file object directly onto memory and access the data directly from there. Using this option can improve performance because there is no longer any I/O overhead.

# %% NA and missing data handling
# na_values:  scalar, str, list-like, or dict, default None
# Additional strings to recognize as NA/NaN. If dict passed, specific per-column NA values. See na values const below for a list of the values interpreted as NaN by default.

# keep_default_na:    boolean, default True
# Whether or not to include the default NaN values when parsing the data. Depending on whether na_values is passed in, the behavior is as follows:
    # If keep_default_na is True, and na_values are specified, na_values is appended to the default NaN values used for parsing.
    # If keep_default_na is True, and na_values are not specified, only the default NaN values are used for parsing.
    # If keep_default_na is False, and na_values are specified, only the NaN values specified na_values are used for parsing.
    # If keep_default_na is False, and na_values are not specified, no strings will be parsed as NaN.
    # Note that if na_filter is passed in as False, the keep_default_na and na_values parameters will be ignored.

# na_filter:  boolean, default True
# Detect missing value markers (empty strings and the value of na_values). In data without any NAs, passing na_filter=False can improve the performance of reading a large file.

# verbose:    boolean, default False
# Indicate number of NA values placed in non-numeric columns.

# skip_blank_lines:   boolean, default True
# If True, skip over blank lines rather than interpreting as NaN values.


#%% Datetime handling
# parse_dates:    boolean or list of ints or names or list of lists or dict, default False.
    # If True -> try parsing the index.
    # If [1, 2, 3] -> try parsing columns 1, 2, 3 each as a separate date column.
    # If [[1, 3]] -> combine columns 1 and 3 and parse as a single date column.
    # If {'foo': [1, 3]} -> parse columns 1, 3 as date and call result ‘foo’. A fast-path exists for iso8601-formatted dates.

# infer_datetime_format:  boolean, default False
# If True and parse_dates is enabled for a column, attempt to infer the datetime format to speed up the processing.

# keep_date_col:  boolean, default False
# If True and parse_dates specifies combining multiple columns then keep the original columns.

# date_parser:    function, default None
# Function to use for converting a sequence of string columns to an array of datetime instances. The default uses dateutil.parser.parser to do the conversion. pandas will try to call date_parser in three different ways, advancing to the next if an exception occurs: 1) Pass one or more arrays (as defined by parse_dates) as arguments; 2) concatenate (row-wise) the string values from the columns defined by parse_dates into a single array and pass that; and 3) call date_parser once for each row using one or more strings (corresponding to the columns defined by parse_dates) as arguments.

# dayfirst:   boolean, default False
# DD/MM format dates, international and European format.

# cache_dates:    boolean, default True
# If True, use a cache of unique, converted dates to apply the datetime conversion. May produce significant speed-up when parsing duplicate date strings, especially ones with timezone offsets.


#%% Iteration
# iterator:   boolean, default False
# Return TextFileReader object for iteration or getting chunks with get_chunk().

# chunksize:    int, default None
# Return TextFileReader object for iteration. See iterating and chunking below.


#%% Quoting, compression, and file format
# compression:    {'infer', 'gzip', 'bz2', 'zip', 'xz', None, dict}, default 'infer'
# For on-the-fly decompression of on-disk data. If ‘infer’, then use gzip, bz2, zip, or xz if filepath_or_buffer is path-like ending in ‘.gz’, ‘.bz2’, ‘.zip’, or ‘.xz’, respectively, and no decompression otherwise. If using ‘zip’, the ZIP file must contain only one data file to be read in. Set to None for no decompression. Can also be a dict with key 'method' set to one of {'zip', 'gzip', 'bz2'} and other key-value pairs are forwarded to zipfile.ZipFile, gzip.GzipFile, or bz2.BZ2File. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}.
    # Changed in version 0.24.0: ‘infer’ option added and set to default.
    # Changed in version 1.1.0: dict option extended to support gzip and bz2.
    # Changed in version 1.2.0: Previous versions forwarded dict entries for ‘gzip’ to gzip.open.

# thousands：   str, default None
# Thousands separator.

# decimalstr, default '.'
# Character to recognize as decimal point. E.g. use ',' for European data.

# float_precisionstring, default None
# Specifies which converter the C engine should use for floating-point values. The options are None for the ordinary converter, high for the high-precision converter, and round_trip for the round-trip converter.

# lineterminatorstr (length 1), default None
# Character to break file into lines. Only valid with C parser.

# quotecharstr (length 1)
# The character used to denote the start and end of a quoted item. Quoted items can include the delimiter and it will be ignored.

# quotingint or csv.QUOTE_* instance, default 0
# Control field quoting behavior per csv.QUOTE_* constants. Use one of QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).

# doublequoteboolean, default True
# When quotechar is specified and quoting is not QUOTE_NONE, indicate whether or not to interpret two consecutive quotechar elements inside a field as a single quotechar element.

# escapecharstr (length 1), default None
# One-character string used to escape delimiter when quoting is QUOTE_NONE.

# commentstr, default None
# Indicates remainder of line should not be parsed. If found at the beginning of a line, the line will be ignored altogether. This parameter must be a single character. Like empty lines (as long as skip_blank_lines=True), fully commented lines are ignored by the parameter header but not by skiprows. For example, if comment='#', parsing ‘#empty\na,b,c\n1,2,3’ with header=0 will result in ‘a,b,c’ being treated as the header.

# encodingstr, default None
# Encoding to use for UTF when reading/writing (e.g. 'utf-8'). List of Python standard encodings.

# dialectstr or csv.Dialect instance, default None
# If provided, this parameter will override values (default or not) for the following parameters: delimiter, doublequote, escapechar, skipinitialspace, quotechar, and quoting. If it is necessary to override values, a ParserWarning will be issued. See csv.Dialect documentation for more details.

# %%Error handling
# error_bad_lines：     boolean, default True
# Lines with too many fields (e.g. a csv line with too many commas) will by default cause an exception to be raised, and no DataFrame will be returned. If False, then these “bad lines” will dropped from the DataFrame that is returned. See bad lines below.

# warn_bad_lines：  boolean, default True
# If error_bad_lines is False, and warn_bad_lines is True, a warning for each “bad line” will be output.

