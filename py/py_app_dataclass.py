#%% 用类来保存数据
class Number:
    def __init__(self, val):
        self.val = val

one = Number(1)
one.val
# 1
one
# <__main__.Number at 0x27b298a6608>

# dataclass
# 自动赋值
# 自带__repr__
from dataclasses import dataclass

@dataclass
class dNum:
    val:int 

two = dNum(2)
two.val
# 2
two
# dNum(val=2)

#%% 数据比较
class Number:

    def __init__( self, val = 0):
       self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

a = Number(1)
b = Number(2)
c = Number(1)

a == b
# False
a == c
# True

a < b
# True
a > b
# False


# dataclass
# 当你使用dataclass(order = True)时，它会在类定义中添加函数__eq__和__lt__
# 相当于这样
# def __eq__(self, other):
#     return (self.val,) == (other.val,)

@dataclass(order = True)
class dNum:
    val:int = 0

da = dNum(1)    
db = dNum(2)
dc = dNum(1)

da == db
# False
da == dc
# True

da < db
# True
da < dc
# False

#%% dataclass 多个属性比较
# def __eq__(self, other):
#    return (self.name, self.age) == ( other.name, other.age)

# def __le__(self, other):
#     return (self.name, self.age) <= (other.name, other.age)


@dataclass(order = True)
class Person:
    name: str
    age:int = 0


#%%
import random
a = [dNum(random.randint(1,10)) for _ in range(10)]

# [dNum(val=3),
#  dNum(val=1),
#  dNum(val=5),
#  dNum(val=3),
#  dNum(val=3),
#  dNum(val=3),
#  dNum(val=5),
#  dNum(val=7),
#  dNum(val=3),
#  dNum(val=3)]

sorted_a = sorted(a)
sorted_a
# [dNum(val=1),
#  dNum(val=2),
#  dNum(val=2),
#  dNum(val=4),
#  dNum(val=7),
#  dNum(val=7),
#  dNum(val=7),
#  dNum(val=7),
#  dNum(val=8),
#  dNum(val=10)]

reverse_sorted_a = sorted(a, reverse = True)
reverse_sorted_a
# [dNum(val=10),
#  dNum(val=9),
#  dNum(val=7),
#  dNum(val=7),
#  dNum(val=6),
#  dNum(val=6),
#  dNum(val=3),
#  dNum(val=3),
#  dNum(val=2),
#  dNum(val=2)]


#%% dataclass dunder可选择
# @dataclass(init=True
#   , repr=True
#   , eq=True
#   , order=False
#   , unsafe_hash=False
#   , frozen=False)
# init：默认将生成__init__方法。如果传入False，那么该类将不会有__init__方法。
# repr：__repr__方法默认生成。如果传入False，那么该类将不会有__repr__方法。
# eq：默认将生成__eq__方法。如果传入False，那么__eq__方法将不会被dataclass添加，但默认为object.__eq__。
# order：默认将生成__gt__、__ge__、__lt__、__le__方法。如果传入False，则省略它们。


@dataclass(repr = False, eq=True) # order, unsafe_hash and frozen are False
class Number:
    val: int = 0

a = Number(1)
a
# <__main__.Number object at 0x7ff395afe898>
b = Number(2)
c = Number(1)
a == b
# False

a < b
# TypeError: '<' not supported between instances of 'Number' and 'Number'


#%% dataclass 不可变实体
# 常数
# 设置
# 这些通常不会在应用程序的生命周期内发生变化，任何企图修改它们的行为都应该被禁止

@dataclass(frozen = True)
class Number:
    val: int = 0
a = Number(1)
a.val
# 1

a.val = 2
# FrozenInstanceError: cannot assign to field 'val'


#%% 初始化后期处理
# 在初始化之后立即执行的操作
import math
class Float:
    def __init__(self, val = 0):
        self.val = val
        self.process()
    def process(self):
        self.decimal, self.integer = math.modf(self.val)
a = Float(2.2)
a.decimal
# 0.2000

a.integer
# 2.0


## dataclass 操作
import math
@dataclass
class FloatNumber:
    val: float = 0.0
    def __post_init__(self):
        self.decimal, self.integer = math.modf(self.val)
a = Number(2.2)
a.val
# 2.2

a.integer
# 2.0

a.decimal
# 0.2


#%% 继承
@dataclass
class Person:
    name: str
    age: int
    

@dataclass
class Student(Person):
    grade: int

s = Student(20, "John Doe", 12)
s.age
# 20

s.name
# "John Doe"
s.grade
# 12



#%% 继承中的__post_init__
@dataclass
class A:
    a: int
    def __post_init__(self):
        print("A")

@dataclass
class B(A):
    b: int
    def __post_init__(self):
        super().__post_init__()
        print("B")

a = B(1,2)
# A
# B


#%% dataclasses.field 定制化dataclass字段的行为以及它们在dataclass的影响
# 引入一个函数作为初始化的数据

import random
from typing import List
def get_random_marks():
    return [random.randint(1,10) for _ in range(5)]

@dataclass
class Student:
    marks: List[int] = list()

    def __post_init__(self):
        self.marks = get_random_marks() #assign random speeds

# a = Student()
# ValueError: mutable default <class 'list'> for field marks is not allowed: use default_factory

## default_factory 如果在创建对象时没有赋值，则使用该方法初始化该字段。
from dataclasses import field
@dataclass
class Student:
    marks: List[int] = field(default_factory= get_random_marks)

s = Student()
s.marks
# [2, 7, 6, 7, 7]



#%% 比较字段
@dataclass(order = True)
class user:
    name: str = field(compare=False) # compare = False
    age: int
    weight: float
    height: float

user_1 = user("John", 18, 75, 180)
# user(name='John', age=18, weight=75, height=180)
user_2 = user("Bob", 24,65,190)
user_1 < user_2
# True

(18,75,180)<(24,65,190)
# True

#%% 显示字段
@dataclass(order = True)
class user:
    name: str = field(compare=False,repr=False) # compare = False
    age: int
    weight: float
    height: float

user_1 = user("John", 18, 75, 180)
user_1
# user(age=18, weight=75, height=180)


#%% 忽略初始化
# 维护一个状态值，不需要提供初始化，而在后续修改这个值。
@dataclass
class user:
    email:str = field(repr=True)
    verified:bool = field(repr=False, init=False, default=False)

a = user('@qq.com')
a
# user(email='@qq.com')
a.verified
# False

