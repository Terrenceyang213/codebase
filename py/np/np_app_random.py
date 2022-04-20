# %% tags:numpy;np;random;随机数
import numpy as np
# random
# random.randint(100)   # 100以内的整数,默认标量，size向量
# random.rand()         # 生成0 到 1 之间的随机浮点数向量
# random.choice()       # 基于给定值生成随机数
# multivariate_normal   # 多元变量向量
#%% tags:numpy;np;random;randint(); 随机整数标量
np.random.randint(100,size=None)
# 16

np.random.randint(1,10,size=None) 
# Out[4]: 8

np.random.randint(1,10,size=(1,5)) 
# array([[9, 9, 4, 9, 8]])

#%% tags:numpy;np;random;rand(); 
np.random.rand()
# Out[12]: 0.3551799900015947

np.random.rand(5)
# array([0.23456081, 0.14399367, 0.70503724, 0.04764928, 0.04896364])

#%% tags:numpy;np;random;choice(); 

np.random.choice([1,2,3,4])
# 4

np.random.choice([1,2,3,4])
# 2

#%% tags:numpy;np;random;multivariate; 多元随机变量
a = np.random.multivariate_normal(
    mean=[0, 3],
    cov=[[1, 0.5],[0.5, 1]],
    size=1000)
# array([[-1.28104074,  3.00228909],
#        [-1.26942349,  2.92222427],
#        [ 0.92625369,  2.52124627],
#        [-0.57462629,  1.62449771],
#        [ 0.28688037,  2.8146925 ],
#        [ 0.3254171 ,  2.70331164],
#        [-0.7366178 ,  2.65254063],
#        [-2.0075996 ,  1.2108896 ],
#        [ 1.84618775,  3.02288973],
#        [-1.30926256,  2.13507995]])

a1 = a[:,0]
np.mean(a1),np.std(a1)
# (0.05160844800204821, 0.8574626638452654)

a2 = a[:,1]
np.mean(a2),np.std(a2)
# (2.8940988980071705, 1.0402762797098768)

np.cov(a1,a2)
# array([[0.91922547, 0.44458961],
#        [0.44458961, 0.92262048]])


