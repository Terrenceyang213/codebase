#%%
import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df
#     A	        B	        C	        D
# 0	-0.589635	-1.128758	-1.836837	0.649957
# 1	-0.564747	3.557050	-0.225625	0.184502
# 2	-0.171421	-1.402046	-0.258757	1.208492
# 3	0.992882	-0.022058	0.223520	-0.255994
# 4	-1.029569	-0.541394	-1.632207	0.011050
# 5	0.437896	-0.991462	-0.739147	1.144689
# 6	0.122739	-0.048138	-0.896234	-0.315093
# 7	0.471191	-1.574410	0.190709	1.048402
# 8	0.013429	-1.019577	-0.353054	-0.904598
# 9	0.503896	-0.300399	-1.512410	-0.665426



# %%

#当前DataFrame常用信息
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10 entries, 0 to 9

# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   A       10 non-null     float64
#  1   B       10 non-null     float64
#  2   C       10 non-null     float64
#  3   D       10 non-null     float64
# dtypes: float64(4)
# memory usage: 448.0 bytes


df.to_string()
# '          A         B         C         D\n
# 0  0.115910 -1.143869 -1.343763 -0.358772\n
# 1 -1.520562  0.502416  0.988575  0.129661\n
# 2  0.189546  1.083677  0.448273  2.115333\n
# 3 -1.239296 -0.349252 -0.633775 -1.063955\n
# 4 -0.059800 -2.871633  0.163059  1.554279\n
# 5  0.559636  0.208128 -0.855423 -0.138476\n
# 6  1.065207  0.996804 -0.995055 -0.637088\n
# 7  0.324226  0.078354  0.668621  0.124676\n
# 8 -0.091012 -0.204294 -0.950217 -0.433294\n
# 9 -1.060040  0.578263 -1.323708  0.944700'



# %% display.width
# You can change how much to print on a single row by setting the display.width option:
pd.set_option("display.width", 40) #default is 80
pd.DataFrame(np.random.randn(3, 12))
# 0	1	2	3	4	5	6	7	8	9	10	11
# 0	0.815218	0.641276	0.718740	-1.373550	-0.910749	0.449539	1.224059	-0.212758	-0.697393	0.554137	-0.009187	-0.480775
# 1	-0.121690	-1.383904	0.999529	0.347518	0.127032	-0.823821	1.345551	-0.990535	-0.094643	-0.716368	-0.293097	-0.506058
# 2	0.540942	-1.447278	1.467118	1.240982	-0.076049	0.537705	0.319409	-0.688705	-0.820490	0.167048	-0.345212	0.541180

pd.set_option("display.width", 1) #default is 80
pd.DataFrame(np.random.randn(3, 12))

# 并没有什么变化，为什么？？



# %% display.max_colwidth
# You can adjust the max width of the individual columns by setting display.max_colwidth

datafile = {
   "filename": ["filename_01", "filename_02"],
   "path": [
            "media/user_name/storage/folder_01/filename_01",
            "media/user_name/storage/folder_02/filename_02",
            ],
    }

pd.set_option("display.max_colwidth", 30)
pd.DataFrame(datafile)

#   filename	path
# 0	filename_01	media/user_name/storage/fo...
# 1	filename_02	media/user_name/storage/fo...

pd.set_option("display.max_colwidth", 100)
pd.DataFrame(datafile)
#   filename	path
# 0	filename_01	media/user_name/storage/folder_01/filename_01
# 1	filename_02	media/user_name/storage/folder_02/filename_02



# %%
# If a DataFrame column label is a valid Python variable name, 
# the column can be accessed like an attribute:

df = pd.DataFrame({"foo1": np.random.randn(5), "foo2": np.random.randn(5)})
df.foo1 # equal df['foo1]
# 0   -0.926710
# 1    1.077350
# 2    1.389344
# 3   -0.930336
# 4    0.265048
# Name: foo1, dtype: float64

