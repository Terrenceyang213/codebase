# 如果生成器函数需要产出另一个生成器生成的值，传统的解决方法是使用嵌套的 for 循环。

# %% 用作协程的生成器的基本行为
# 从句法上看，协程与生成器类似，都是定义体中包含 yield 关键字的函数。
# 可是，在协程中，yield通常出现在表达式的右边（例如，datum = yield），
# 可以产出值，也可以不产出——如果 yield 关键字后面没有表达式，那么生成器产出 None。
# 协程可能会从调用方接收数据，不过调用方把数据提供给协程使用的是 .send(datum) 方法，
# 而不是 next(...) 函 数。
# 通常，调用方会把值推送给协程。 yield关键字甚至还可以不接收或传出数据。
# 不管数据如何流动，yield 都是一种流程控制工具，
# 使用它可以实现协作式多任务：协程可以把控制器让步给中心调度程序，从而激活其他的协程。
# 从根本上把 yield 视作控制流程的方式，这样就好理解协程了。

def simple_coroutine():
    print('-> coroutine started')
    # yield 在表达式中使用；如果协程只需从客户那里接收数据，那么产出的值是 None
    # —— 这个值是隐式指定的，因为 yield 关键字右边没有表达式。
    x = yield
    print('-> coroutine received:',x)

my_coro = simple_coroutine()
my_coro
# <generator object simple_coroutine at 0x0000028A2B380148>

# 首先要调用 next(...) 函数，因为生成器还没启动，没在yield语句处暂停，所以一开 始无法发送数据
next(my_coro)
# coroutine started

# 调用这个方法后，协程定义体中的yield表达式会计算出 42；
# 现在，协程会恢复，一直运行到下一个yield表达式，或者终止
my_coro.send(42)
# coroutine received: 42

# 这里，控制权流动到协程定义体的末尾，导致生成器像往常一样抛出 StopIteration 异常。
# StopIteration

# %% 协程的四种状态
# 'GEN_CREATED' 等待开始执行。 
# 'GEN_RUNNING' 解释器正在执行。
# 'GEN_SUSPENDED' 在 yield 表达式处暂停。 
# 'GEN_CLOSED'执行结束。

import inspect
my_coro = simple_coroutine()
print(inspect.getgeneratorstate(my_coro))
# GEN_CREATED

next(my_coro)
# -> coroutine started
print(inspect.getgeneratorstate(my_coro))
# GEN_SUSPENDED

my_coro.send(42)
# -> coroutine received: 42
# StopIteration
print(inspect.getgeneratorstate(my_coro))
# GEN_CLOSED

# 因为 send 方法的参数会成为暂停的 yield 表达式的值，
# 所以，仅当协程处于暂停状态时才 能调用 send 方法，例如 my_coro.send(42)。
# 不过，如果协程还没激活（即，状态是 'GEN_ CREATED'），情况就不同了。
# 因此，始终要调用 next(my_coro) 激活协程——也可以调用
# my_coro.send(None)，效果一样。

# %% 如果创建协程对象后立即把 None 之外的值发给它，会出现下述错误

my_coro = simple_coroutine()
my_coro.send(42)
# TypeError: can't send non-None value to a just-started generator

# 最先调用 next(my_coro) 函数这一步通常称为“预激”（prime）协程
# （即，让协程向前执 行到第一个 yield 表达式，准备好作为活跃的协程使用）。


#%% 产生两个值的协程 **** b = yield a 会被挂起操作分割成两个语句
# b = yield a 相当于
# yield a
# suspend
# b = yield
from inspect import getgeneratorstate
def simple_coro2(a):
    print('-> Started: a=', a)
    b = yield a
    print('-> Received: b=', b)
    c = yield a+b
    print('-> Received: c=', c)

my_coro2 = simple_coro2(14)
getgeneratorstate(my_coro2)
# GEN_CREATED

next(my_coro2)
# 1 print: -> Started: a= 14
# 2 yield a: 14
# 3 暂停，等待为b赋值：b = yield

getgeneratorstate(my_coro2)
# GEN_SUSPENDED

