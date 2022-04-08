#%%
import numpy as np
import pandas as pd

# %% Series has an accessor to succinctly return datetime like properties for the values of the Series, 
# if it is a datetime/period like Series. 
# This will return a Series, indexed like the existing Series.
s = pd.Series(pd.date_range("20130101 09:10:12", periods=4))
s
# 0   2013-01-01 09:10:12
# 1   2013-01-02 09:10:12
# 2   2013-01-03 09:10:12
# 3   2013-01-04 09:10:12
# dtype: datetime64[ns]

s.dt.hour
# 0    9
# 1    9
# 2    9
# 3    9
# dtype: int64


s.dt.second
# 0    12
# 1    12
# 2    12
# 3    12
# dtype: int64

s.dt.day
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64


s[s.dt.day == 2]
# 1   2013-01-02 09:10:12
# dtype: datetime64[ns]

#%% timezone convert 时区转换
stz = s.dt.tz_localize("US/Eastern")
# 0   2013-01-01 09:10:12-05:00
# 1   2013-01-02 09:10:12-05:00
# 2   2013-01-03 09:10:12-05:00
# 3   2013-01-04 09:10:12-05:00
# dtype: datetime64[ns, US/Eastern]


stz.dt.tz
# <DstTzInfo 'US/Eastern' LMT-1 day, 19:04:00 STD>


s.dt.tz_localize("UTC").dt.tz_convert("US/Eastern")
# 0   2013-01-01 04:10:12-05:00
# 1   2013-01-02 04:10:12-05:00
# 2   2013-01-03 04:10:12-05:00
# 3   2013-01-04 04:10:12-05:00
# dtype: datetime64[ns, US/Eastern]


# %% You can also format datetime values as strings with Series.dt.strftime() 
# which supports the same format as the standard strftime().


s = pd.Series(pd.date_range("20130101", periods=4))
s
# 0   2013-01-01
# 1   2013-01-02
# 2   2013-01-03
# 3   2013-01-04
# dtype: datetime64[ns]


s.dt.strftime("%Y/%m/%d")
# 0    2013/01/01
# 1    2013/01/02
# 2    2013/01/03
# 3    2013/01/04
# dtype: object


s = pd.Series(pd.period_range("20130101", periods=4))
s
# 0    2013-01-01
# 1    2013-01-02
# 2    2013-01-03
# 3    2013-01-04
# dtype: period[D]


s.dt.strftime("%Y/%m/%d")
# 0    2013/01/01
# 1    2013/01/02
# 2    2013/01/03
# 3    2013/01/04
# dtype: object


# %% The .dt accessor works for period and timedelta dtypes.
s = pd.Series(pd.period_range("20130101", periods=4, freq="s"))
s
# 0    2013-01-01 00:00:00
# 1    2013-01-01 00:00:01
# 2    2013-01-01 00:00:02
# 3    2013-01-01 00:00:03
# dtype: period[S]

s.dt.year
# 0    2013
# 1    2013
# 2    2013
# 3    2013
# dtype: int64

s.dt.day
# 0    1
# 1    1
# 2    1
# 3    1
# dtype: int64


# %%
s = pd.Series(pd.timedelta_range("1 day 00:00:05", periods=4, freq="s"))
s
# 0   1 days 00:00:05
# 1   1 days 00:00:06
# 2   1 days 00:00:07
# 3   1 days 00:00:08
# dtype: timedelta64[ns]

s.dt.days
# 0    1
# 1    1
# 2    1
# 3    1
# dtype: int64

s.dt.seconds
# 0    5
# 1    6
# 2    7
# 3    8
# dtype: int64

s.dt.components
# 	days	hours	minutes	seconds	milliseconds	microseconds	nanoseconds
# 0	1	    0	    0	    5	    0	            0	            0
# 1	1	    0	    0	    6	    0	            0	            0
# 2	1	    0	    0	    7	    0	            0	            0
# 3	1	    0	    0	    8	    0	            0         	    0

