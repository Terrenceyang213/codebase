#%%
import numpy as np

### One-dimensional arrays

a = np.arange(0, 11)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
# index   0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10
# revesei-11 -10 -9  -8   -7  -6  -5  -4  -3  -2  -1                                           
a[0]  # the first element
# 0

a[-1] # the last element
# 10

a[4]  # the fifth element, at index 4
# 4

a[0:-1]
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[1:-1] #[1,-1)
# array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[:]
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

a[1:-1:2]
# array([1, 3, 5, 7, 9])

a[:5]
# array([0, 1, 2, 3, 4])

a[-5:]
# array([ 6,  7,  8,  9, 10])

a[::-2]
# array([10,  8,  6,  4,  2,  0])

a[-11]
# 0

#%% 多维数组:multidimension indexing and selecting

f = lambda m, n: n + 10 * m

A = np.fromfunction(f, (6, 6), dtype=int)

A
# array([[ 0,  1,  2,  3,  4,  5],
#        [10, 11, 12, 13, 14, 15],
#        [20, 21, 22, 23, 24, 25],
#        [30, 31, 32, 33, 34, 35],
#        [40, 41, 42, 43, 44, 45],
#        [50, 51, 52, 53, 54, 55]])

A[:, 1]  # the second column
# array([ 1, 11, 21, 31, 41, 51])

A[1, :]  # the second row
# array([10, 11, 12, 13, 14, 15])

A[:3, :3]  # upper half diagonal block matrix
# array([[ 0,  1,  2],
#        [10, 11, 12],
#        [20, 21, 22]])

A[3:, :3]  # lower left off-diagonal block matrix
# array([[30, 31, 32],
#        [40, 41, 42],
#        [50, 51, 52]])

A[::2, ::2]  # every second element starting from 0, 0
# array([[ 0,  2,  4],
#        [20, 22, 24],
#        [40, 42, 44]])


A[1::2, 1::3]  # every second element starting from 1, 1
# array([[11, 14],
#        [31, 34],
#        [51, 54]])

#%% 视图；view；别名
A = np.fromfunction(f, (6, 6), dtype=int)

A
# array([[ 0,  1,  2,  3,  4,  5],
#        [10, 11, 12, 13, 14, 15],
#        [20, 21, 22, 23, 24, 25],
#        [30, 31, 32, 33, 34, 35],
#        [40, 41, 42, 43, 44, 45],
#        [50, 51, 52, 53, 54, 55]])

B = A[1:5, 1:5]
# array([[11, 12, 13, 14],
#        [21, 22, 23, 24],
#        [31, 32, 33, 34],
#        [41, 42, 43, 44]])

B[:, :] = 0
A
# array([[ 0,  1,  2,  3,  4,  5],
#        [10,  0,  0,  0,  0, 15],
#        [20,  0,  0,  0,  0, 25],
#        [30,  0,  0,  0,  0, 35],
#        [40,  0,  0,  0,  0, 45],
#        [50, 51, 52, 53, 54, 55]])

C = B[1:3, 1:3].copy()
# array([[0, 0],
#        [0, 0]])


C[:, :] = 1  # this does not affect B since C is a copy of the view B[1:3, 1:3]
B
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]])


#%% 花式索引；高级索引；布尔值索引；
# Fancy indexing and Boolean-valued indexing
# 与切片得到的不同，花式索引得到的是全新的独立数组。

A = np.linspace(0, 1, 11)
# array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])

A[np.array([0, 2, 4])]
# array([0. , 0.2, 0.4])
A[[0, 2, 4]]
# array([0. , 0.2, 0.4])
A[range(0,5,2)]
# array([0, 2, 4])

# bool
A > 0.5 
# array([False, False, False, False, False, False,  True,  True,  True, True,  True])
A[A > 0.5]
# array([0.6, 0.7, 0.8, 0.9, 1. ])

# 花式索引在命名后会创建新的独立数组。
A = np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

indices = [2, 4, 6]
B = A[indices]
# array([2, 4, 6])
B[0] = -1  # t

A
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
B
# array([-1,  4,  6])

A[indices] = -1
# array([ 0,  1, -1,  3, -1,  5, -1,  7,  8,  9])