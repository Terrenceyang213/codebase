# tags:plot

#%% plot:histograms
from pandas import read_csv 
from matplotlib import pyplot
from quantframe.sampconf import dataset_root
filename = filename = dataset_root+"/pima-indians-diabetes.data.csv"
names = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
data = read_csv(filename, names=names)
data.hist() # <>
pyplot.show()


#%% plot:density
from pandas import read_csv 
from matplotlib import pyplot
from quantframe.sampconf import dataset_root
filename = filename = dataset_root+"/pima-indians-diabetes.data.csv"
names = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
data = read_csv(filename, names=names)
data.plot(kind='density' , # <>
    subplots=True, layout=(3,3), sharex=False)
pyplot.show()

# %% Box
from pandas import read_csv 
from matplotlib import pyplot
from quantframe.sampconf import dataset_root
filename = filename = dataset_root+"/pima-indians-diabetes.data.csv"
names = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
data = read_csv(filename, names=names)
data.plot(kind='box' , # <>
            subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()

# %% ml plot:多变量绘图, multivariate plots
# 相关性热力图
from quantframe.sampconf import dataset_root
from pandas import read_csv, set_option
from matplotlib import pyplot
import numpy as np
filename = dataset_root+"/pima-indians-diabetes.data.csv" 
names = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
data = read_csv(filename, names=names) 
set_option('display.width' , 100) # <>
set_option('precision' , 3)         # <>
correlations = data.corr(method='pearson') # <>

fig = pyplot.figure() 
ax = fig.add_subplot(111) 
cax = ax.matshow(correlations, vmin=-1, vmax=1) #<>
fig.colorbar(cax) 
ticks = np.arange(0,9,1) 
ax.set_xticks(ticks) 
ax.set_yticks(ticks) 
ax.set_xticklabels(names) 
ax.set_yticklabels(names)
pyplot.show()

# %% ml plot:scatter

