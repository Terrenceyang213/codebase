#%% tags:sklearn;linear;线性模型;
from sklearn import linear_model

#%% tags:sklearn;LinearRegression;
######################################################################
# fit and predict
from sklearn import linear_model
import numpy as np
X_train = np.array([ [0,0],
            [1,1],
            [2,2]])
Y_train = np.array([0,1,2])

X_test = np.array([  [5,5],
            [7,7],
            [1,7]])
Y_test = np.array([5,7,4])


reg = linear_model.LinearRegression()
reg.fit(X_train, # <1> X 行向量，每个样本为行元素，这样做能够与tensorflow保持一致
        Y_train,  # <2> 
        )        # <3> fit

print(reg.coef_)
# [0.5 0.5]

print(reg.intercept_)
# 2.220446049250313e-16

print(reg.predict([[5,5],[7,7],[1,7]])) # <4> reg.predict
# [5. 7. 4.]

######################################################################
#  精度评估
from sklearn.metrics import mean_squared_error, r2_score # <5> MSE,R2
pre_train = reg.predict(X_train)
pre_test = reg.predict(X_test)
print(f"MSE train:{mean_squared_error(pre_train, Y_train):.4f}") # MSE_tr
print(f"R2 train:{r2_score(pre_train, Y_train)}") # MSE_tr
# MSE train:0.0000
# R2 train:1.0

print(f"MSE test:{mean_squared_error(pre_test, Y_test):.4f}") # MSE_tr
print(f"R2 test:{r2_score(pre_test, Y_test)}") # MSE_tr
# MSE test:0.0000
# R2 test:1.0

######################################################################
# 画图
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw=dict(projection='3d')) # <> 3d plot

# 真实值
ax.scatter(X_test[:,0], X_test[:,1], Y_test, marker='o',c='r')
ax.set(xlabel='x', ylabel='y', zlabel='z')

# 预测曲面
X = np.arange(0, 10, 1)
Y = np.arange(0, 10, 1)
axX, axY = np.meshgrid(X, Y)
X, Y = [x.reshape(x.shape[0]*x.shape[1],1) for x in np.meshgrid(X, Y)]

Z = reg.predict(np.hstack([X,Y]))
Z = Z.reshape(axX.shape)

print(Z)
ax.plot_wireframe(axX, axY, Z)
plt.show()

# %% tags:sklearn;Ridge;岭回归;
###############################################################################
from sklearn import linear_model
import numpy as np
X = np.random.randint(0,10,size=(100,2))
Y = 0.5*X[:,0] + 0.7*X[:,1] + np.random.rand(100) * 2 + 7
print(X.shape,Y.shape)
# (100, 2) (100,)

X_train = X[:80,:]
X_test = X[80:100,:]
Y_train = Y[:80]
Y_test = Y[80:100]

reg = linear_model.Ridge(alpha=.5)
reg.fit(X_train,Y_train)
print(f'reg.coef_:{reg.coef_:},reg.intercept_:{reg.intercept_:.4f}')
# reg.coef_:[0.50997646 0.69248863],reg.intercept_:0.5225

###############################################################################
from sklearn.metrics import mean_squared_error,r2_score 
pre_train = reg.predict(X_train)
pre_test = reg.predict(X_test)

print(f"MSE train:{mean_squared_error(pre_train, Y_train):.4f}") # MSE_tr
print(f"R2 train:{r2_score(pre_train, Y_train)}") # MSE_tr
# MSE train:0.0879
# R2 train:0.9832581438949357

print(f"MSE test:{mean_squared_error(pre_test, Y_test):.4f}") # MSE_tr
print(f"R2 test:{r2_score(pre_test, Y_test)}") # MSE_tr
# MSE test:0.0701
# R2 test:0.9865420076323983

###############################################################################
# 画图
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw=dict(projection='3d')) # <> 3d plot

# 真实值

ax.scatter(X_test[:,0], X_test[:,1], Y_test, marker='o',c='r')
ax.set(xlabel='x', ylabel='y', zlabel='z')

# 预测曲面
X = np.arange(0, 10, 1)
Y = np.arange(0, 10, 1)
axX, axY = np.meshgrid(X, Y)
X, Y = [x.reshape(x.shape[0]*x.shape[1],1) for x in np.meshgrid(X, Y)]

Z = reg.predict(np.hstack([X,Y]))
Z = Z.reshape(axX.shape)

print(Z)
ax.plot_wireframe(axX, axY, Z)
plt.show()



