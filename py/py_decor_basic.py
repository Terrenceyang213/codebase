#!/usr/bin/env python
# coding: utf-8


#%% 空装饰器
def null_decorator(func):
    return func

# 装饰器的运作
def foo():
    return 'Hello world!'

foo = null_decorator(foo)
foo()

# 空装饰器使用形式
@null_decorator
def greet():
    return 'greet!'

greet()
# 'greet!'



#%% 影响函数行为的装饰器
def uppercase(func):
    
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'greet'

greet()
# 'GREET'


# In[7]:


#%% 空装饰器和uppercase会返回不同的函数对象
foo

null_decorator(foo)

uppercase(foo)


# In[11]:


#%% 多个装饰器
def d1(func):
    def wrapper():
        return 'd1 '+func()+' d1'
    return wrapper

def d2(func):
    def wrapper():
        return 'd2 '+func()+' d2'
    return wrapper

@d1
@d2
def greet():
    return 'Hello'

greet()
# 'd1 d2 Hello d2 d1'


#这种定义相当于
d_greet = d1(d2(foo))
d_greet()





#%% 接受参数的装饰器
# 这个装饰器在wrapper闭包定义中用*，**操作符收集所有的位置参数和关键字参数，将其存放在args和kwargs变量中
# wrapper闭包使用*，**参数解包操作符将收集的参数转发到原输入函数func
def proxy(func):
    
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    return wrapper

@proxy
def greet(a,b=2):
    return a+str(b)

greet('a',1)
# 'a1'



#%% 对proxy扩展
def trace(func):
    
    def wrapper(*args, **kwargs):
        print(f'Trace: calling {func.__name__}()'
              f'with {args},{kwargs}'
                )
        
        original_result = func(*args, **kwargs)
        
        print(f'Trace: calling {func.__name__}()'
              f'returned {original_result!r}'
                )       
        
        return original_result
    return wrapper

@trace
def say(name,line):
    return f'{name}:{line}'

say('jane','hello')



#%% 保存被装饰函数的元数据

# 被直接装饰的函数会丢失__name__,__doc__
def greet():
    '''return a hello'''
    return 'hello!'

decorated_greet = uppercase(greet)

greet.__name__
# 'return a hello'
greet.__doc__
# 'return a hello'

decorated_greet.__name__
# 'wrapper'
decorated_greet.__doc__
# None



#%% 使用functools可以保留
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    '''return a hello!'''
    return 'Hello!'

greet.__name__
# 'greet'
greet.__doc__
# 'return a hello!'

#%% 实现一个用来计时的装饰器
from functools import wraps
from time import time,sleep


def tu(fmt = '[{elapsed:0.8f}s] {funcname}({args},{kwargs}) -> {result}'):
    
    def decor(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):

            start = time()
            original_result = func(*args, **kwargs)
            elapsed = time() - start

            funcname = func.__name__
            result = repr(original_result)
            print(fmt.format(**locals()))
            
            return original_result
        
        return wrapper
    
    return decor

@tu()  # <11>
def snooze(a,b,c='a',d=None):
    sleep(a)
    return 'hello world'

snooze(2)
# [2.01306009s] snooze((2,),{}) -> 'hello world'
# 'hello world'