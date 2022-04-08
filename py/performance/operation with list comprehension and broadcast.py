#%%
import numpy as np

#%% 向量与常量的运算
# array:a; list:l
# broadcast:b; comprehension:c; foreach:f
# ab< lb< lc< ac< lf< af
def deviation(series, start, limit, mean):
    '''
    :type start: int
    :type limit: int
    :type mean: int
    :rtype: list()

    计算序列对均值的偏离值,其计算基础结构是list(),list没有广播功能。
    '''
    d = []
    for x in range(start, limit):
        d.append(float(series[x] - mean))
    return d

def deviation2(series, start, limit, mean):
    '''
    :type start: int
    :type limit: int
    :type mean: int
    :rtype: list()

    计算序列对均值的偏离值,其计算基础结构是list(),list没有广播功能。
    '''
    return [x - mean for x in series[start:limit]]

def deviation3(series, start, limit, mean):
    '''
    :type start: int
    :type limit: int
    :type mean: int
    :rtype: list()

    计算序列对均值的偏离值
    '''
    return np.array(series[start:limit]) - mean 

# 测试
# s1是np.array/ s2是list()
# 测试结果最快的是输入np.array并且使用broadcast.
s1 = np.random.random(100000)
s2 = list(s1)

print("\n deviation1, s1")
%timeit deviation(s1,5,100000, 100)

print("\n deviation2, s1")
%timeit deviation2(s1,5,100000, 100)

print("\n deviation3, s1")
%timeit deviation3(s1,5,100000, 100)

print("\n deviation1, s2")
%timeit deviation(s2,5,100000, 100)

print("\n deviation2, s2")
%timeit deviation2(s2,5,100000, 100)

print("\n deviation3, s2")
%timeit deviation3(s2,5,100000, 100)

#  deviation1, s1
# 10 loops, best of 3: 55.1 ms per loop
#  deviation2, s1
# 10 loops, best of 3: 33.6 ms per loop
#  deviation3, s1
# 1000 loops, best of 3: 611 µs per loop

#  deviation1, s2
# 10 loops, best of 3: 42.5 ms per loop
#  deviation2, s2
# 10 loops, best of 3: 28.2 ms per loop
#  deviation3, s2
# 100 loops, best of 3: 7.1 ms per loop

# %% 向量与向量的互操作
# list普遍较慢
# 最快的还是aa1
# ll操作最适合使用列表推导式
import numpy as np
import pandas as pd

def vectMinusVect(series1, series2):
    '''
    '''

    return series1 - series2

def vectMinusVect2(series1, series2):
    return [(x-y) for (x,y) in zip(series1, series2)]

sa = np.random.random(100000) # a
sl = list(sa) #l
sp = pd.Series(sa)

print("v1:aa")
%timeit vectMinusVect(sa,sa)

print("v1:al")
%timeit vectMinusVect(sa,sl)

print("v1:ll:error")
#%timeit vectMinusVect(sl,sl)

print("v1:pp")
%timeit vectMinusVect(sp,sp)

print("v1:ap")
%timeit vectMinusVect(sa,sp)

print("v1:lp")
%timeit vectMinusVect(sl,sp)

#########################################
print("v2:aa")
%timeit vectMinusVect2(sa,sa)

print("v2:al")
%timeit vectMinusVect2(sa,sl)

print("v2:ll")
%timeit vectMinusVect2(sl,sl)

print("v2:pp")
%timeit vectMinusVect2(sp,sp)

print("v2:ap")
%timeit vectMinusVect2(sa,sp)

print("v2:lp")
%timeit vectMinusVect2(sl,sp)

# v1:aa
# 10000 loops, best of 3: 36 µs per loop
# v1:al
# 100 loops, best of 3: 6.54 ms per loop
# v1:ll:
# error
# v1:pp
# 1000 loops, best of 3: 230 µs per loop
# v1:ap
# 1000 loops, best of 3: 261 µs per loop
# v1:lp
# 100 loops, best of 3: 7.12 ms per loop
#########################################
# v2:aa
# 10 loops, best of 3: 25.8 ms per loop
# v2:al
# 100 loops, best of 3: 18.6 ms per loop
# v2:ll
# 100 loops, best of 3: 11.6 ms per loop
# v2:pp
# 100 loops, best of 3: 19.4 ms per loop
# v2:ap
# 10 loops, best of 3: 31.6 ms per loop
# v2:lp
# 10 loops, best of 3: 22.7 ms per loop

# %%
