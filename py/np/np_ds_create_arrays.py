#%% 
import numpy as np

#%% Create from python object

data1d = np.array([1, 2, 3, 4])
data1d.ndim
# 1
data1d.shape
# (4,)

data2d=np.array([[1, 2], [3, 4]])
data2d.ndim
# 2
data2d.shape
# (2, 2)
data2d.strides
# (8, 4)

#%% Create np.array from constant value or increment value
a1 = np.zeros((2, 3))
a2 = np.ones(4)
a2.dtype
# dtype('float64') #这个是默认的类型

a2 = np.ones(4, dtype=np.int64)
a2.dtype
# dtype('int64')

x1 = 5.4 * np.ones(10)
# array([5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4])
x2 = np.full(10, 5.4)
# array([5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4, 5.4])


x1 = np.empty(5)
# array([1.45050748e-311, 3.37517338e+069, 5.11852009e-321, 1.44932313e-311,
    #    0.00000000e+000])
x1.fill(3.0)
# array([3., 3., 3., 3., 3.])
x2 = np.full(5, 3.0)
# array([3., 3., 3., 3., 3.])


np.arange(0.0, 10, 1)
# array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
np.linspace(0, 10, 11)
# array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])


#%% 对数坐标；Arrays filled with logarithmic sequences

np.logspace(0, 2, 5)  # 5 data points between 10**0=1 to 10**2=100
# array([1. , 3.16227766,  10., 31.6227766, 100. ])

#%% 未初始化的数组；np.empty
'''
创建数组但是不进行赋值，这种操作节省了初始化的时间，因此大型数组运算时有用。
该数组必须在赋值之后在引用。
'''
np.empty(3)
# array([1.45052476e-311, 0.00000000e+000, 1.19445286e+190])

#%% 根据其他数组的元数据创建np.array；
# np.oneslike, np.zeros_like, np.full_like,np.empty_like
'''
这种函数在特定场景中很常用
依照给定数组的元数据创建新的数组。
'''
def f(x):
    y = np.ones_like(x)
    # compute with x and y
    return y

f([1,2,3])
# array([1, 1, 1])
f(np.array([1,2,3]))
# array([1, 1, 1])
f(np.random.rand(5))
# array([1., 1., 1., 1., 1.])

#%% 创建矩阵数组；
# np.identity, np.eye,np.diag

np.identity(4)
# array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])

#np.eye可以选择偏移量的对角单位阵
np.eye(3, k=1)
# array([[0., 1., 0.],
#        [0., 0., 1.],
#        [0., 0., 0.]])
np.eye(3, k=-1)
# array([[0., 0., 0.],
#        [1., 0., 0.],
#        [0., 1., 0.]])

#np.diag可以创建任意对角阵，并且可以选择偏移量
np.diag(np.arange(0, 20, 5))
# array([[ 0,  0,  0,  0],
#        [ 0,  5,  0,  0],
#        [ 0,  0, 10,  0],
#        [ 0,  0,  0, 15]])

#无法控制元素个数。
np.diag(np.arange(0,20,5),k=1)
# array([[ 0,  0,  0,  0,  0],
#        [ 0,  0,  5,  0,  0],
#        [ 0,  0,  0, 10,  0],
#        [ 0,  0,  0,  0, 15],
#        [ 0,  0,  0,  0,  0]])