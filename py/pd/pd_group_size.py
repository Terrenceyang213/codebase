# tags: group,size,count,groupby

#%% question: 计算一个分组中，不同类别的数量

import pandas as pd
d = {
    "one": pd.Series([1.0, 2.0, 3.0, 4.0], 
        index=["a", "b", "c","d"]),
    "two": pd.Series([1, 2, 1, 1], index=["a", "b", "c", "d"]),
    }
df = pd.DataFrame(d)
#   one	two
# a	1.0	1
# b	2.0	2
# c	3.0	1
# d	4.0	2

#%% 

df.groupby('two').size()
# two
# 1    3
# 2    1
# dtype: int64

# %%
