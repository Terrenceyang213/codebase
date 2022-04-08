#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#%%
# The figure keeps track of all the child Axes, 
# a smattering of 'special' artists (titles, figure legends, etc), and the canvas. 
# (Don't worry too much about the canvas, it is crucial as it is the object that actually does the drawing to get you your plot, but as the user it is more-or-less invisible to you). 
# A figure can contain any number of Axes, but will typically have at least one.
# It's convenient to create the axes together with the figure, 
# but you can also add axes later on, allowing for more complex axes layouts.

fig = plt.figure()              # an empty figure with no Axes
fig, ax = plt.subplots()        # a figure with a single Axes
fig, axs = plt.subplots(2, 2)   # a figure with a 2x2 grid of Axes



#%% Axes
# it is the region of the image with the data space. 

# A given figure can contain many Axes, but a given Axes object can only be in one Figure. 
# The Axes contains two (or three in the case of 3D) Axis objects (be aware of the difference between Axes and Axis) 

# Axis objects take care of the data limits 
# (the data limits can also be controlled via the axes.Axes.set_xlim() and axes.Axes.set_ylim() methods). 

# Each Axes has a title (set via set_title()), an x-label (set via set_xlabel()), and a y-label set via set_ylabel()).
# The Axes class and its member functions are the primary entry point to working with the OO interface.


#%% Axis
# These are the number-line-like objects. 
# 
# They take care of setting the graph limits and generating the ticks (the marks on the axis) 
# and ticklabels (strings labeling the ticks). 
# 
# The location of the ticks is determined by a Locator object and the ticklabel strings are formatted by a Formatter. 
# The combination of the correct Locator and Formatter gives very fine control over the tick locations and labels.


#%% Artist
# Basically, everything you can see on the figure is an artist (even the Figure, Axes, and Axis objects). 
# This includes Text objects, Line2D objects, collections objects, Patch objects ... (you get the idea). 
# When the figure is rendered, all of the artists are drawn to the canvas. 
# Most Artists are tied to an Axes; 
# such an Artist cannot be shared by multiple Axes, or moved from one to another.



# %% matplotlib最好使用numpy中的array为输入
# All of plotting functions expect numpy.array or numpy.ma.masked_array as input. 
# 
# Classes that are 'array-like' such as pandas data objects and numpy.matrix may or may not work as intended. 
# It is best to convert these to numpy.array objects prior to plotting.

# from DataFrame to numpy.array
a = pd.DataFrame(np.random.rand(4, 5), columns = list('abcde'))
a_asarray = a.values


# from Series to numpy.array
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
s.to_numpy()
np.asarray(s)


# from numpy.Matrix to numpy.array
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)

# %% The object-oriented interface and the pyplot interface

# there are essentially two ways to use Matplotlib:
#   Explicitly create figures and axes, and call methods on them (the "object-oriented (OO) style").
#   Rely on pyplot to automatically create and manage the figures and axes, and use pyplot functions for plotting.
# 
# you should feel free to use either 
# however, it is preferable pick one of them and stick to it, instead of mixing them. 
# In general, we suggest to restrict pyplot to interactive plotting (e.g., in a Jupyter notebook), 
# and to prefer the OO-style for non-interactive plotting (in functions and scripts that are intended to be reused as part of a larger project).
# 通常，我们建议将pyplot限制为交互式绘图（例如，在Jupyter笔记本中），
# 并建议使用OO样式进行非交互式绘图（在打算作为较大项目的一部分重用的函数和脚本中） 。

# OO-Style
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
x = np.linspace(0, 2, 100)


fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label haha')  # Add an x-label to the axes.
ax.set_ylabel('y label yoho')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

# pyplot-style
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

# %% pylab is not recommanded
# from pylab import *
# This approach is strongly discouraged nowadays and deprecated.


# %% 对不同的数据，进行重复绘画的建议

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

# 分块图
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})


# %% Backends
# Matplotlib针对许多不同的用例和输出格式。
# 有些人从python shell交互地使用Matplotlib，并且在键入命令时弹出绘图窗口。
# 有些人运行 Jupyter笔记本并绘制内联图以进行快速数据分析。
# 其他人则将Matplotlib嵌入到PyQt或PyGObject等图形用户界面中，以构建丰富的应用程序。
# 有些人在批处理脚本中使用Matplotlib从数值模拟生成后记图像，还有一些人运行Web应用程序服务器以动态提供图形。
# 
# To support all of these use cases, Matplotlib can target different outputs, 
# and each of these capabilities is called a backend;
# the "frontend" is the user facing code, i.e., the plotting code, 
# whereas the "backend" does all the hard work behind-the-scenes to make the figure. 
#
# two types of backends:
#   user interface backends (for use in PyQt/PySide, PyGObject, Tkinter, wxPython, or macOS/Cocoa); also referred to as "interactive backends"
#   hardcopy backends to make image files (PNG, SVG, PDF, PS; also referred to as "non-interactive backends").

# %% Selecting a backend （暂时还用不上）
# 3 ways to configure backend
    # The rcParams["backend"] parameter in your matplotlibrc file
    # The MPLBACKEND environment variable
    # The function matplotlib.use()

