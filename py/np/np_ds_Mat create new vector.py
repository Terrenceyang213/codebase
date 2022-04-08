import numpy as np

#%%
# 构造行向量与列向量的方法 reshape
L = np.array([[1,2,3,4,5]])
# array([[1, 2, 3]])

alpha_b = np.linspace(1, 20, 20).reshape(20,1) 
# array([[ 1. ],
#        [ 4.5],
#        [ 8. ],
#        [11.5],
#        [15. ]])

np.matmul(alpha_b,L)
# array([[ 1. ,  2. ,  3. ],
#        [ 4.5,  9. , 13.5],
#        [ 8. , 16. , 24. ],
#        [11.5, 23. , 34.5],
#        [15. , 30. , 45. ]])


# %%
