# tags:numpy options,np options

#%% tags:numpy option: precision,digits,精度, 小数位数
import numpy as np
np.set_printoptions(precision=3,suppress=True) # 取消科学计数法
print(np.array([1.23456]))

#%% tags:numpy option;np option;展示数据列数
np.set_printoptions(threshold=float("inf")) # <> 展示所有数据

#%% tags:numpy option;np option;每行容纳数据的宽度
np.set_printoptions(linewidth=150) # <> 默认75

