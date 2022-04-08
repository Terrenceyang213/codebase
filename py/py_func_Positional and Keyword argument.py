#%% 函数参数的顺序，order of arguments of a function
# 定位参数与关键字参数在函数定义时应当遵循的顺序：
# 1 定位参数      a,b,c
# 2 变长的定位参数 *args
# 3 关键字参数    kw = 'a'
# 4 变长的关键字参数 **kwargs
# 
def f(positional, *args, 
      kwarg = None, **kwargs):
    
    print('posi:'+str(positional))
    
    if args:
        print('args:'+str(args))
        
    print('kw:'+str(kwarg))
    
    if kwargs:
        print('kwargs:'+str(kwargs))


f(1)
# posi:1
# kw:None

f(1,2,3)
# posi:1
# args:(2, 3)
# kw:None

f(1,2,kw='hello')
# posi:1
# args:(2,)
# kw:hello

f(1,'a', 'b',a=1, b=2)
# posi:1
# args:('a', 'b')
# kw:None
# kwargs:{'a': 1, 'b': 2}

f(1,'a', 'b',a=1, b=2,kw='hello')
# posi:1
# args:('a', 'b')
# kw:hello
# kwargs:{'a': 1, 'b': 2}


# %% 参数的输入方式影响函数以定位参数还是关键字参数进行接受
def decor(func):
    
    def wrapper(*args, **kwargs):
    
        if args:
            print('args:'+str(args))
            
        if kwargs:
            print('kwargs:'+str(kwargs))
        
        return func(*args, **kwargs)
    
    return wrapper

@decor
def foo(a=1,b=2,c=3):
    print((a,b,c))

foo()
# 装饰器未打印任何参数，也就是说args和kwargs都是空的
# foo在真正执行时才使用默认值
# 1, 2, 3

foo(b=1,a=2,c=3)
#装饰器将所有参数当作关键字参数
# kwargs:{'b': 1, 'a': 2, 'c': 3}
# 2 1 3


foo(1,c=5,b=6)
# args:(1,)
# kwargs:{'c': 5, 'b': 6}
# 1 6 5

# 关键字参数与定位参数之间的关系
# 不指定参数名称时，直接当作定位参数处理

foo(1,a=1,c=3)
# args:(1,)
# kwargs:{'a': 1}
# TypeError: foo() got multiple values for argument 'a'

# %%
