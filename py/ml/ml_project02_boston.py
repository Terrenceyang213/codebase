# %% 1. prepare problem
## a. load libs
import numpy as np
from numpy import arange
from matplotlib import pyplot
from pandas import set_option
from pandas import read_csv
from pandas.plotting import scatter_matrix
from sklearn.impute import KNNImputer

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor, kneighbors_graph
from sklearn.svm import SVR

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error


## b. load dataset
from quantframe.sampconf import dataset_root
from sklearn.utils import shuffle
from yaml import ScalarToken

from codebase.py.ml.ml_project01_iris import X_validation, Y_validation
filename = dataset_root +'/housing.csv'
names = ['CRIM' , 'ZN' , 'INDUS' , 'CHAS' , 'NOX' , 'RM' ,\
     'AGE' , 'DIS' , 'RAD' , 'TAX' , 'PTRATIO' , 'B' , 'LSTAT' , 'MEDV' ]
dataset = read_csv(filename , names = names)


# %% 2. summarize data
## a. descriptive statistics
print(dataset.shape)
# (506, 14)

print(dataset.dtypes)
# CRIM       float64
# ZN         float64
# INDUS      float64
# CHAS         int64
# NOX        float64
# RM         float64
# AGE        float64
# DIS        float64
# RAD          int64
# TAX        float64
# PTRATIO    float64
# B          float64
# LSTAT      float64
# MEDV       float64
# dtype: object

print(dataset.head(10))
#   CRIM	ZN	    INDUS	CHAS	NOX	    RM	    AGE	    DIS	    RAD	TAX	    PTRATIO	B	    LSTAT	MEDV
# 0	0.00632	18.0	2.31	0	    0.538	6.575	65.2	4.0900	1	296.0	15.3	396.90	4.98	24.0
# 1	0.02731	0.0	    7.07	0	    0.469	6.421	78.9	4.9671	2	242.0	17.8	396.90	9.14	21.6
# 2	0.02729	0.0	    7.07	0	    0.469	7.185	61.1	4.9671	2	242.0	17.8	392.83	4.03	34.7
# 3	0.03237	0.0	    2.18	0	    0.458	6.998	45.8	6.0622	3	222.0	18.7	394.63	2.94	33.4
# 4	0.06905	0.0	    2.18	0	    0.458	7.147	54.2	6.0622	3	222.0	18.7	396.90	5.33	36.2
# 5	0.02985	0.0	    2.18	0	    0.458	6.430	58.7	6.0622	3	222.0	18.7	394.12	5.21	28.7
# 6	0.08829	12.5	7.87	0	    0.524	6.012	66.6	5.5605	5	311.0	15.2	395.60	12.43	22.9
# 7	0.14455	12.5	7.87	0	    0.524	6.172	96.1	5.9505	5	311.0	15.2	396.90	19.15	27.1
# 8	0.21124	12.5	7.87	0	    0.524	5.631	100.0	6.0821	5	311.0	15.2	386.63	29.93	16.5
# 9	0.17004	12.5	7.87	0	    0.524	6.004	85.9	6.5921	5	311.0	15.2	386.71	17.10	18.9

