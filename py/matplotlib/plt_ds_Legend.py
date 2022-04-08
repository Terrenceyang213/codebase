


#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl




#%% label参数与legend()
# legend(loc=1,2,3,4) 标签位置
# loc = 1 以legend标签的右上角为基准点，与ax的右上角对齐。
# loc = 2 以legend标签的左上角为基准点，与ax的左上角对齐。
# loc = 3 以legend标签的左下角为基准点，与ax的左下角对齐。
# loc = 4 以legend标签的右下角为基准点，与ax的右下角对齐。



fig, axes = plt.subplots(1, 4, figsize=(16, 4))

x = np.linspace(0, 1, 100)

for n in range(4):
    axes[n].plot(x, x, label="y(x) = x")
    axes[n].plot(x, x + x**2, label="y(x) = x + x**2")
    ################
    axes[n].legend(loc=n+1)
    ################
    axes[n].set_title("legend(loc={:d})".format(n+1))

# 1,2,3,4 会影响legend依据哪个标签点作为参考点。loc=1，则右上角。
# 在下个例子中，loc的取值会影响使用哪个点作为bbox_to_anchor的点
    
fig.tight_layout()

# %% legend形态控制
# ncol
# nrow
# bbox_to_anchor :(1,1)
fig, ax = plt.subplots(1, 1, figsize=(8.5, 3),facecolor='#ffffff')

x = np.linspace(-1, 1, 100)

for n in range(1, 9):
    ax.plot(x, n * x, label="y(x) = {:d}*x".format(n) )

ax.legend(ncol=2, loc=2,bbox_to_anchor=(1, 1), fontsize=12) #ncol标签分4列
# ncol legend标签分为两列
# loc = 2 ，legend标签以左上角为对准点。
# bbox_to_anchor=(1,1) , 对准点对准（1，1）

fig.subplots_adjust(top=0.8); #修改高度


# %%