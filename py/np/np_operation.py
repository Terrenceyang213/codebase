#%%
import numpy as np
from timeit import timeit

#%% tags:numpy;operation; max
a = np.array([1,2,3,4])

np.max(a) # a中最大元素
# 4
np.maximum(2,a) # 逐个元素进行max(0,element)
# array([2, 2, 3, 4])