set_option('precision',1)
print(dataset.describe())
#       CRIM	ZN	    INDUS	CHAS	NOX	    RM	    AGE	    DIS	    RAD	    TAX	    PTRATIO	B	    LSTAT	MEDV
# count	5.1e+02	506.0	506.0	5.1e+02	506.0	506.0	506.0	506.0	506.0	506.0	506.0	506.0	506.0	506.0
# mean	3.6e+00	11.4	11.1	6.9e-02	0.6	    6.3	    68.6	3.8	    9.5	    408.2	18.5	356.7	12.7	22.5
# std	8.6e+00	23.3	6.9	    2.5e-01	0.1	    0.7	    28.1	2.1	    8.7	    168.5	2.2	    91.3	7.1	    9.2
# min	6.3e-03	0.0	    0.5	    0.0e+00	0.4	    3.6	    2.9	    1.1	    1.0	    187.0	12.6	0.3	    1.7	    5.0
# 25%	8.2e-02	0.0	    5.2	    0.0e+00	0.4	    5.9	    45.0	2.1	    4.0	    279.0	17.4	375.4	6.9	    17.0
# 50%	2.6e-01	0.0	    9.7	    0.0e+00	0.5	    6.2	    77.5	3.2	    5.0	    330.0	19.1	391.4	11.4	21.2
# 75%	3.7e+00	12.5	18.1	0.0e+00	0.6	    6.6	    94.1	5.2	    24.0    666.0	20.2	396.2	17.0	25.0
# max	8.9e+01	100.0	27.7	1.0e+00	0.9	    8.8	    100.0	12.1	24.0	711.0	22.0	396.9	38.0	50.0

set_option('precision' , 2) 
print(dataset.corr(method='pearson'))
# 	        CRIM	ZN	    INDUS	CHAS	    NOX	    RM	    AGE	    DIS	    RAD	        TAX	    PTRATIO	B	    LSTAT	MEDV
# CRIM	    1.00	-0.20	0.41	-5.59e-02	0.42	-0.22	0.35	-0.38	6.26e-01	0.58	0.29	-0.39	0.46	-0.39
# ZN	    -0.20	1.00	-0.53	-4.27e-02	-0.52	0.31	-0.57	0.66	-3.12e-01	-0.31	-0.39	0.18	-0.41	0.36
# INDUS	    0.41	-0.53	1.00	6.29e-02	0.76	-0.39	0.64	-0.71	5.95e-01	0.72	0.38	-0.36	0.60	-0.48
# CHAS	    -0.06	-0.04	0.06	1.00e+00	0.09	0.09	0.09	-0.10	-7.37e-03	-0.04	-0.12	0.05	-0.05	0.18
# NOX	    0.42	-0.52	0.76	9.12e-02	1.00	-0.30	0.73	-0.77	6.11e-01	0.67	0.19	-0.38	0.59	-0.43
# RM	    -0.22	0.31	-0.39	9.13e-02	-0.30	1.00	-0.24	0.21	-2.10e-01	-0.29	-0.36	0.13	-0.61	0.70
# AGE	    0.35	-0.57	0.64	8.65e-02	0.73	-0.24	1.00	-0.75	4.56e-01	0.51	0.26	-0.27	0.60	-0.38
# DIS	    -0.38	0.66	-0.71	-9.92e-02	-0.77	0.21	-0.75	1.00	-4.95e-01	-0.53	-0.23	0.29	-0.50	0.25
# RAD	    0.63	-0.31	0.60	-7.37e-03	0.61	-0.21	0.46	-0.49	1.00e+00	0.91	0.46	-0.44	0.49	-0.38
# TAX	    0.58	-0.31	0.72	-3.56e-02	0.67	-0.29	0.51	-0.53	9.10e-01	1.00	0.46	-0.44	0.54	-0.47
# PTRATIO	0.29	-0.39	0.38	-1.22e-01	0.19	-0.36	0.26	-0.23	4.65e-01	0.46	1.00	-0.18	0.37	-0.51
# B	        -0.39	0.18	-0.36	4.88e-02	-0.38	0.13	-0.27	0.29	-4.44e-01	-0.44	-0.18	1.00	-0.37	0.33
# LSTAT	    0.46	-0.41	0.60	-5.39e-02	0.59	-0.61	0.60	-0.50	4.89e-01	0.54	0.37	-0.37	1.00	-0.74
# MEDV	    -0.39	0.36	-0.48	1.75e-01	-0.43	0.70	-0.38	0.25	-3.82e-01	-0.47	-0.51	0.33	-0.74	1.00

# strong correlation


## b. data visualizations   

### hist
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
pyplot.show()

### density
dataset.plot(kind='density', subplots=True, layout=(4,4), sharex=False, legend=False, fontsize=1)
pyplot.show()

