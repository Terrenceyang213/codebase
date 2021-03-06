#%%
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])
df + df2
#   A	        B	        C	        D
# 0	2.469650	-2.835023	-1.316705	NaN
# 1	0.640293	0.743802	0.935325	NaN
# 2	1.423573	1.073739	-0.824655	NaN
# 3	-0.829337	-0.160558	-0.500191	NaN
# 4	-0.466663	-1.383111	1.713833	NaN
# 5	-2.114952	0.660042	0.651989	NaN
# 6	0.219360	0.663289	-0.082985	NaN
# 7	NaN	        NaN	        NaN	        NaN
# 8	NaN	        NaN	        NaN	        NaN
# 9	NaN	        NaN	        NaN	        NaN


# %%
# 在DataFrame和Series之间进行操作时，默认行为是在DataFrame列上对齐Series索引，从而逐行广播。

df.iloc[0]
# A    1.548956
# B   -1.425253
# C   -0.568224
# D    0.145176
# Name: 0, dtype: float64

df
#   A	        B	        C	        D
# 0	1.548956	-1.425253	-0.568224	0.145176
# 1	-0.405454	-0.145553	1.287776	-2.009271
# 2	1.002589	-0.016431	-0.795494	0.093324
# 3	-0.685817	-1.923567	0.761660	1.352433
# 4	0.031649	-0.642212	1.140935	0.732709
# 5	-0.467496	1.787485	0.183241	0.419487
# 6	1.335303	0.829308	-0.534829	-0.712638
# 7	1.311685	1.232302	-1.590805	-1.548688
# 8	-0.338347	-0.835791	1.028043	0.661038
# 9	1.568342	0.916082	0.480689	-0.489627

df - df.iloc[0]
#   A	        B	        C	        D
# 0	0.000000	0.000000	0.000000	0.000000
# 1	-1.954410	1.279700	1.856000	-2.154448
# 2	-0.546367	1.408822	-0.227270	-0.051852
# 3	-2.234773	-0.498314	1.329884	1.207256
# 4	-1.517307	0.783041	1.709159	0.587533
# 5	-2.016452	3.212737	0.751465	0.274311
# 6	-0.213653	2.254561	0.033395	-0.857814
# 7	-0.237272	2.657554	-1.022582	-1.693865
# 8	-1.887303	0.589462	1.596267	0.515862
# 9	0.019385	2.341335	1.048912	-0.634803

# For explicit control over the matching and broadcasting behavior, 
# see the section on flexible binary operations.

#%%