my_coro2.send(28)
# 1 为b赋值: b=28
# 2 print: -> Received: b= 28
# 3 yield a+b: 42

my_coro2.send(99)
# 1 等待赋值：c = 99
# 2 print: -> Received: c= 99
# 3 StopIteration

getgeneratorstate(my_coro2) 
# 'GEN_CLOSED'

# 关键的一点是，协程在 yield 关键字所在的位置暂停执行。
# 前面说过，在赋值语句中，= 右边的代码在赋值之前执行。
# 因此，对于b = yield a这行代码来说，等到客户端代码再激活协程时才会设定 b 的值。

# %% 使用协程计算移动平均数
def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # <1>
        term = yield average  # <2>
        total += term
        count += 1
        average = total/count

coro_avg = averager()
next(coro_avg)
# 1 调用到 yield average: none
# 2 暂停，等待赋值：term = yield

coro_avg.send(10)
# 10
coro_avg.send(20)
# 15
coro_avg.send(30)
# 20

# %% 协程的启动：预激装饰器
from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args,**kwargs):  # <1>
        gen = func(*args,**kwargs)  # <2>
        next(gen)  # <3>
        return gen  # <4>
    return primer

@coroutine
def averager1():
    total = 0.0
    count = 0
    average = None
    while True:  # <1>
        term = yield average  # <2>
        total += term
        count += 1
        average = total/count

coro_avg = averager1()   

coro_avg.send(10)
# 10
coro_avg.send(20)
# 15
coro_avg.send(30)
# 20


# %% 协程终止与异常处理

coro_avg = averager1()
coro_avg.send(40)
# 40.0

coro_avg.send(50)
# 45.0

coro_avg.send('spam')
# TypeError: unsupported operand type(s) for +=: 'float' and 'str'
# 由于在协程内没有处理异常，协程会终止。如果试图重新激活协程，会抛出 StopIteration 异常。



#%% 上例暗示了终止协程的一种方式：发送某个哨符值，让协程退出。
# 内置的 None 和 Ellipsis 等常量经常用作哨符值。
# Ellipsis 的优点是，数据流中不太常有这个值。
# 我还见 过有人把 StopIteration 类（类本身，而不是实例，也不抛出）作为哨符值；
# 也就是说是像这样使用的：my_coro.send(StopIteration)。

# 另外两个终止的方法
# generator.throw(exc_type[, exc_value[, traceback]])
# generator.close()

class DemoException(Exception):
    """An exception type for the demonstration."""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:  # <1>
            print('*** DemoException handled. Continuing...')
        else:  # <2>
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')  # <3>

exc_coro = demo_exc_handling()
next(exc_coro)
# -> coroutine started

exc_coro.send(11)
# -> coroutine received: 11

exc_coro.throw(DemoException) #exc_coro.throw(ZeroDivisionError) # 如果是其他的异常，协程就会结束
# *** DemoException handled. Continuing...
getgeneratorstate(exc_coro)
# GEN_SUSPENDED

exc_coro.send(22)
# -> coroutine received: 22

exc_coro.close()
from inspect import getgeneratorstate
getgeneratorstate(exc_coro)
# 'GEN_CLOSED'

# %% 协程使用 try/finnally控制流程结束
# 如果不管协程如何结束都想做些清理工作，要把协程定义体中相关的代码放入 try/ finally 块中
class DemoException(Exception):
    """An exception type for the demonstration."""


def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

#%% 让协程返回值
# averager 协程的不同版本，这一版会返回结果。为了说明如何返回值，每次激活协程时不会产出移动平均值。
# 这么做是为了强调某些协程不会产出值，而是在最后返回一个值（通常是某种累计值）

# averager 协程返回的结果是一个 namedtuple，两个字段分别是项数 （count）和平均值（average）。
# 我本可以只返回平均值，但是返回一个元组可以获得累积数据的另一个重要信息——项数
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager2():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield # 不产出只接受值
        if term is None:
            break  # <1>
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # <2>


