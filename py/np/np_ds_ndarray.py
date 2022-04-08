#%% what is ndarray
# ndarray = block of memory + indexing scheme + data type descriptor
import numpy as np

# typedef struct PyArrayObject {
#         PyObject_HEAD

#         /* Block of memory */
#         char *data;

#         /* Data type descriptor */
#         PyArray_Descr *descr;

#         /* Indexing scheme */
#         int nd;
#         npy_intp *dimensions;
#         npy_intp *strides;

#         /* Other stuff */
#         PyObject *base;
#         int flags;
#         PyObject *weakreflist;
# } PyArrayObject;

#%% Block of memory
x = np.array([1, 2, 3], dtype=np.int32)
x.data      
# <memory at 0x000002770247CB88>
bytes(x.data) 
# b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'

# Memory Address
x.__array_interface__['data'][0] 
# 2712258260512

# array interface
x.__array_interface__
# {'data': (2712258260512, False),
#  'strides': None,
#  'descr': [('', '<i4')],
#  'typestr': '<i4',
#  'shape': (3,),
#  'version': 3}

#%% x is a string (in Python 3 a bytes), 
# we can represent its data as an array of ints:
x = b'1234'
y = np.frombuffer(x, dtype=np.int8)
# array([49, 50, 51, 52], dtype=int8)
y.data      
# <memory at 0x000002770247CC48>

y.base is x
# True

y.flags
#  C_CONTIGUOUS : True
#   F_CONTIGUOUS : True
#   OWNDATA : False
#   WRITEABLE : False
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
#   UPDATEIFCOPY : False

# The owndata and writeable flags 
# indicate status of the memory block.

#%% dtype
np.dtype(int).type      
# numpy.int32

np.dtype(int).itemsize
# 4

np.dtype(int).byteorder
# '='