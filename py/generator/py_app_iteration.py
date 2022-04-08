# %% [markdown]
# # Generator Tricks for Systems Programmers
# ## 1. Iteration 
# ### 1.1 Iterates list
# %% use for statement iterates collection
# end: string appended after the last value
# , default a newline '\n'.
for x in [1,4,5,6,10]:
    print(x,end=' ')
# 1 4 5 6 10

#%% [markdown]
### 1.2 Iterate dicts
#%% 
prices = {  'GOOG':490.10,
            'AAPL':145.23,
            'YHOO':21.71}
for key in prices:
    print(key)
# GOOG
# AAPL
# YHOO

# %% [markdown]
# ### 1.3 Iterating over a String
#%%
s = "Yow!"
for c in s:
    print(c,end=' ')
# Y o w !

# %% [markdown] 
# ### 1.4 Iterating over a File
#%%
for line in open("./src/real.txt"):
    print(line, end='') # <1> 
# ab.c
# adsf

# adsf
# sd

# <1> 一定要end=''，print才不会插入多余的换行。

# %% [markdown] 
# ### 1.5 Consuming Iterables
# Many operations consume an "iterable" object
# Reductions: sum(s), min(s), max(s) 
# Constructors: list(s), tuple(s), set(s), dict(s)
# Various operators: item in s

# %% [markdown]
# ### 1.6 Iteration Protocol
#%% Iteration Protocol
items = [1, 4, 5] 
it = iter(items)
it.__next__() 
# 1
it.__next__() 
# 4
it.__next__()
# 5 
it.__next__()
# StopIteration: 

# %% [markdown] Under the cover of for statement
# for x in obj:
#   statement

# underneath the covers
# _iter = iter(obj)             # Get iterator object
# while 1:
#   try:
#       x = _iter.__next__()    # Get next item
#   except StopIteration:       # No more iterms
#       break
#   #statements

# %% [markdown] iterable
# Any object that supports iter() is said to be "iterable."

# %% [markdown]
# ### 1.7 Supporting Iteration
# User-defined objects can support iteration
# To do this, you have to make the object implement __iter__() and __next__()
# __iter__(): Iterable object
# __iter__(), __next__(): Iterator
#%%
class countdown(object):
    '''
    Iterable countdown object
    '''
    def __init__(self, start):
        self.start = start

    def __iter__(self): # <1> 
        return countdown_iter(self.start)

class countdown_iter(object):
    '''
    Iterator? only __next__ realised
    '''
    def __init__(self, count):
        self.count = count

    def __next__(self): # <2> next函数是需要返回一个确切值的。
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

for x in countdown(10):
    print(x, end=' ')
# 10 9 8 7 6 5 4 3 2 1


# %% [markdown]
# ## 2. Generator
# ### 2.1 Generator Function
# A generator is a function that produces a sequence of results instead of a single value
#%%
def countdown(n):
    print(f'Counting down from {n}')
    while n > 0:
        yield n
        n -= 1
    
for i in countdown(5):
    print(i, end=' ')
# Counting down from 5
# 5 4 3 2 1

# <1> 创建生成器不执行函数
x = countdown(10) 
x 
# <generator object countdown at 0x000001902183E6C8>

# <2> function only executes on __next__()
x.__next__()
# 10

# <3> yield produces a value, but suspends the function
# <3> Function resumes on next call to __next__()
x.__next__()
# 9
x.__next__()
# 8
# ...
x.__next__()
# 1
x.__next__()
# StopIteration

#%% [markdown]
# ### 2.2 Generators vs. Iterators
# 生成器只能访问一次，可迭代对象如list可多次迭代
#%% 生成器表达式版本的列表表达式
a = [1,2,3,4]
b = (2*x for x in a)
b
# <generator object <genexpr> at 0x000001902187B8C8>
for i in b:
    print(i, end=' ')
# 2 4 6 8
#%% 
a = [1,2,3,4]
b = [2*x for x in a] # <1> list
b 
# [2, 4, 6, 8]
c = (2*x for x in a) # <2> generator
c 
# <generator object <genexpr> at 0x000001902189B548>

#%% [markdown] 生成器表达式
# ### 2.3 Generator Expressions

# (expression for i in s if condition)

# This is equal to
# for i in s:
#   if condition:
#       yield expression

# 当作为唯一参数传递给函数时，括号可以省略
# sum( x*x for x in s )
#%% Generator functions
def countdown(n):
    while n > 0:
        yield n
        n -= 1
#%% Generator expressions
squares = (x*x for x in s)


#%% [markdown]
# # Part 2 Processing Data Files
# ## 1. Programming Problem
# Find out how many bytes of data were transferred 
# by summing up the last column of data in this Apache web server log

#%% [markdown]
# ## 2 The Log File
# Each line of the log looks like this:
81.107.39.38 - ... "GET /ply/ply.html HTTP/1.1" 200 97238
# The number of bytes is the last column
bytes_sent = line.rsplit(None,1)[1]
# It's either a number or a missing value (-)
81.107.39.38 - ... "GET /ply/ HTTP/1.1" 304 -
# Converting the value
if bytes_sent != '-':
    bytes_sent = int(bytes_sent)

