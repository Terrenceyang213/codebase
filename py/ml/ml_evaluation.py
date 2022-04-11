#%% tag:ml;Performance;
# from Jason Brownlee <> chapter 9
# 1.Train and Test Sets.
# 2.k-fold Cross Validation.
# 3.Leave One Out Cross Validation.
# 4.Repeated Random Test-Train Splits.
# http://scikit-learn.org/stable/modules/feature_selection.html

# %% tag:ml;performance;split and train;

from pandas import read_csv 
from sklearn.model_selection import train_test_split # <1>
from sklearn.linear_model import LogisticRegression # <2>

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
#       preg	plas	pres	skin	test	mass	pedi	age	    class
# 0	    6	    148 	72  	35  	0	    33.6	0.627	50	    1
# 1	    1	    85	    66	    29	    0	    26.6	0.351	31	    0
# 2	    8	    183 	64  	0	    0	    23.3	0.672	32	    1
# 3	    1	    89	    66	    23	    94	    28.1	0.167	21	    0
# 4	    0	    137 	40  	35  	168	    43.1	2.288	33	    1
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]    

test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test \
    = train_test_split(X, Y, test_size=test_size, random_state=seed)

model = LogisticRegression()
model.fit(X_train, Y_train)

result = model.score(X_test, Y_test)
print("Accuracy:{}".format(result*100.0))
# Accuracy:78.74015748031496


# %% tag:ml;performance;k-fold validation;
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
seed = 7

kfold = KFold(n_splits=num_folds, random_state=seed,shuffle=True)
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: ({:3f}) ({:3f})".format(results.mean()*100.0, results.std()*100.0))
# Accuracy: (77.734108) (4.605141)

# %% tag:ml;performance; Leave one out cross validation;
from pandas import read_csv
from sklearn.model_selection import LeaveOneOut
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
loocv = LeaveOneOut()
model = LogisticRegression()
result = cross_val_score(model, X, Y, cv=loocv)
print("Accuracy: ({:3f}) ({:3f})".format(results.mean()*100.0, results.std()*100.0))
# Increase the number of iterations (max_iter) or scale the data as shown in:
#     https://scikit-learn.org/stable/modules/preprocessing.html
# Please also refer to the documentation for alternative solver options:
#     https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
#   extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
# c:\programdata\anaconda3\lib\site-packages\sklearn\linear_model\_logistic.py:765: ConvergenceWarning: lbfgs failed to converge (status=1):
# STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

# %% tag:ml; performance; repeated random test-train splits;
from pandas import read_csv
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

n_splits = 3
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=n_splits, test_size= test_size, random_state=seed)
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: ({:3f}) ({:3f})".format(results.mean()*100.0, results.std()*100.0))
# Output exceeds the size limit. Open the full output data in a text editor
# c:\programdata\anaconda3\lib\site-packages\sklearn\linear_model\_logistic.py:765: ConvergenceWarning: lbfgs failed to converge (status=1):
# STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

# %%
