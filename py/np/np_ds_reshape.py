#%% 
import numpy as np

#%%
## Reshaping and resizing

data = np.array([[1, 2], [3, 4]])
# array([[1, 2],
#        [3, 4]])

np.reshape(data, (1, 4))
# array([[1, 2, 3, 4]]) # 依旧是二维
data.reshape(4)
# array([1, 2, 3, 4]) #降维了



data = np.array([[1, 2], [3, 4]])
# array([[1, 2],
#        [3, 4]])

data.flatten()
# array([1, 2, 3, 4])
data.flatten().shape
# (4,)


#%% add new axis
data = np.arange(0, 5)
# array([0, 1, 2, 3, 4])

column = data[:, np.newaxis]
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4]])

row = data[np.newaxis, :]
# array([[0, 1, 2, 3, 4]])


#%% 堆叠新的矩阵

data = np.arange(5)
# array([0, 1, 2, 3, 4])


np.vstack((data, data, data))
# array([[0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4]])



data = np.arange(5)
# array([0, 1, 2, 3, 4])

np.hstack((data, data, data))
# array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])

data = data[:, np.newaxis]
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4]])

np.hstack((data, data, data))
# array([[0, 0, 0],
#        [1, 1, 1],
#        [2, 2, 2],
#        [3, 3, 3],
#        [4, 4, 4]])

#%%
data = np.eye(3)
data
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])

np.hstack((data, data, data))
# array([[1., 0., 0., 1., 0., 0., 1., 0., 0.],
#        [0., 1., 0., 0., 1., 0., 0., 1., 0.],
#        [0., 0., 1., 0., 0., 1., 0., 0., 1.]])