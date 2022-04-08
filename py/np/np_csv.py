# tags:numpy csv, load csv, np csv

#%%
from numpy import loadtxt
from quantframe.sampconf import dataset_root

#%% numpy csv: load
url = dataset_root+"/pima-indians-diabetes.data.csv"
raw_data = open(url, 'rb')
data = loadtxt(raw_data, delimiter=",")
print(data.shape)