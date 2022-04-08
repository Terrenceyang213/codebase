#%%

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def hide_labels(fig, ax):
    global fignum
    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.axis('tight')
    
x = np.linspace(-3, 3, 25)
y1 = x**3+ 3 * x**2 + 10
y2 = -1.5 * x**3 + 10*x**2 - 15

#%% 线图/plot line
###############################################################################
fig, ax = plt.subplots(figsize=(4, 3))

ax.plot(x, y1,ls='--')
ax.plot(x, y2,marker='o')

hide_labels(fig, ax)



#%% 阶梯图/ax.step
fig, ax = plt.subplots(figsize=(4, 3))

ax.step(x, y1,marker='o')
ax.step(x, y2,)

hide_labels(fig, ax)
#%% 柱状图/bar
###############################################################################
fig, ax = plt.subplots(figsize=(4, 3))
width = 6/50.0
ax.bar(x -width/2, y1, width=width, color="blue")
ax.bar(x + width/2, y2, width=width, color="green")

hide_labels(fig, ax)

#%% 填充图/ax.fill
###############################################################################
fig, ax = plt.subplots(figsize=(4, 3))
ax.plot(x, y1)
ax.plot(x, y2)
ax.fill_between(x, y1, y2)

hide_labels(fig, ax)
#%% 统计直方图
###############################################################################
fig, ax = plt.subplots(figsize=(4, 3))
ax.hist(y2, bins=30)
ax.hist(y1, bins=30)

hide_labels(fig, ax)

#%% 误差图/errorbar
###############################################################################
fig, ax = plt.subplots(figsize=(4, 3))

ax.errorbar(x, y2, yerr=y1, fmt='o-')
ax.plot(x, y2+y1,color='red')
ax.plot(x, y2-y1,color='green')
hide_labels(fig, ax)

#%% ax.stem
###############################################################################

fig, ax = plt.subplots(figsize=(4, 3))

ax.stem(x, y2, 'b', markerfmt='bs')
ax.stem(x, y1, 'r', markerfmt='ro')

hide_labels(fig, ax)
#%% 散点图/scatter
###############################################################################
fig, ax = plt.subplots(figsize=(4, 3))

x = np.linspace(0, 5, 50)

ax.scatter(x, -1 + x + 0.25 * x**2 + 2 * np.random.rand(len(x)))
ax.scatter(x, np.sqrt(x) + 2 * np.random.rand(len(x)), color="green")

hide_labels(fig, ax)

#%% 向量场/quiver
###############################################################################
fig, ax = plt.subplots(figsize=(3, 3))

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

x = y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)
U = np.sin(X)
V = np.sin(Y)

ax.quiver(X, Y, U, V)

hide_labels(fig, ax)
#%%
###############################################################################
#%%
###############################################################################
#%%
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################