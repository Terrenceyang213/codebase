#%% 
import numpy as np

#%% Casting in general copies data:
x = np.array([1, 2, 3, 4], dtype=np.float)
x
# array([1., 2., 3., 4.])
#%%
y = x.astype(np.int8)
y
# array([1, 2, 3, 4], dtype=int8)
#%%
y + 1
# array([2, 3, 4, 5], dtype=int8)

#%%
y + 256
# array([257, 258, 259, 260], dtype=int16)

#%%
y + 256.0
# array([257., 258., 259., 260.]) #dtype('float64')

#%%
y + np.array([256], dtype=np.int32)
# array([257, 258, 259, 260], dtype=np.int32)


#%% Casting on setitem: dtype of the array is not changed on item assignment:
y
# array([1, 2, 3, 4], dtype=int8)
y[:] = y + 1.5
y
# array([2, 3, 4, 5], dtype=int8)


#%% switch dtype with the same data memory

# Data block in memory (4 bytes)
#  0x01 || 0x02 || 0x03 || 0x04

#     4 of uint8, OR,
#     4 of int8, OR,
#     2 of int16, OR,
#     1 of int32, OR,
#     1 of float32, OR,
#     …
x = np.array([1, 2, 3, 4], dtype=np.uint8)
# array([1, 2, 3, 4], dtype=uint8)

x.dtype = "<i2"
x
# array([ 513, 1027], dtype=int16)

0x0201, 0x0403
# (513, 1027)

x.dtype = "<i4"
x
# 67305985

0x04030201
# 67305985

#%% create view to switch dtype
# .view() makes views, does not copy (or alter) the memory block
# only changes the dtype (and adjusts array shape):

y = x.view("<i4")
y
# 67305985

0x04030201
# 67305985
    
x[1] = 5
y
# array([328193])


y.base is x
# True