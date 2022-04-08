# %% 线段简化
# Line segment simplification

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()

# %% 标记简化
# 该markevery参数允许进行简单的二次采样，或尝试进行均匀间隔的采样（沿x轴）。
plt.plot(x, y, markevery=10)


# %% 将线段切分成小块
# Splitting lines into smaller chunks
# 
# If you are using the Agg backend (see What is a backend?), 
# then you can make use of rcParams["agg.path.chunksize"] (default: 0) 
# This allows you to specify a chunk size, 
# and any lines with greater than that many vertices will be split into multiple lines, 
# each of which has no more than agg.path.chunksize many vertices. 
# (Unless agg.path.chunksize is zero, in which case there is no chunking.) 
# For some kind of data, chunking the line up into reasonable sizes can greatly decrease rendering time.

# The following script will first display the data without any chunk size restriction, 
# and then display the same data with a chunk size of 10,000. 
# The difference can best be seen when the figures are large, try maximizing the GUI and then interacting with them:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()


# %% 使用快速样式 
# 
import matplotlib.style as mplstyle
mplstyle.use('fast')

#它非常轻巧，因此可以与其他样式很好地配合使用，只需确保最后应用快速样式，以使其他样式不会覆盖设置：
mplstyle.use(['dark_background', 'ggplot', 'fast'])