### box
dataset.plot(kind='box', subplots=True, layout=(4,4), sharex=False, legend=False, fontsize=8)
pyplot.show()

### scatter plot matirx
scatter_matrix(dataset)
pyplot.show()

### correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(dataset.corr(), vmin=-1, vmax=1, interpolation='none')
fig.colorbar(cax)
ticks = np.arange(0,14,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()

# %% 3. prepare data
## a. data cleaning
## b. feature selection
## c. data transforms

# %% 4. evaluate algorithms
## a. split-out validation dataset
array = dataset.values
X = array[:, 0:13]
Y = array[:,13]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, \
    test_size=validation_size, random_state=seed)

## b. test options and evaluation metric
num_folds = 10
seed = 7
scoring = 'neg_mean_squared_error'

## c. spot check algorithms
models  = []
models.append(('LR', LinearRegression()))
models.append(("LASSO", Lasso()))
models.append(('EN', ElasticNet(max_iter=1000)))
models.append(('KNN', KNeighborsRegressor()))
models.append(('CART', DecisionTreeRegressor()))
models.append(('SVR',SVR()))

## c1. evaluate in turn
results = []
names = []
for name, model in models:
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print(f'{name}: {cv_results.mean():.4f},{cv_results.std():.4f}')
# LR: -22.0060,12.1889
# LASSO: -27.1058,13.1659
# EN: -27.9230,13.1564
# KNN: -39.8089,16.5080
# CART: -25.6005,17.4702
# SVR: -67.8247,32.8015

## d. compare algorithms
fig = pyplot.figure() 
fig.suptitle(' Algorithm Comparison' ) 
ax = fig.add_subplot(111) 
pyplot.boxplot(results) 
ax.set_xticklabels(names)
pyplot.show()

# %% 3a. 
# We suspect that the differing scales of the raw data may be negatively 
# impacting the skill of some of the algorithms. 
# Let’s evaluate the same algorithms with a standardized copy of the dataset.

## a. data cleaning
## b. feature selection
## c. data transforms

### standardize the dataset
pipelines = []
pipelines.append(('ScaledLR', \
    Pipeline([('Scaler', StandardScaler()),('LR', LinearRegression())])
    ))
pipelines.append(('ScaledLASSO', \
    Pipeline([('Scaler', StandardScaler()),('LASSO', Lasso())])
    ))
pipelines.append(('ScaledEN',\
    Pipeline([('Scaler', StandardScaler()),('EN', ElasticNet())])
    ))
pipelines.append(('ScaledKNN',\
    Pipeline([('Scaler', StandardScaler()),('KNN', KNeighborsRegressor())])
    ))
pipelines.append(('ScaledCART',\
    Pipeline([('Scaler', StandardScaler()),('CART', DecisionTreeRegressor())])
    ))
pipelines.append(('ScaledSVR',\
    Pipeline([('Scaler', StandardScaler()),('SVR', SVR())])
    ))
results = []
names = []
for name, model in pipelines:
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print(f'{name}: {cv_results.mean():.4f},{cv_results.std():.4f}')
# ScaledLR: -22.0060,12.1889
# ScaledLASSO: -27.2059,12.1244
# ScaledEN: -28.3012,13.6091
# ScaledKNN: -21.4569,15.0162
# ScaledCART: -26.4089,17.8796
# ScaledSVR: -29.5704,18.0530

# %% 4a. evaluate

## d. compare algorithms
fig = pyplot.figure() 
fig.suptitle('Scaled Algorithm Comparison') 
ax = fig.add_subplot(111) 
pyplot.boxplot(results) 
ax.set_xticklabels(names)
pyplot.show()
# KNN is best