#%% [markdown]
# ## 3. A Non-Generator Soln
#%% simple for-loop : 0 ns
with open("C:\\base\\codebase\\python\\books\\dabeaz\\Generators\\www\\bar\\access-log") as wwwlog:
    total = 0
    for line in wwwlog:
        bytes_sent = line.rsplit(None,1)[1]
        if bytes_sent != '-':
            total += int(bytes_sent)
    print(f'Total:{total}')

#%% A Generator Solution: 0 ns
%time
with open("C:\\base\\codebase\\python\\books\\dabeaz\\Generators\\www\\bar\\access-log") as wwwlog:
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
    bytes_sent = (int(x) for x in bytecolumn if x!= '-')
    print("Total:{!r}".format(sum(bytes_sent)))

#%% [markdown]
# ## 4. A Pipeline
# access-log -> wwwlog -> bytecolumn -> bytes_sent -> sum() -> total
# each step is defined by iteration/generation

# ### 4.1 Being Declarative
# 每个阶段都声明一个应用于整个数据流的操作

# ### 4.2 Iteration is the Glue
# The glue that holds the pipeline together is the iteration that occurs in each step

#%% [markdown]
# # Part 3 Fun with Files and Directories
# ## 1. Programming Problem
# You have hundreds of web server logs scattered across various directories. 
# In additional, some of the logs are compressed. Modify the last program 
# so that you can easily read all of these logs

#%% 查找文件path，使用的生成器
from pathlib import Path
for filename in Path('C:\\base').rglob('*.py'):
    print(filename) # <1> filename包含路径

# C:\base\codebase\algorithm\quicksort.py
# C:\base\codebase\leetcode\455-assign cookies.py
# C:\base\codebase\leetcode\53-Maximum Subarray.py
# C:\base\codebase\mq5\copy ranges.py
# C:\base\codebase\mq5\download.py

Path('C:\\base').rglob('*.py')
# <generator object Path.rglob at 0x000002A66B36A5C8>

#%% [markdown]
# ## A File Opener
# open a sequence of paths
import gzip, bz2
def gen_open(paths):
    for path in paths:
        if path.suffix == '.gz':
            yield gzip.open(path, 'rt')
        elif path.suffix == '.bz2':
            yield bz2.open(path, 'rt')
        else:
            yield open(path, 'rt')
# it takes a sequence of paths as input 
# and yields a sequence of open file objects

#%% [markdown]
# # Part 4 Parsing and Processing Data
#%%
import re
loglines = open("C:\\base\\codebase\\python\\books\\dabeaz\\Generators\\www\\bar\\access-log")



logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

groups   = (logpat.match(line) for line in loglines)
tuples   = (g.groups() for g in groups if g)
#%%
s = '140.180.132.213 - - [24/Feb/2008:00:08:59 -0600] "GET /ply/ply.html HTTP/1.1" 200 97238'
g = logpat.match(s)
# <re.Match object; span=(0, 87), match='140.180.132.213 - - [24/Feb/2008:00:08:59 -0600] >
g.groups()
# ('140.180.132.213',
#  '-',
#  '-',
#  '24/Feb/2008:00:08:59 -0600',
#  'GET',
#  '/ply/ply.html',
#  'HTTP/1.1',
#  '200',
#  '97238')

# %% [markdown] 
# ## Re-dict
#%%
loglines = open("access-log")

import re

logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
           r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

logpat   = re.compile(logpats)

groups   = (logpat.match(line) for line in loglines) # <1> 
tuples   = (g.groups() for g in groups if g) # <2>
colnames = ('host','referrer','user','datetime',
            'method', 'request','proto','status','bytes')

log      = (dict(zip(colnames, t)) for t in tuples) # <3> 
#%%
# <1>
s = '140.180.132.213 - - [24/Feb/2008:00:08:59 -0600] "GET /ply/ply.html HTTP/1.1" 200 97238'
g = logpat.match(s)
# <re.Match object; span=(0, 87), match='140.180.132.213 - - [24/Feb/2008:00:08:59 -0600] >

# <2>
t = g.groups()
# ('140.180.132.213',
#  '-',
#  '-',
#  '24/Feb/2008:00:08:59 -0600',
#  'GET',
#  '/ply/ply.html',
#  'HTTP/1.1',
#  '200',
#  '97238')

# <3>
zip(colnames,t)
# <zip at 0x18840854388>

for x,y in zip(colnames,t):
    print(f'{x}:{y}')
# host:140.180.132.213
# referrer:-
# user:-
# datetime:24/Feb/2008:00:08:59 -0600
# method:GET
# request:/ply/ply.html
# proto:HTTP/1.1
# status:200
# bytes:97238

dict(zip(colnames,t))
# {'host': '140.180.132.213',
#  'referrer': '-',
#  'user': '-',
#  'datetime': '24/Feb/2008:00:08:59 -0600',
#  'method': 'GET',
#  'request': '/ply/ply.html',
#  'proto': 'HTTP/1.1',
#  'status': '200',
#  'bytes': '97238'}

# %% [markdown] 
# ## 封装

# %% [markdown] 
# # Part 5
# ## Processing Infinite Data
# %% [markdown] 
# # Part 6
# ## Feeding Generators
