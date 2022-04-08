#%%
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# ax.plot 参数：
# linewidth: 线宽
# linestyle：'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# color: 'red','blue','green','#f1f1f1'

# markers ： ['+', 'o', '*', 's', '.', '1', '2', '3', '4']
# markersize: 标记点大小
# markeredgewidth：标记点边缘大小




# %% Line type and point properties
###############################################################################
x = np.linspace(-5,5,5)
y = np.ones_like(x)

def axes_settings(fig, ax, title, ymax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0,ymax+1)
    ax.set_title(title)


fig,axes = plt.subplots(1,4,figsize=(16,3))


# %% Line width
fig,ax = plt.subplots(1,1,figsize=(4,3))
linewidths = [0.5, 1, 2, 4,10]
for n, linewidth in enumerate(linewidths):
    ax.plot(x, y+n, color = 'blue', linewidth=linewidth)
axes_settings(fig, ax, "linewidth", len(linewidths))


# %% Line style/set_dashes
# line style:'-', '--', '-.', ':', 'None', ' ', '', 
#            'solid', 'dashed', 'dashdot', 'dotted'
fig,ax = plt.subplots(1,1,figsize=(4,4))
linestyles = ['-','-.',':','--']
for n,linestyle in enumerate(linestyles):
    ax.plot(x, y+n, color="blue", lw=2, linestyle = linestyle)

    
#custom dash style
# 改变最上面间隔横线的横线长度与间隔长度
line, = ax.plot(x, len(linestyles)+y, color="blue", lw=5)
length1, gap1, length2, gap2 = 10, 7, 20, 1 
# 四个长度为一组dash，长度10的横线，长度7的间隔，长度20的横线，长度为1的间隔
line.set_dashes([length1, gap1, length2, gap2])
axes_settings(fig, ax, "linetypes", len(linestyles)+1)


# %%marker types
fig,ax = plt.subplots(1,1,figsize=(10,10))
markers = ['+', 'o', '*', 's', '.', '1', '2', '3', '4']
for n,marker in enumerate(markers):
    #lw = shorthand for linewidth, ls = shorthand for linestyle
    ax.plot(x, y+n, color="blue", lw=2, ls=" ", marker=marker)
axes_settings(fig, ax, "markers", len(markers))
ax.set_yticks(np.arange(len(markers)+1))

# marker size and color
# %%
markersizecolors = [(4,"white"), (8,"red"), (12,"yellow"), (16,"lightgreen")]
for n,(markersize, markerfacecolor) in enumerate(markersizecolors):
    ax.plot(x, y+n, color="black", lw=1, ls='-',
                marker='s', markersize=markersize,
                markerfacecolor=markerfacecolor,
                markeredgewidth=1)
axes_settings(fig, ax, "marker size/color", len(markersizecolors))

# %%
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################