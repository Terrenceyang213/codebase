#%% tag:ml-prepare data using scikit-learn.
# from Jason Brownlee <> chapter 7
# rescale data
# standardize data
# normalize data
# binarize data


#%% tag:ml; rescale data, 调整数据尺度
## rescale data
## 通常将数据调整到0-1范围内

from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler # <>
from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
# 	preg	plas	pres	skin	test	mass	pedi	age	class
# 0	6	148	72	35	0	33.6	0.627	50	1
# 1	1	85	66	29	0	26.6	0.351	31	0
# 2	8	183	64	0	0	23.3	0.672	32	1
# 3	1	89	66	23	94	28.1	0.167	21	0
# 4	0	137	40	35	168	43.1	2.288	33	1

array = df.values   #<1> 转np.ndarray
X = array[:, 0:8]   #<2> 取前8列（preg-age）作为input
# array([[  6.   , 148.   ,  72.   ,  35.   ,   0.   ,  33.6  ,   0.627,   50.   ],
#        [  1.   ,  85.   ,  66.   ,  29.   ,   0.   ,  26.6  ,   0.351,   31.   ],
#        [  8.   , 183.   ,  64.   ,   0.   ,   0.   ,  23.3  ,   0.672,   32.   ],
#        [  1.   ,  89.   ,  66.   ,  23.   ,  94.   ,  28.1  ,   0.167,   21.   ],
#        [  0.   , 137.   ,  40.   ,  35.   , 168.   ,  43.1  ,   2.288,   33.   ]])

Y = array[:,8]      #<3> 取第9列（class）作为output
scaler = MinMaxScaler(feature_range=(0,1)) 
rescaledX = scaler.fit_transform(X) #<4> 重新标度
# array([[0.353, 0.744, 0.59 , 0.354, 0.   , 0.501, 0.234, 0.483],
#        [0.059, 0.427, 0.541, 0.293, 0.   , 0.396, 0.117, 0.167],
#        [0.471, 0.92 , 0.525, 0.   , 0.   , 0.347, 0.254, 0.183],
#        [0.059, 0.447, 0.541, 0.232, 0.111, 0.419, 0.038, 0.   ],
#        [0.   , 0.688, 0.328, 0.354, 0.199, 0.642, 0.944, 0.2  ]])

set_printoptions(precision=3,suppress=True) # 小数点三位，不使用科学计数法

# MinMaxScaler工作原理：使用列向量进行计算
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) #<> axis=0 在列向量中选取最小值
# X_scaled = X_std * (max - min) + min

# 常用的使用方法
## fit and transform：
### fit：Compute the minimum and maximum to be used for later scaling.
### transform:Scale features of X according to feature_range.
## fit_transform:Fit to data, then transform it.

# %% tag:ml; standardize data, 数据标准化
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions
from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
# 	preg	plas	pres	skin	test	mass	pedi	age	class
# 0	6	148	72	35	0	33.6	0.627	50	1
# 1	1	85	66	29	0	26.6	0.351	31	0
# 2	8	183	64	0	0	23.3	0.672	32	1
# 3	1	89	66	23	94	28.1	0.167	21	0
# 4	0	137	40	35	168	43.1	2.288	33	1

array = df.values   #<1> 转np.ndarray
X = array[:, 0:8]   #<2> 取前8列（preg-age）作为input
# array([[  6.   , 148.   ,  72.   ,  35.   ,   0.   ,  33.6  ,   0.627,   50.   ],
#        [  1.   ,  85.   ,  66.   ,  29.   ,   0.   ,  26.6  ,   0.351,   31.   ],
#        [  8.   , 183.   ,  64.   ,   0.   ,   0.   ,  23.3  ,   0.672,   32.   ],
#        [  1.   ,  89.   ,  66.   ,  23.   ,  94.   ,  28.1  ,   0.167,   21.   ],
#        [  0.   , 137.   ,  40.   ,  35.   , 168.   ,  43.1  ,   2.288,   33.   ]])

Y = array[:,8]      #<3> 取第9列（class）作为output

