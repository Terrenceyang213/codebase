#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# %% 坐标轴标签 Axis label
# ax.set_xlabel/ax.set_ylabel/ax.set_title
fig, ax = plt.subplots(figsize=(8, 3), subplot_kw={'facecolor': "#ebf5ff"})

x = np.linspace(0, 50, 500)

ax.plot(x, np.sin(x) * np.exp(-x/10), lw=2, marker=' ',color='red')

ax.set_xlabel("x", labelpad=5, fontsize=18, fontname='serif', color="blue")

ax.set_ylabel("f(x)", labelpad=15, fontsize=18, fontname='serif', color="blue")

ax.set_title("axis labels and title example", loc='right', fontsize=16, 
                fontname='serif', color="blue")

fig.tight_layout()


# %% 坐标轴范围/Axis range：ax.set_xlim/ax.set_ylim/ax.axis('tight')/ax.axis('equal')
x = np.linspace(0, 30, 500)
y = np.sin(x) * np.exp(-x/10)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), subplot_kw={'facecolor': "#ebf5ff"})

axes[0].plot(x, y, lw=2)
axes[0].set_xlim(-5, 35)
axes[0].set_ylim(-1, 1)
axes[0].set_title("set_xlim / set_ylim")

axes[1].plot(x, y, lw=2)
axes[1].axis('tight') #Set limits just large enough to show all data, then disable further autoscaling.
axes[1].set_title("axis('tight')")

axes[2].plot(x, y, lw=2)
axes[2].axis('equal') # x, y 轴长度相等
axes[2].set_title("axis('equal')")

#%% 坐标轴的数轴/Ticks：ax.set_xticks()/ax.set_yticks()/ax.xaxis.set_major_locator()/ax.xaxis.set_minor_locator()
#ax.xaxis.set_major_locator(ticker)
# mpl.ticker的种类：
#   MaxNlocator(nbins): Find nice tick locations with no more than N being within the view limits. 
#   FixedLocator(locs): 固定
#   MultipleLocator(base) : Set a tick on each integer multiple of a base within the view interval.

x = np.linspace(-3 * np.pi, 3 * np.pi, 500)
y = np.sin(x) * np.exp(x**2/40)

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

axes[0].plot(x, y, lw=2)
axes[0].set_title("default ticks")

axes[1].plot(x, y, lw=2)
axes[1].set_yticks([-1, 0, 1])
axes[1].set_xticks([-5, 0, 5])
axes[1].set_title("set_xticks")

axes[2].plot(x, y, lw=2)
axes[2].xaxis.set_major_locator(mpl.ticker.MaxNLocator(nbins = 7))
axes[2].yaxis.set_major_locator(mpl.ticker.FixedLocator([-1, 0, 1]))
axes[2].xaxis.set_minor_locator(mpl.ticker.MaxNLocator(5))
axes[2].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(8))
axes[2].set_title("set_major_locator")

axes[3].plot(x, y, lw=2)
axes[3].yaxis.set_major_locator(mpl.ticker.MultipleLocator(3))#set_yticks([-1, 0, 1])
axes[3].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
axes[3].set_xticklabels(['$-2\pi$', '$-1\pi$', r'$0$', r'$1\pi$', r'$2\pi$'])
axes[3].xaxis.set_minor_locator(mpl.ticker.FixedLocator([-3 * np.pi / 2, -np.pi/2, 0, np.pi/2, 3 * np.pi/2]))
axes[3].yaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
axes[3].set_title("set_xticklabels")

fig.tight_layout()


# %% 坐标轴网格/Grid：ax.grid()
# color
# which:both/major/minor
# axis:x/y
# linestyle:'-',':'...
# linewidth
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

x_major_ticker = mpl.ticker.MultipleLocator(10)
x_minor_ticker = mpl.ticker.MultipleLocator(3)
y_major_ticker = mpl.ticker.MultipleLocator(1)
y_minor_ticker = mpl.ticker.MultipleLocator(0.5)

for ax in axes:
    ax.plot(x, y, lw=2)
    ax.xaxis.set_major_locator(x_major_ticker)
    ax.yaxis.set_major_locator(y_major_ticker)
    ax.xaxis.set_minor_locator(x_minor_ticker)
    ax.yaxis.set_minor_locator(y_minor_ticker)

axes[0].set_title("default grid")
axes[0].grid()

axes[1].set_title("major/minor grid")
axes[1].grid(color="red", which="both", linestyle=':', linewidth=0.5)

axes[2].set_title("individual x/y major/minor grid")
axes[2].grid(color="grey", which="major", axis='x', linestyle='-', linewidth=5)
axes[2].grid(color="grey", which="minor", axis='x', linestyle=':', linewidth=0.25)
axes[2].grid(color="grey", which="major", axis='y', linestyle='-', linewidth=0.5)

fig.tight_layout()


# %% Tick Fomatter : mpl.ticker.ScalarFormatter(useMathText=True)
fig, axes = plt.subplots(1, 2, figsize=(8, 3))

x = np.linspace(0, 1e5, 100) #1e5 = 100000
y = x ** 2

axes[0].plot(x, y, 'b.')
axes[0].set_title("default labels", loc='right')

axes[1].plot(x, y, 'b')
axes[1].set_title("scientific notation labels", loc='right')
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
axes[1].xaxis.set_major_formatter(formatter)
axes[1].yaxis.set_major_formatter(formatter)

fig.tight_layout()


#%% 对数坐标/Log Plots: ax.loglog()/ax.semilogy/ax.semilogx/ax.set_xscale('log')/ax.set_yscale('log')
fig, axes = plt.subplots(1, 3, figsize=(12, 3))

x = np.linspace(0, 1e3, 100)
y1, y2 = x**3, x**4

axes[0].set_title('loglog')
axes[0].loglog(x, y1, 'b', x, y2, 'r')

axes[1].set_title('semilogy')
axes[1].semilogy(x, y1, 'b', x, y2, 'r')

axes[2].set_title('plot / set_xscale / set_yscale')
axes[2].plot(x, y1, 'b', x, y2, 'r')
axes[2].set_xscale('log')
axes[2].set_yscale('log')

fig.tight_layout()

