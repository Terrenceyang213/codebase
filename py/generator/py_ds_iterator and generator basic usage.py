"""
Sentence: access words by index
"""

#%% 可迭代对象生成迭代器
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence1:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # <1>

    def __getitem__(self, index):
        return self.words[index]  # <2>

    def __len__(self):  # <3>
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # <4>

s = Sentence1('I will be back')
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#%% 可迭代对象直接实现迭代器协议
# 为什么要单独创建一个迭代类，而不是在sentence类中实现迭代：
# 为了“支持多种遍历”，必须能从同一个可迭代的实例中获取多个独立的迭代器，而且各 个迭代器要能维护自身的内部状态，因此这一模式正确的实现方式是，
# 每次调用 iter(my_iterable) 都新建一个独立的迭代器。这就是为什么这个示例需要定义 SentenceIterator 类。
# BEGIN SENTENCE_ITER
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence2:
    # 去掉了__getitem__,则迭代不要由__iter__提供
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # <1>
        return SentenceIterator2(self.words)  # <2>


class SentenceIterator2:

    def __init__(self, words):
        self.words = words  # <3>
        self.index = 0  # <4>

    def __next__(self):
        try:
            word = self.words[self.index]  # <5>
        except IndexError:
            raise StopIteration()  # <6>
        self.index += 1  # <7>
        return word  # <8>

    def __iter__(self):  # <9>
        return self
# END SENTENCE_ITER

s = Sentence2('I will be back')
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#%% 用生成器函数替代迭代类：sentence3

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence3:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        #生成器函数
        for word in self.words:  # <1>
            yield word  # <2>
        return  # <3>

s = Sentence3('I will be back')
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# %% 生成器的惰性实现版本：findall->finditer
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence4:
    #惰性实现版本，不在对象初始化时构建单词列表
    def __init__(self, text):
        self.text = text  # <1>

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):  # <2>
            yield match.group()  # <3>

s = Sentence4('I will be back')
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#%% 生成器表达式实现(x for x in gen_AB())
# BEGIN SENTENCE_GENEXP
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence5:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # 与上例唯一的区别是 __iter__ 方法，这里不是生成器函数了（没有 yield），
        # 而是使 用生成器表达式构建生成器，然后将其返回。
        # 不过，最终的效果一样：调用 __iter__ 方法会得到一个生成器对象
        return (match.group() for match in RE_WORD.finditer(self.text))

s = Sentence5('I will be back')
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# %% 等差数列生成器
class ArithmeticProgression0:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        while forever or result < self.end:
            yield result
            result += self.step

class ArithmeticProgression1:

    def __init__(self, begin, step, end=None):  # <1>
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)  # <2>
        forever = self.end is None  # <3>
        index = 0
        while forever or result < self.end:  # <4>
            yield result  # <5>
            index += 1
            result = self.begin + self.step * index  # <6>




ap = ArithmeticProgression1(0, 1, 3)
list(ap)
# [0, 1, 2]

ap = ArithmeticProgression1(1, .5, 3) 
list(ap)
# [1.0, 1.5, 2.0, 2.5]

ap = ArithmeticProgression1(0, 1/3, 1) 
list(ap)
# [0.0, 0.3333333333333333, 0.6666666666666666] 

from fractions import Fraction
ap = ArithmeticProgression1(0, Fraction(1, 3), 1) 
list(ap)
# [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)] 

from decimal import Decimal
ap = ArithmeticProgression1(0, Decimal('.1'), .3)
list(ap)
# [Decimal('0'), Decimal('0.1'), Decimal('0.2')]

#%% 等差数列生成器函数
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

aritprog_gen(0,1,10)
# <generator object aritprog_gen at 0x000001A4DC904E48>

list(aritprog_gen(0,1,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% 使用itertools模块生成等差数列
import itertools

# itertools.count 函数返回的生成器能生成多个数。
# 如果不传入参数，itertools. count 函数会生成从零开始的整数数列。
g = itertools.count(1, .5)
print(next(g),
    next(g),
    next(g),)
# 1 1.5 2.0
# list(g) 会生成无限大的list直到占满内存

# itertools.takewhile 函数则不同，
# 它会生成一个使用另一个生成器的生成器，在指定的条件计算结果为 False 时停止
gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
list(gen)
# [1, 1.5, 2.0, 2.5]


# 以itertools改造上面的等差数列生成函数
def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
#  aritprog_gen 不是生成器函数，因为定义体中没有 yield 关键字。
#  但是它会返回一个生成器，因此它与其他生成器函数一样，也是生成器工厂函数。


#%% iter函数再探
# iter 函数还有一个鲜为人知的用法：
# 传入两个参数，使用常规的函数或任何可调用的对象创建迭代器。
# 这样使用时，第一个参数必须是可调用的对象，用于不断调用（没有参数），产出各个值；
# 第二个值是哨符，这是个标记值，当可调用的对象返回这个值时，触发迭代器抛出 StopIteration 异常，而不产出哨符。
from random import randint
def d6():
    return randint(1,6)

d6_iter = iter(d6,1)
d6_iter
# <callable_iterator at 0x28a2b362288>

for roll in d6_iter:
    print(roll)
# 6
# 4
# 4
# 2
# 2
# 5

#%% 