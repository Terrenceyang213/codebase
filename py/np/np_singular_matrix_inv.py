#%%
import numpy as np
from numpy.linalg import matrix_rank as rank
from numpy.linalg import inv
A = np.loadtxt('./A.csv',delimiter=',')
A.shape
B = A[1:,1:].copy()
B.shape

np.linalg.inv(A.T@A)
matB = B.T@B
# rank 10
invmatB = np.linalg.pinv(matB)
# rank 10



#%%#######################################################
# 不要用不满秩的矩阵求逆,对于同一个矩阵,其朝向方向也会造成结果不一致
q_left_up = np.array([
    [3,2,1],
    [2,2,0],
    [1,0,1]
])
inv(q_left_up)
# array([[ 4.50359963e+15, -4.50359963e+15, -4.50359963e+15],
#        [-4.50359963e+15,  4.50359963e+15,  4.50359963e+15],
#        [-4.50359963e+15,  4.50359963e+15,  4.50359963e+15]])

q_left_down = np.array([
    [1,0,1],
    [2,2,0],
    [3,2,1]
])
inv(q_left_down)
# array([[-4.50359963e+15, -4.50359963e+15,  4.50359963e+15],
#        [ 4.50359963e+15,  4.50359963e+15, -4.50359963e+15],
#        [ 4.50359963e+15,  4.50359963e+15, -4.50359963e+15]])

q_right_up = np.array([
    [1,2,3],
    [0,2,2],
    [1,0,1]
])

inv(q_right_up)
# LinAlgError: Singular matrix

q_right_down = np.array([
    [1,0,1],
    [0,2,2],
    [1,2,3]
])

inv(q_right_down)
# LinAlgError: Singular matrix