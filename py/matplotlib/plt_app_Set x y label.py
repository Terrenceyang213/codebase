#%% import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

#ax.set(xlabel='time (s)', 
#       ylabel='voltage (mV)',
#       title='About as simple as it gets, folks')
plt.ylabel("time y")
ax.set_xlabel("time x")

plt.show()

# %% 改变label的颜色: ax.get_yticklabels()->label.set_color("blue")
###############################################################################
fig, ax1 = plt.subplots(figsize=(8, 4))

r = np.linspace(0, 5, 100)
a = 4 * np.pi * r ** 2  # area
v = (4 * np.pi / 3) * r ** 3  # volume


ax1.set_title("surface area and volume of a sphere", fontsize=16)
ax1.set_xlabel("radius [m]", fontsize=16)

ax1.plot(r, a, lw=2, color="blue")
ax1.set_ylabel(r"surface area ($m^2$)", fontsize=16, color="blue")
#把tick上的数字标记都上色
for label in ax1.get_yticklabels():
    label.set_color("blue")

fig.tight_layout()