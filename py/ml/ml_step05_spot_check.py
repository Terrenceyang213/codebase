# %% tag:ml;spot-check;算法抽查;
#Starting with two linear machine learning algorithms: 
## Logistic Regression. 
## Linear Discriminant Analysis. 
# Then looking at four nonlinear machine learning algorithms: 
## k-Nearest Neighbors. 
## Naive Bayes. 
## Classification and Regression Trees.
## Support Vector Machines.

# %% tag:ml; spot-check; Logistic;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_folds = 10
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = LogisticRegression(max_iter=3000) # <> max_iter
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7721633629528366

# %% tag:ml; spot-check; LDA;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_folds = 10
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = LinearDiscriminantAnalysis() # <> max_iter

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7669685577580315

# %% tag:ml; spot-check; KNN Classifier;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_folds = 10
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = KNeighborsClassifier() # <> max_iter

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7109876965140123

# %% tag:ml; spot-check; Naive Bayes;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_folds = 10
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = GaussianNB() # <> max_iter

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7591421736158578

# %% tag:ml; spot-check; Classification and Regression Trees;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_folds = 10
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = DecisionTreeClassifier() 

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.6941216678058784

# %% tag:ml; spot-check; SVM;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_folds = 10
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = SVC() 

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.760457963089542

# %% tag:ml; spot-check; Linear Regression;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = LinearRegression() 
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring
print(results.mean())
# -23.746501811313486

# %% tag:ml; spot-check; Ridge Regression;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from numpy import set_printoptions
set_printoptions(precision=3,suppress=True)

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = Ridge() 
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring

print(results.mean())
# -23.88989018505342


# %% tag:ml; spot-check; LASSO Regression;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from numpy import set_printoptions
set_printoptions(precision=3,suppress=True)

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = Lasso() 
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring

print(results.mean())
# -28.74589007585154

# %% tag:ml; spot-check; ElasticNet;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import ElasticNet
from numpy import set_printoptions
set_printoptions(precision=3,suppress=True)

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = ElasticNet()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring

print(results.mean())
# -31.1645737142

# %% tag:ml; spot-check; KNN Regressor;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from numpy import set_printoptions
set_printoptions(precision=3,suppress=True)

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = KNeighborsRegressor()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring

print(results.mean())
# -38.852320266666666
# %% tag:ml; spot-check; Decision Tree Regressor;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor # <>
from numpy import set_printoptions
set_printoptions(precision=3,suppress=True)

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = DecisionTreeRegressor() # <>
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring

print(results.mean())
# -21.178202352941174


# %% tag:ml; spot-check; SVM Regressor;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
from numpy import set_printoptions
set_printoptions(precision=3,suppress=True)

from quantframe.sampconf import dataset_root
filename = dataset_root+"/housing.csv"
colnames = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' , 
        'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:13]   
Y = array[:,13]


kfold = KFold(n_splits=10, random_state=7,shuffle=True)
model = SVR()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring) # <1> scoring

print(results.mean())
# -67.64140705473743

# %%
