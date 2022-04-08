#tags:basic steps for ml

#%% 
# 这里使用了相对路径，需要在py的上层文件夹
# (vnpy270) C:\base\codebase>python -m py.ml.ml_basic_step


#%% basic steps 1: preprocess
#####################################################################################
# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
import pandas
import numpy
from quantframe.sampconf import dataset_root
url = dataset_root+"/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
# [[ 0.64   0.848  0.15   0.907 -0.693  0.204  0.468  1.426]
#  [-0.845 -1.123 -0.161  0.531 -0.693 -0.684 -0.365 -0.191]
#  [ 1.234  1.944 -0.264 -1.288 -0.693 -1.103  0.604 -0.106]
#  [-0.845 -0.998 -0.161  0.155  0.123 -0.494 -0.921 -1.042]
#  [-1.142  0.504 -1.505  0.907  0.766  1.41   5.485 -0.02 ]]

#%% basic step 2: 算法评估, algorithm evaluation
# Evaluate using Cross Validation
##########################################################################

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
url = dataset_root+"/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7, shuffle=True)
model = LogisticRegression(solver='liblinear')
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))
# Accuracy: 77.086% (5.091%)

# %%
