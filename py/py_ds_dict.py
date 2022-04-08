#%% defaultdict：处理找不到的键的一个选择
# 在用户创 建 defaultdict 对象的时候，就需要给它配置一个为找不到的键创造默认值的方法。
# 具体而言，在实例化一个 defaultdict 的时候，需要给构造方法提供一个可调用对象，
# 这个可调用对象会在 __getitem__ 碰到找不到的键的时候被调用，让 __getitem__ 返回某种默认值。

# 比如，我们新建了这样一个字典：dd = defaultdict(list)，
# 如果键 'new-key' 在 dd 中还 不存在的话，表达式 dd['new-key'] 会按照以下的步骤来行事。 
# (1) 调用 list() 来建立一个新列表。 
# (2) 把这个新列表作为值，'new-key' 作为它的键，放到 dd 中。
# (3) 返回这个列表的引用。
# 而这个用来生成默认值的可调用对象存放在名为 default_factory 的实例属性里。

from collections import defaultdict
d1 = defaultdict()
# d1["i1"]s
# KeyError: 'i1'

d2 = defaultdict(list)
d2['i1']
# []
d2["i2"].append('a')
# defaultdict(list, {'i1': [], 'i2': ['a']})
d2["i3"].append(1)
d2["i3"].append(2)
d2["i3"].append(3)
# defaultdict(list, {'i1': []
#                  , 'i2': ['a']
#                  , 'i3': [1, 2, 3]})

# key的存在性判断
"i2" in d2
# True
"i4" in d2
# False

# 字典中list的增加和删除
d2["i3"].append(4)
d2["i3"].remove(1)
# defaultdict(list, {'i1': []
#                  , 'i2': ['a']
#                  , 'i3': [2, 3, 4]})

