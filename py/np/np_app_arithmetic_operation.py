#%% 
import numpy as np

#%% operation with same shape;相同结构的数学运算；广播

x = np.array([[1, 2], [3, 4]]) 
# array([[1, 2],
#        [3, 4]])

y = np.array([[5, 6], [7, 8]])
# array([[5, 6],
#        [7, 8]])

x + y
# array([[ 6,  8],
#        [10, 12]])

y - x
# array([[4, 4],
#        [4, 4]])

x * y
# array([[ 5, 12],
#        [21, 32]])

y / x
# array([[5.        , 3.        ],
#        [2.33333333, 2.        ]])

x * 2
# array([[2, 4],
#        [6, 8]])

2 ** x
# array([[ 2,  4],
#        [ 8, 16]], dtype=int32)

y / 2
# array([[2.5, 3. ],
#        [3.5, 4. ]])

(y / 2).dtype
# dtype('float64')

#%%
x = np.array([1, 2, 3, 4]).reshape(2,2)
# array([[1, 2],
#        [3, 4]])
z = np.array([1, 2, 3, 4])
# array([1, 2, 3, 4])

x / z
# ValueError: operands could not be broadcast together with shapes (2,2) (4,) 

z = np.array([[2, 4]])
# array([[2, 4]])
z.shape

x / z

zz = np.concatenate([z, z], axis=0)

zz

x / zz

z = np.array([[2], [4]])

z.shape

x / z

zz = np.concatenate([z, z], axis=1)

zz

x / zz

x = np.array([[1, 3], [2, 4]])
x = x + y
x

x = np.array([[1, 3], [2, 4]])
x += y
x