#%% tags:numpy;np;select data;index data;

#%% tags:numpy.where;np.where;
# usage: numpy.where(condition, [x, y, ])

# np.where is equal to 
# [xv if c else yv
#  for c, xv, yv in zip(condition, x, y)]

# 带参数
import numpy as np
a  = np.arange(5,15)
# array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

np.where(a < 5, a, 10*a)
# array([  5,   6,   7,   8,   9, 100, 110, 120, 130, 140])

# 不带参数返回的满足条件的索引
np.where(a<10)
# (array([0, 1, 2, 3, 4], dtype=int64),)

#二维情况
d2 = np.random.randint(-5,10,size=(4,4))
print(d2)
# [[-5  1  9  1]
#  [ 0  9 -5  4]
#  [ 0  1  7  7]
#  [-1  3  7  5]]

np.where(d2>0) # 返回的是axis0的索引和axis1的索引
# (array([0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3], dtype=int64),
#  array([1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3], dtype=int64))

# 高维情况
np.where([[True, False], 
          [True, True]])
# (array([0, 1, 1], dtype=int64), 
#  array([0, 0, 1], dtype=int64))


np.where([[True, False], 
          [True, True]],

         [[1, 2], 
          [3, 4]], # matx

         [[9, 8], 
          [7, 6]]) # maty
# condition中为真的位置取matx，假的取maty