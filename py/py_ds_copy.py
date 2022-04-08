#%% copy操作在python中极具迷惑性
from copy import deepcopy

#%% 包含数字的字典dict
d1_int = {"ind1":1,"ind2":2}

# 复制操作有三种
d2_int = d1_int #这个只相当于别名
d3_int = dict(d1_int) #浅拷贝
d4_int = d1_int.copy() #浅拷贝
d5_int = deepcopy(d1_int)

print('字典的id')
print(id(d1_int))
print(id(d2_int)) #别名
# 2609613780616
# 2609613780616

print(id(d3_int)) #shallow
print(id(d4_int)) #shallow
print(id(d5_int)) #deep
# 2609613780456
# 2609613780136
# 2609613881080

print('键值的id')
print(id(d1_int["ind1"]))
print(id(d2_int["ind1"])) #别名
print(id(d3_int["ind1"])) #shallow
print(id(d4_int["ind1"])) #shallow
print(id(d5_int["ind1"])) #deep
# 140726499049744
# 140726499049744
# 140726499049744
# 140726499049744
# 140726499049744
# 即使使用深度拷贝，数字也不会被拷贝第二份。

#%% 包含其他object的dict
# 除了深拷贝，其他拷贝均是统一对象

d1_obj = {"ind":[1,2,3]}

d2_obj = d1_obj #这个只相当于别名
d3_obj = dict(d1_obj) #浅拷贝
d4_obj = d1_obj.copy() #浅拷贝
d5_obj = deepcopy(d1_obj)

print('字典的id')
print(id(d1_obj))
print(id(d2_obj)) #别名
# 2609614930872
# 2609614930872

print(id(d3_obj)) #shallow
print(id(d4_obj)) #shallow
print(id(d5_obj)) #deep
# 2609614930952
# 2609614931032
# 2609614140104

print('键值的id')
print(id(d1_obj["ind"]))
print(id(d2_obj["ind"])) #别名
print(id(d3_obj["ind"])) #shallow
print(id(d4_obj["ind"])) #shallow
print(id(d5_obj["ind"])) #deep
# 2609614360136
# 2609614360136
# 2609614360136
# 2609614360136
# 2609614886152