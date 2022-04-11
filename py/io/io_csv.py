# tags: load csv, standard library
#%%
from quantframe.sampconf import dataset_root
#%% csv:load
import csv 
import numpy
filename = dataset_root +'/pima-indians-diabetes.data.csv' 
raw_data = open(filename, 'r' ) 
reader = csv.reader(raw_data, delimiter=',' , quoting=csv.QUOTE_NONE) 
x = list(reader) 
data = numpy.array(x).astype('float')
print(data.shape)
# %%
