#%% 切片slicing：半开半闭区间

## 半开半闭区间通过一个坐标可以对序列进行切分
## 如：[:2],[2:]
s1 = [1,2,3,4,5]
s1[:2]
# [1, 2]
s1[2:]
# [3, 4, 5]

## 可以当提供起点和终点，可以直接算出长度，或个数
len(s1[:3])
# 3

len(s1[1:3])
# 2

#%% 对对象切片
## 完整切片语法：[start:stop:step]
s2 = 'abcedfg'
s2[1:7:3] #取得是坐标1，4
# 'bd' 

s2[::-1]
# 'gfdecba'

s2[::-2]
# 'gdca'

## 切片命名
text = '''0001  11111222223333344444  $17.89  10:21
0002  22222                  $1.22  11:22
0003  44444444444444444444  $10.00  12:55
'''

ID = slice(0,6)
DESC = slice(6,28)
PRIC = slice(28,36)
TIME = slice(36,None)
line_item = text.split('\n')
for item in line_item:
    print(item[ID])
    print(item[TIME])
    print(item[DESC])

#%% numpy
import numpy as np

s3 = np.arange(0,100)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
#        34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#        51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
#        68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
#        85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
s3[ID]
# array([0, 1, 2, 3, 4, 5])
s3[DESC]
# array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
    #    23, 24, 25, 26, 27])
s3[PRIC]
# array([28, 29, 30, 31, 32, 33, 34, 35])

# s3[ID,PRIC]
# IndexError: too many indices for array

## numpy中切片得特殊用法
### 多维切片
s4 = s3.reshape(20,5).copy()
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14],
#        [15, 16, 17, 18, 19],
#...
#        [90, 91, 92, 93, 94],
#        [95, 96, 97, 98, 99]])

s4[1:3,2:4]
# array([[ 7,  8],
    #    [12, 13]])2
Rslice = slice(1,3)
Cslice = slice(2,4)
s4[Rslice,Cslice]
# array([[ 7,  8],
#        [12, 13]])

### ...
### 如果s5 是4维的，s5[i,...] = s5[i,:,:,:]
s5 = s3.reshape((2,2,5,5))
# array([[[[ 0,  1,  2,  3,  4],
#          [ 5,  6,  7,  8,  9],
#          [10, 11, 12, 13, 14],
#          [15, 16, 17, 18, 19],
#          [20, 21, 22, 23, 24]],

#         [[25, 26, 27, 28, 29],
#          [30, 31, 32, 33, 34],
#          [35, 36, 37, 38, 39],
#          [40, 41, 42, 43, 44],
#          [45, 46, 47, 48, 49]]],


#        [[[50, 51, 52, 53, 54],
#          [55, 56, 57, 58, 59],
#          [60, 61, 62, 63, 64],
#          [65, 66, 67, 68, 69],
#          [70, 71, 72, 73, 74]],

#         [[75, 76, 77, 78, 79],
#          [80, 81, 82, 83, 84],
#          [85, 86, 87, 88, 89],
#          [90, 91, 92, 93, 94],
#          [95, 96, 97, 98, 99]]]])

s5[1,:,:,:]
# array([[[50, 51, 52, 53, 54],
#         [55, 56, 57, 58, 59],
#         [60, 61, 62, 63, 64],
#         [65, 66, 67, 68, 69],
#         [70, 71, 72, 73, 74]],

#        [[75, 76, 77, 78, 79],
#         [80, 81, 82, 83, 84],
#         [85, 86, 87, 88, 89],
#         [90, 91, 92, 93, 94],
#         [95, 96, 97, 98, 99]]])

s5[1,...]
# array([[[50, 51, 52, 53, 54],
#         [55, 56, 57, 58, 59],
#         [60, 61, 62, 63, 64],
#         [65, 66, 67, 68, 69],
#         [70, 71, 72, 73, 74]],

#        [[75, 76, 77, 78, 79],
#         [80, 81, 82, 83, 84],
#         [85, 86, 87, 88, 89],
#         [90, 91, 92, 93, 94],
#         [95, 96, 97, 98, 99]]])


#%% 切片赋值

s6 = s3.copy()
s6[:3]
# array([0, 1, 2])
s6[:3] = [2,1,0]
# array([2, 1, 0])

s6[:3] = 100
# array([100, 100, 100,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        # 13,  14,  15,  16, ...

s6[:3] = [100]
# array([100, 100, 100,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        # 13,  14,  15,  16,  17...

## list 与numpy的差别
s7=[1,2,3,4]
s7[1:3] = 100
# TypeError: can only assign an iterable
s7[1:3] = [100]
# [1, 100, 4]


#%% 支持切片的对象

class Myseq:

    def __getitem__(self, index):
        return index

s = Myseq()
s[1]
# 1

s[1:2]
# slice(1, 2, None)

s[1:10:2]
# slice(1, 10, 2)

s[1:10:2,3]
# (slice(1, 10, 2), 3)

s[1:10:2,1:3:1]
# (slice(1, 10, 2), slice(1, 3, 1))


dir(slice) #留意indice方法
# ['__class__',
#  '__delattr__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'indices',   ###
#  'start',     ###
#  'step',      ###
#  'stop']      ###

help(slice.indices)
# indices(...)

#     S.indices(len) -> (start, stop, stride)
#     
#     Assuming a sequence of length len, calculate the start and stop
#     indices, and the stride length of the extended slice described by
#     S. Out of bounds indices are clipped in a manner consistent with the
#     handling of normal slices.

slice(0,6).indices(3)
# (0, 3, 1)

slice(0,6).indices(10)
# (0, 6, 1)

# indices 中的参数是序列长度
slice(None,10,2).indices(5)
# (0, 5, 2)
# 'abcde'[:10:2] = 'abcde'[0:5:2]
'abcde'[:10:2] #'ace'
'abcde'[0:5:2] #'ace'

slice(-3,None,None).indices(5)
# (2, 5, 1)
# 'abced'[-3::] = 'abcde'[2:5:1]
'abced'[-3::]
# 'ced'
'abcde'[2:5:1]
# 'cde'