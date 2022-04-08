#%% 常用生成器函数

# itertools.compress(it, selector_it) 
# 并行处理两个可迭代的对象；如果 selector_it 中的元素是 真值，产出 it 中对应的元素

# itertools.dropwhile(predicate, it)
# 处理 it，跳过 predicate 的计算结果为真值的元素，然后 产出剩下的各个元素（不再进一步检查）

# filter(predicate, it)
# 把 it 中的各个元素传给 predicate，如果 predicate(item) 返回真值，那么产出对应的元素；
# 如果 predicate 是 None，那么只产出真值元素

# itertools.filterfalse(predicate, it)
# 与 filter 函数的作用类似，不过 predicate 的逻辑是相反的：predicate 返回假值时产出对应的元素

# itertools.islice(it, stop) 或 islice(it, start, stop, step=1)
# 产出 it 的切片，作用类似于 s[:stop] 或 s[start:stop:step]， 
# 不过 it 可以是任何可迭代的对象，而且这个函数实现的是惰性操作

# itertools.takewhile(predicate, it)
# predicate 返回真值时产出对应的元素，然后立即停止，不 再继续检查


def vowel(c): 
    return c.lower() in 'aeiou' 
list(filter(vowel, 'Aardvark')) 
# ['A', 'a', 'a'] 

import itertools
list(itertools.filterfalse(vowel, 'Aardvark')) 
# ['r', 'd', 'v', 'r', 'k']

list(itertools.dropwhile(vowel, 'Aardvark')) 
# ['r', 'd', 'v', 'a', 'r', 'k']

list(itertools.takewhile(vowel, 'Aardvark')) 
# ['A', 'a']

list(itertools.compress('Aardvark', (1,0,1,1,0,1))) 
# ['A', 'r', 'd', 'a']

list(itertools.islice('Aardvark', 4)) 
# ['A', 'a', 'r', 'd']

list(itertools.islice('Aardvark', 4, 7)) 
# ['v', 'a', 'r']

list(itertools.islice('Aardvark', 1, 7, 2))
# ['a', 'd', 'a']


#%%