# %% 5. improve accuracy
## a. algorithm tuning
### KNN tuning
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
k_values = np.array(range(1,23,2))
param_grid = dict(n_neighbors = k_values)
model = KNeighborsRegressor()
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(rescaledX, Y_train)

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_)) 
# Best: -19.497829 using {'n_neighbors': 1}
means = grid_result.cv_results_['mean_test_score' ] 
stds = grid_result.cv_results_['std_test_score' ] 
params = grid_result.cv_results_['params' ] 
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
# -19.497829 (15.769847) with: {'n_neighbors': 1}
# -19.977984 (13.803973) with: {'n_neighbors': 3}
# -21.270967 (14.833544) with: {'n_neighbors': 5}
# -21.577292 (14.952592) with: {'n_neighbors': 7}
# -21.001075 (14.701297) with: {'n_neighbors': 9}
# -21.490306 (14.866957) with: {'n_neighbors': 11}
# -21.268533 (14.454969) with: {'n_neighbors': 13}
# -21.968092 (14.209894) with: {'n_neighbors': 15}
# -22.739880 (14.492752) with: {'n_neighbors': 17}
# -23.506901 (14.903224) with: {'n_neighbors': 19}
# -24.240303 (15.156565) with: {'n_neighbors': 21}

# %% b. ensembles
ensembles = [] 
ensembles.append(('ScaledAB' , \
    Pipeline([('Scaler' , StandardScaler()),('AB' , AdaBoostRegressor())])
    )) 
ensembles.append(('ScaledGBM' , \
    Pipeline([('Scaler' , StandardScaler()),('GBM' , GradientBoostingRegressor())])
    )) 
ensembles.append(('ScaledRF' , \
    Pipeline([(' Scaler' , StandardScaler()),('RF' , RandomForestRegressor())])
    )) 
ensembles.append(('ScaledET' , \
    Pipeline([(' Scaler' , StandardScaler()),('ET' ,ExtraTreesRegressor())])
    ))
results = [] 
names = [] 
for name, model in ensembles: 
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True) 
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring) 
    results.append(cv_results) 
    names.append(name) 
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
# ScaledAB: -15.672530 (8.159538)
# ScaledGBM: -11.024365 (8.706587)
# ScaledRF: -12.447849 (8.750129)
# ScaledET: -9.001900 (6.429285)

# Compare Algorithms 
fig = pyplot.figure() 
fig.suptitle(' Scaled Ensemble Algorithm Comparison' ) 
ax = fig.add_subplot(111) 
pyplot.boxplot(results) 
ax.set_xticklabels(names)
pyplot.show()
# ScaledET is best

# %% Tune scaled ET
scaler = StandardScaler().fit(X_train) 
rescaledX = scaler.transform(X_train) 
param_grid = dict(n_estimators=np.array([50,100,150,200,250,300,350,400])) 
model = ExtraTreesRegressor(random_state=seed) 
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
grid_result = grid.fit(rescaledX, Y_train)

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_)) 
means = grid_result.cv_results_['mean_test_score' ] 
stds = grid_result.cv_results_['std_test_score' ] 
params = grid_result.cv_results_['params' ] 
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
# Best: -9.016279 using {'n_estimators': 150}
# -9.431419 (6.682316) with: {'n_estimators': 50}
# -9.141589 (6.323830) with: {'n_estimators': 100}
# -9.016279 (6.244052) with: {'n_estimators': 150}
# -9.066266 (6.212076) with: {'n_estimators': 200}
# -9.141895 (6.328563) with: {'n_estimators': 250}
# -9.162757 (6.407527) with: {'n_estimators': 300}
# -9.161324 (6.423344) with: {'n_estimators': 350}
# -9.152246 (6.491571) with: {'n_estimators': 400}

# %% 6. finalize model
## a. predictions on validation dataset
### prepare the model
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
model = ExtraTreesRegressor(random_state=seed, n_estimators=150)
model.fit(rescaledX, Y_train)

### transform the validation dataset
rescaledValidationX = scaler.transform(X_validation)
predictions = model.predict(rescaledValidationX)
print(mean_squared_error(Y_validation, predictions))
# 12.74953946840959


## b. create standalone model on entire training dataset
## c. save model for later use