# If multiple of these are configurations are present, the last one from the list takes precedence; 
# e.g. calling matplotlib.use() will override the setting in your matplotlibrc.

# https://matplotlib.org/stable/tutorials/introductory/usage.html#types-of-inputs-to-plotting-functions

#%% 交互式后端中使用matplotlib
# matplotlib.is_interactive() # 查询交互式变量
# 交互模式也可以通过matplotlib.pyplot.ion()和matplotlib.pyplot.ioff() 来开关。
plt.ion()
plt.plot([1.6, 2.7])
# This will pop up a plot window. Your terminal prompt will remain active, 
# so that you can type additional commands such as:
plt.title("interactive test")
plt.xlabel("index")
# On most interactive backends, the figure window will also be updated if you change it via the object-oriented interface. 
# E.g. get a reference to the Axes instance, and call a method of that instance:
ax = plt.gca()
ax.plot([3.1, 2.2])
# If you are using certain backends (like macosx), or an older version of Matplotlib, 
# you may not see the new line added to the plot immediately. 
# In this case, you need to explicitly call draw() in order to update the plot:
plt.draw()

#%%
import matplotlib.pyplot as plt
import numpy as np
plt.ioff()
plt.plot([1.6, 2.7])
# Nothing happened--or at least nothing has shown up on the screen 
# (unless you are using macosx backend, which is anomalous). 
# To make the plot appear, you need to do this:
plt.show()
# Now you see the plot, but your terminal command line is unresponsive; 
# pyplot.show() blocks the input of additional commands until you manually kill the plot window.

# What good is this--being forced to use a blocking function? 
# Suppose you need a script that plots the contents of a file to the screen. You want to look at that plot, and then end the script. 
# Without some blocking command such as show(), the script would flash up the plot and then end immediately, leaving nothing on the screen.

# In addition, non-interactive mode delays all drawing until show() is called; 
# this is more efficient than redrawing the plot each time a line in the script adds a new feature.



# %%
# pyplot
# The axis function in the example above takes a list of [xmin, xmax, ymin, ymax] 
# and specifies the viewport of the axes.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# %% 
# The example below illustrates plotting several lines with different format styles 
# in one function call using arrays.
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# %% Plotting with keyword strings
# Matplotlib allows you provide such an object with the data keyword argument. 
# If provided, then you may generate plots with the strings corresponding to these variables.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# %% Plotting with categorical variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

# %% Controlling line properties
# Lines have many attributes that you can set: linewidth, dash style, antialiased, etc; 
# lines.Line2D. There are several ways to set line properties

    # Use keyword args:
plt.plot(x, y, linewidth=2.0)

    # Use the setter methods of a Line2D instance. 
    # plot returns a list of Line2D objects; e.g., line1, line2 = plot(x1, y1, x2, y2). 
    # In the code below we will suppose that we have only one line 
    # so that the list returned is of length 1. 
    # We use tuple unpacking with line, to get the first element of that list:

line, = plt.plot(x, y, '-')
line.set_antialiased(False) # turn off antialiasing

    # Use setp. The example below uses a MATLAB-style function to set multiple properties on a list of lines. 
    # setp works transparently with a list of objects or a single object. 
    # You can either use python keyword arguments or MATLAB-style string/value pairs:

lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)


# %% Working with multiple figures and axes
# pyplot, have the concept of the current figure and the current axes. 
# All plotting functions apply to the current axes. 
# The function gca returns the current axes (a matplotlib.axes.Axes instance), 
# and gcf returns the current figure (a matplotlib.figure.Figure instance).
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# The figure call here is optional because a figure will be created if none exists, 
# just as an axes will be created (equivalent to an explicit subplot() call) if none exists.
plt.figure()

# The subplot call specifies numrows, numcols, plot_number 
# where plot_number ranges from 1 to numrows*numcols. 
# The commas in the subplot call are optional if numrows*numcols<10. 
# So subplot(211) is identical to subplot(2, 1, 1).
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()

# %%  You can create an arbitrary number of subplots and axes
# See Axes Demo for an example of placing axes manually 
# and Basic Subplot Demo for an example with lots of subplots.


#%% Multiple figures
# You can create multiple figures by using multiple figure calls with an increasing figure number.
# each figure can contain as many axes and subplots as your heart desires:
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot() by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title


# %% clf/cla
# You can clear the current figure with clf and the current axes with cla


# %% close
# the memory required for a figure is not completely released until 
# the figure is explicitly closed with close. 
# Deleting all references to the figure, and/or using the window manager to kill the window 
# in which the figure appears on the screen, 
# is not enough, because pyplot maintains internal references until close is called.


# %% Working with text
# text can be used to add text in an arbitrary location, and 
# xlabel, ylabel and title are used to add text in the indicated locations

# All of the text functions return a matplotlib.text.Text instance
mu, sigma = 150, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu={a:},\ \sigma={b:}$'.format(a=mu,b=sigma))
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# %% Annotating text
ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.00001),
             )

plt.ylim(-2, 2)
plt.show()


# %% Logarithmic and other nonlinear axes
# Changing the scale of an axis is easy:
# plt.xscale('log')

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()