scaler = StandardScaler().fit(X) # <1> 使用fit and transform 方式
rescaledX = scaler.transform(X)
set_printoptions(precision=3,suppress=True)
print(rescaledX[0:5,:])
# [[ 0.64   0.848  0.15   0.907 -0.693  0.204  0.468  1.426]
#  [-0.845 -1.123 -0.161  0.531 -0.693 -0.684 -0.365 -0.191]
#  [ 1.234  1.944 -0.264 -1.288 -0.693 -1.103  0.604 -0.106]
#  [-0.845 -0.998 -0.161  0.155  0.123 -0.494 -0.921 -1.042]
#  [-1.142  0.504 -1.505  0.907  0.766  1.41   5.485 -0.02 ]]

rescaledX.mean(axis=0)
# array([-0., -0.,  0.,  0., -0.,  0.,  0.,  0.])

rescaledX.std(axis=0)
# array([1., 1., 1., 1., 1., 1., 1., 1.])

## 工作原理 
### The standard score of a sample x is calculated as:
### z = (x - u) / s



# %% tag:ml; normalize data; 规范化的数据
from sklearn.preprocessing import Normalizer
from pandas import read_csv
from numpy import set_printoptions
from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   #<1> 转np.ndarray
X = array[:, 0:8]   #<2> 取前8列（preg-age）作为input
# array([[  6.   , 148.   ,  72.   ,  35.   ,   0.   ,  33.6  ,   0.627,   50.   ],
#        [  1.   ,  85.   ,  66.   ,  29.   ,   0.   ,  26.6  ,   0.351,   31.   ],
#        [  8.   , 183.   ,  64.   ,   0.   ,   0.   ,  23.3  ,   0.672,   32.   ],
#        [  1.   ,  89.   ,  66.   ,  23.   ,  94.   ,  28.1  ,   0.167,   21.   ],
#        [  0.   , 137.   ,  40.   ,  35.   , 168.   ,  43.1  ,   2.288,   33.   ]])

Y = array[:,8]      #<3> 取第9列（class）作为output

scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
set_printoptions(precision=3,suppress=True)
print(normalizedX[0:5,:])
# [[0.034 0.828 0.403 0.196 0.    0.188 0.004 0.28 ]
#  [0.008 0.716 0.556 0.244 0.    0.224 0.003 0.261]
#  [0.04  0.924 0.323 0.    0.    0.118 0.003 0.162]
#  [0.007 0.588 0.436 0.152 0.622 0.186 0.001 0.139]
#  [0.    0.596 0.174 0.152 0.731 0.188 0.01  0.144]]

## 工作原理：将样本单独标准化为单位范数。 
## 每个样本（即数据矩阵的每一行）至少有一个非零分量独立于其他样本重新缩放，
## 它的范数（l1、l2 或 inf）等于 1。
### ?这个做了什么操作


# %% tag:ml; binarize data; 
from sklearn.preprocessing import Binarizer
from pandas import read_csv
from numpy import set_printoptions
from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   #<1> 转np.ndarray
X = array[:, 0:8]   #<2> 取前8列（preg-age）作为input
# array([[  6.   , 148.   ,  72.   ,  35.   ,   0.   ,  33.6  ,   0.627,   50.   ],
#        [  1.   ,  85.   ,  66.   ,  29.   ,   0.   ,  26.6  ,   0.351,   31.   ],
#        [  8.   , 183.   ,  64.   ,   0.   ,   0.   ,  23.3  ,   0.672,   32.   ],
#        [  1.   ,  89.   ,  66.   ,  23.   ,  94.   ,  28.1  ,   0.167,   21.   ],
#        [  0.   , 137.   ,  40.   ,  35.   , 168.   ,  43.1  ,   2.288,   33.   ]])
Y = array[:,8]      #<3> 取第9列（class）作为output

binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)
set_printoptions(precision=3,suppress=True)
print(binaryX[0:5,:])
# [[1. 1. 1. 1. 0. 1. 1. 1.]
#  [1. 1. 1. 1. 0. 1. 1. 1.]
#  [1. 1. 1. 0. 0. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1.]
#  [0. 1. 1. 1. 1. 1. 1. 1.]]

## 工作原理：Binarize data (set feature values to 0 or 1) according to a threshold.
## Values **greater than** the threshold map to 1, 
## while values **less than or equal to** the threshold map to 0. 
## With the default threshold of 0, only positive values map to 1.

# %%