coro_avg = averager2()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
coro_avg.send(None)
# StopIteration: Result(count=3, average=15.5) #为什么会出现异常？
# 发送 None 会终止循环，导致协程结束，返回结果。一如既往，生成器对象会抛出 StopIteration 异常。
# 异常对象的 value 属性保存着返回的值。

#%% 如何获取协程返回的值：只能在异常中获取这个结果吗？
coro_avg = averager2()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value
print(result)

# Result(count=3, average=15.5)


# %% yield from 结构会在内部自动捕获 StopIteration 异常。
# 对 yield from 结构来说，解释器不仅会捕获 StopIteration 异常，
# 还会把 value 属性 的值变成 yield from 表达式的值。
# 可惜，我们无法在控制台中使用交互的方式测试这种行为，
# 因为在函数外部使用 yield from（以及 yield）会导致句法出错。

# 类似的结构使用 await 关键字，这个 名称好多了，因为它传达了至关重要的一点：
# 在生成器 gen 中使用 yield from subgen() 时，subgen 会获得控制权，把产出的值传给 gen 的调用方，
# 即调用方可以直接控制subgen。与此同时，gen 会阻塞，等待 subgen 终止

def gen():
    for c in 'AB':
        yield c
    for i in range(1,3):
        yield i

list(gen())
# ['A', 'B', 1, 2]

def gen2():
    yield from 'AB'
    yield from range(1,3)

list(gen2())
# ['A', 'B', 1, 2]

#%%  
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s='ABC'
t = tuple(range(3))
list(chain(s,t))
# ['A', 'B', 'C', 0, 1, 2]



def chain(*iterables):
    for i in iterables:
        yield from i
list(chain(s,t))
# ['A', 'B', 'C', 0, 1, 2]

# yield from i 完全代替了内层的 for 循环。
# 在这个示例中使用 yield from 是对的，而且代码读起来更顺畅，不过感觉更像是语法糖。
# 除了代替循环之外，yield from还会创建通道，把内层生成器直接与外层生成器的客户端联系起来。
# 把生成器当成协程使用时，这个通道特别重要，不仅能为客户端代码生成值，还能使用客户端代码提供的值。

#%% yield from 结果
# 调用方/委派生成器（包含yield from的生成器函数）/子生成器
from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # <1>
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2>
        if term is None:  # <3>
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # <4>


# the delegating generator
def grouper(results, key):  # <5>
    while True:  # <6>
        results[key] = yield from averager()  # <7>
        # 内层 for 循环调用 group.send(value)，直接把值传给子生成器 averager。同时，当前 的 grouper 实例（group）在 yield from 表达式处暂停。


# the client code, a.k.a. the caller
def main(data):  # <8>
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # <9>
        next(group)  # <10>
        for value in values:
            group.send(value)  # <11>
        group.send(None)  # important! <12> 如果子生成器不终止，委派生成器会在 yield from 表达式处永远暂停。

    # print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
              result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}
main(data)


# 子生成器产出的值都直接传给委派生成器的调用方（即客户端代码）。 
# 使用 send() 方法发给委派生成器的值都直接传给子生成器。
# 如果发送的值是 None，那 么会调用子生成器的 __next__() 方法。
# 如果发送的值不是 None，那么会调用子生成器 的 send() 方法。如果调用的方法抛出 StopIteration 异常，那么委派生成器恢复运行。 
# 任何其他异常都会向上冒泡，传给委派生成器。
# 生成器退出时，生成器（或子生成器）中的return expr 表达式会触发 StopIteration(expr) 异常抛出。
# yield from 表达式的值是子生成器终止时传给 StopIteration 异常的第一个参数。

# 传入委派生成器的异常，除了 GeneratorExit 之外都传给子生成器的 throw() 方法。
# 如 果调用 throw() 方法时抛出 StopIteration 异常，委派生成器恢复运行。StopIteration 之外的异常会向上冒泡，传给委派生成器。
# 如果把 GeneratorExit 异常传入委派生成器，或者在委派生成器上调用 close() 方法， 那么在子生成器上调用 close() 方法，如果它有的话。
# 如果调用 close() 方法导致异常 抛出，那么异常会向上冒泡，传给委派生成器；否则，委派生成器抛出 GeneratorExit异常。
