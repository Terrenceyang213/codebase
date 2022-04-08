#%% 只要 Python 函数的定义体中有 yield 关键字，该函数就是生成器函数。
# 调用生成器函数 时，会返回一个生成器对象。也就是说，生成器函数是生成器工厂。

def gen_123():
    yield 1
    yield 2
    yield 3
    yield 'a'

# 生成器函数会创建一个生成器对象，包装生成器函数的定义体。把生成器传给 next(...) 函数时，
# 生成器函数会向前，执行函数定义体中的下一个 yield 语句，返回产出的值，
# 并在函数定义体的当前位置暂停。最终，函数的定义体返回时，外层的生成器对象会抛出
# StopIteration 异常——这一点与迭代器协议一致。

# 函数返回值；调用生成器函数返回生成器；生成器产出或生成值。 
# 生成器不会以常规的方式“返回”值：生成器函数定义体中的 return 语句会
# 触发生成器对象抛出 StopIteration 异常。
for i in gen_123():
    print(i)
# 1
# 2
# 3
# a

g = gen_123()
print(next(g))
# 1

gen_123
# <function __main__.gen_123()>

gen_123()
# <generator object gen_123 at 0x000001AC07ED4C48>
#%% 生成器执行过程

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

for i,j in enumerate(gen_AB()):
    print(i,j)
# start
# 0 A
# continue
# 1 B
# end 

g = gen_AB()
next(g)
# start
# 'A'
next(g)
# continue
# 'B'
next(g)
# end
# StopIteration

#%% yield 会暂停当前的函数执行过程
# 所以返回函数句柄，在next被调用后再关闭是可行的。
def gen():
    a = [1,2,3]
    print("initialising")
    for ix in a:
        print(f'before yield {ix}')
        yield ix
        print(f'after yield {ix}')
    print("Finished")

g = gen()
next(g)
# initialising
# before yield 1

next(g)
# after yield 1
# before yield 2

next(g)
# after yield 2
# before yield 3

next(g)
# after yield 3
# Finished
# StopIteration


# %% 生成器表达式
# 生成器表达式会产出生成器，因此可以使用生成器表达式进一步减少 Sentence 类的代码

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

#列表推导迫切地迭代 gen_AB() 函数生成的生成器对象产出的元素：'A' 和 'B'。
# 注意， 下面的输出是 start、continue 和 end.
res1 = [x*3 for x in gen_AB()]
# start
# continue
# end

for i in res1:
    print('--->',i)
# ---> AAA
# ---> BBB

# 把生成器表达式返回的值赋值给 res2。res2是一个生成器对象
# 只需调用 gen_AB() 函数，虽然调用时会返回一 个生成器，但是这里并不使用。
res2 = (x*3 for x in gen_AB())
res2
# <generator object <genexpr> at 0x000001AC08047C48>

# 只有 for 循环迭代 res2 时，gen_AB 函数的定义体才会真正执行。
# for 循环每次迭代时 会隐式调用 next(res2)，
# 前进到 gen_AB 函数中的下一个 yield 语句。
# 注意，gen_AB 函数的输出与 for 循环中 print 函数的输出夹杂在一起。
for i in res2:
    print('--->',i)
# start
# ---> AAA
# continue
# ---> BBB
# end


# %%
