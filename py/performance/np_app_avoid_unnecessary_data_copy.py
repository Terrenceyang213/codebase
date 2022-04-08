# tags: numpy, high performance, 
#%% avoid unnecessary array copies in order to save memory
import numpy as np


#%% check if two array share the same data buffer
# First, we need a way to check whether two arrays share the same underlying data buffer in memory. 
# Let's define a function aid() that returns the memory location of the underlying data buffer:


def aid(x):
    # This function returns the memory
    # block address of an array.
    return x.__array_interface__['data'][0]

a = np.zeros(3)
aid(a), aid(a[1:])
# (1940539423056, 1940539423064)

#%% stable verision
def get_data_base(arr):
    """For a given NumPy array, find the base array
    that owns the actual data.
    a1 = np.array([1,2,3])
    a1[1:].base = np.array([1,2,3])
    
    """
    base = arr
    while isinstance(base.base, np.ndarray):
        base = base.base
    return base


def arrays_share_data(x, y):
    return get_data_base(x) is get_data_base(y)

print(arrays_share_data(a, a.copy()))
# False

print(arrays_share_data(a, a[:1]))
# True

#%% example
# We may sometimes need to make a copy of an array; 
# for instance, if we need to manipulate an array 
# while keeping an original copy in memory:
import numpy as np
a = np.zeros(10)
ax = aid(a) # 地址
ax
# 1940560727456

b = a.copy()
aid(b) == ax

False

#%% 
# Array computations can involve in-place operations 
# (the first example in the following code: the array is modified) 
# or implicit-copy operations (the second example: a new array is created):
a *= 2 #in-place operation：节约时间
aid(a) == ax

True

c = a * 2 #imlicit-copy
aid(c) == ax

False

#%% Implicit-copy operations are slower, as shown here:
#\%%timeit:cell magic
# %timeit:line magic

%%timeit a = np.zeros(10000000)
a *= 2
# 100 loops, best of 3: 8.78 ms per loop

#%%
%%timeit a = np.zeros(10000000)
b = a * 2
# 10 loops, best of 3: 27.4 ms per loop


#%% Reshaping an array may or may not involve a copy. 
# The reasons will be explained in the How it works... section. 
# For instance, reshaping a 2D matrix does not involve a copy,
# unless it is transposed (or more generally, non-contiguous):
a = np.zeros((100, 100))
ax = aid(a)

b = a.reshape((1, -1))
aid(b) == ax

# True

c = a.T.reshape((1, -1)) #转置涉及拷贝
aid(c) == ax

# False
#%% Therefore, the latter instruction is significantly slower than the former:
%timeit b = a.reshape((1, -1))
# 1000000 loops, best of 3: 300 ns per loop


%timeit a.T.reshape((1, -1))
# 100000 loops, best of 3: 7.57 µs per loop

#%% Both the flatten() and the ravel() methods of an array 
# reshape it into a 1D vector (a flattened array). 
# However, the flatten() method always returns a copy, 
# and the ravel() method returns a copy only if necessary 
# (thus it's faster, especially with large arrays).

d = a.flatten()
aid(d) == ax
# False

e = a.ravel()
aid(e) == ax
# True

%timeit a.flatten()
# 100000 loops, best of 3: 2.51 µs per loop

%timeit a.ravel()
# 10000000 loops, best of 3: 185 ns per loop


#%% Broadcasting rules allow us to make computations on arrays with different but compatible shapes. 
# In other words, we don't always need to reshape 
# or tile our arrays to make their shapes match. 

# The following example illustrates two ways of 
# doing an outer product between two vectors: 
# the first method involves array tiling, 
# the second one (faster) involves broadcasting:
n = 1000

a = np.arange(n)
ac = a[:, np.newaxis]  # column vector
ar = a[np.newaxis, :]  # row vector

%timeit np.tile(ac, (1, n)) * np.tile(ar, (n, 1))
# 100 loops, best of 3: 6.06 ms per loop
%timeit ar * ac
# 1000 loops, best of 3: 1.62 ms per loop

#%% why numpy effient
# A NumPy array is basically described by metadata (notably the number of dimensions, the shape, and the data type) and the actual data. 
# 
# The data is stored in a homogeneous and contiguous block of memory, at a particular address in system memory (Random Access Memory, or RAM). 
# 
# This block of memory is called the data buffer. This is the main difference between an array and a pure Python structure, such as a list, where the items are scattered across the system memory. 
# 
# This aspect is the critical feature that makes NumPy arrays so efficient.

# In conclusion, storing data in a contiguous block of memory ensures that the architecture of modern CPUs is used optimally, in terms of memory access patterns, CPU cache, and vectorized instructions.


#%% 数据储存方式造成的速度差异
# numpy以rowmajor为主。
a = np.random.rand(5000, 5000)

%timeit a[0, :].sum()
# 100000 loops, best of 3: 4.23 µs per loop

%timeit a[:, 0].sum()
# 10000 loops, best of 3: 34.6 µs per loop