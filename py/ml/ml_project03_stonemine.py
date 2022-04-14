# %% Load libraries 
import numpy 
from matplotlib import pyplot 
from pandas import read_csv 
from pandas import set_option 
from pandas.plotting import scatter_matrix 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import KFold 
from sklearn.model_selection import cross_val_score 

from sklearn.model_selection import GridSearchCV 
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.pipeline import Pipeline 

from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.naive_bayes import GaussianNB 
from sklearn.svm import SVC 

from sklearn.ensemble import AdaBoostClassifier 
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

# %%  load data
from quantframe.sampconf import dataset_root
url = dataset_root + '/sonar.csv'
dataset = read_csv(url, header=None)

#%% summarize data
print(dataset.shape)

set_option('display.max_rows', 500)
print(dataset.dtypes)

set_option('display.width', 100)
print(dataset.head(10))

set_option('precision', 3)
print(dataset.describe())

# class distribution
print(dataset.groupby(60).size())

# %% data visualization
# hist
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
pyplot.show()

# density
dataset.plot(kind='density' , subplots=True, layout=(8,8), sharex=False, legend=False, fontsize=1)
pyplot.show()

# box and whisker plots
dataset.plot(kind='box' , subplots=True, layout=(8,8), sharex=False, legend=False, fontsize=1)
pyplot.show()

# correlation
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(dataset.corr(), vmin=-1, vmax=1, interpolation='none')
fig.colorbar(cax)
pyplot.show()

# %% split-out validation dataset
array = dataset.values
X = array[:,0:60].astype(float) 
Y = array[:,60] 
validation_size = 0.20 
seed = 7 
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y,\
    test_size=validation_size, random_state=seed)

# test options and evaluation metric
num_folds = 10
seed = 7
scoring = 'accuracy'

# %% spot-check algorithms
models = [] 
models.append((' LR' , LogisticRegression(max_iter=1000))) 
models.append((' LDA' , LinearDiscriminantAnalysis())) 
models.append((' KNN' , KNeighborsClassifier())) 
models.append((' CART' , DecisionTreeClassifier())) 
models.append((' NB' , GaussianNB()))
models.append((' SVM' , SVC(max_iter=1000)))


results = [] 
names = [] 
for name, model in models: 
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True) 
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring) 
    results.append(cv_results) 
    names.append(name) 
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
#  LR: 0.777574 (0.088423)
#  LDA: 0.778676 (0.093570)
#  KNN: 0.758824 (0.106417)
#  CART: 0.775735 (0.080514)
#  NB: 0.682721 (0.136040)
#  SVM: 0.765074 (0.087519)

# %% compare algorithms
# Compare Algorithms 
fig = pyplot.figure() 
fig.suptitle(' Algorithm Comparison' ) 
ax = fig.add_subplot(111) 
pyplot.boxplot(results) 
ax.set_xticklabels(names)
pyplot.show()
# 数据量纲可能对算法效果有影响

# %% standardize the dataset
pipelines = []
pipelines.append(('ScaledLR', \
    Pipeline([('Scaler' , StandardScaler()),('LR' , LogisticRegression())])
    ))
pipelines.append(('ScaledLDA', \
    Pipeline([('Scaler' , StandardScaler()),('LDA' , LinearDiscriminantAnalysis())])
    ))

pipelines.append(('ScaledKNN', \
    Pipeline([('Scaler' , StandardScaler()),('KNN' , KNeighborsClassifier())])
    ))

pipelines.append(('ScaledCART', \
    Pipeline([('Scaler' , StandardScaler()),('CART' , DecisionTreeClassifier())])
    ))

pipelines.append(('ScaledNB', \
    Pipeline([('Scaler' , StandardScaler()),('NB' , GaussianNB())])
    ))

pipelines.append(('ScaledSVM', \
    Pipeline([('Scaler' , StandardScaler()),('SVM' , SVC())])
    ))

results = []
names = []

for name, model in pipelines: 
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True) 
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring) 
    results.append(cv_results) 
    names.append(name) 
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
# ScaledLR: 0.754412 (0.067926)
# ScaledLDA: 0.778676 (0.093570)
# ScaledKNN: 0.808456 (0.107996)
# ScaledCART: 0.752574 (0.106909)
# ScaledNB: 0.682721 (0.136040)
# ScaledSVM: 0.826103 (0.081814)

# %% compare algorithms
fig = pyplot.figure() 
fig.suptitle('Scaled Algorithm Comparison' ) 
ax = fig.add_subplot(111) 
pyplot.boxplot(results) 
ax.set_xticklabels(names)
pyplot.show()

# %% tuning knn
scaler = StandardScaler().fit(X_train) 
rescaledX = scaler.transform(X_train) 
neighbors = [1,3,5,7,9,11,13,15,17,19,21] 
param_grid = dict(n_neighbors=neighbors) 
model = KNeighborsClassifier() 
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True) 
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold) 
grid_result = grid.fit(rescaledX, Y_train)
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score' ] 
stds = grid_result.cv_results_['std_test_score' ] 
params = grid_result.cv_results_['params' ] 
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
# Best: 0.836029 using {'n_neighbors': 1}
# 0.836029 (0.079487) with: {'n_neighbors': 1}
# 0.813603 (0.088021) with: {'n_neighbors': 3}
# 0.814338 (0.096870) with: {'n_neighbors': 5}
# 0.777574 (0.120387) with: {'n_neighbors': 7}
# 0.730147 (0.099376) with: {'n_neighbors': 9}
# 0.741544 (0.073970) with: {'n_neighbors': 11}
# 0.710662 (0.105829) with: {'n_neighbors': 13}
# 0.723162 (0.080983) with: {'n_neighbors': 15}
# 0.698897 (0.072669) with: {'n_neighbors': 17}
# 0.710662 (0.091337) with: {'n_neighbors': 19}
# 0.698897 (0.091195) with: {'n_neighbors': 21}

# %% tuning svm
scaler = StandardScaler().fit(X_train) 
rescaledX = scaler.transform(X_train) 
c_values = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0, 1.3, 1.5, 1.7, 2.0] 
kernel_values = ['linear' , 'poly' , 'rbf' , 'sigmoid' ] 
param_grid = dict(C=c_values, kernel=kernel_values) 
model = SVC() 
kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True) 
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold) 
grid_result = grid.fit(rescaledX, Y_train) 
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_)) 
means = grid_result.cv_results_['mean_test_score' ] 
stds = grid_result.cv_results_['std_test_score' ] 
params = grid_result.cv_results_['params' ] 
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))
# Best: 0.850000 using {'C': 1.7, 'kernel': 'rbf'}
# 0.748529 (0.069953) with: {'C': 0.1, 'kernel': 'linear'}
# 0.582721 (0.127062) with: {'C': 0.1, 'kernel': 'poly'}
# 0.601103 (0.184435) with: {'C': 0.1, 'kernel': 'rbf'}
# 0.712868 (0.116579) with: {'C': 0.1, 'kernel': 'sigmoid'}
# 0.754412 (0.082337) with: {'C': 0.3, 'kernel': 'linear'}
# 0.644118 (0.099873) with: {'C': 0.3, 'kernel': 'poly'}
# 0.742279 (0.081853) with: {'C': 0.3, 'kernel': 'rbf'}
# 0.748529 (0.069953) with: {'C': 0.3, 'kernel': 'sigmoid'}
# 0.765809 (0.070336) with: {'C': 0.5, 'kernel': 'linear'}
# 0.704779 (0.098225) with: {'C': 0.5, 'kernel': 'poly'}
# 0.784559 (0.068922) with: {'C': 0.5, 'kernel': 'rbf'}
# 0.760662 (0.065632) with: {'C': 0.5, 'kernel': 'sigmoid'}
# 0.759926 (0.083206) with: {'C': 0.7, 'kernel': 'linear'}
# 0.759559 (0.093807) with: {'C': 0.7, 'kernel': 'poly'}
# 0.814338 (0.059832) with: {'C': 0.7, 'kernel': 'rbf'}
# 0.761029 (0.079602) with: {'C': 0.7, 'kernel': 'sigmoid'}
# 0.765441 (0.066964) with: {'C': 0.9, 'kernel': 'linear'}
# 0.789706 (0.094189) with: {'C': 0.9, 'kernel': 'poly'}
# 0.808088 (0.062884) with: {'C': 0.9, 'kernel': 'rbf'}
# 0.760662 (0.079898) with: {'C': 0.9, 'kernel': 'sigmoid'}
# 0.771691 (0.062141) with: {'C': 1.0, 'kernel': 'linear'}
# 0.814338 (0.093230) with: {'C': 1.0, 'kernel': 'poly'}
# 0.825735 (0.072291) with: {'C': 1.0, 'kernel': 'rbf'}
# 0.754779 (0.085671) with: {'C': 1.0, 'kernel': 'sigmoid'}
# ...
# 0.778676 (0.085856) with: {'C': 2.0, 'kernel': 'linear'}
# 0.838971 (0.072879) with: {'C': 2.0, 'kernel': 'poly'}
# 0.850000 (0.081776) with: {'C': 2.0, 'kernel': 'rbf'}
# 0.730147 (0.056579) with: {'C': 2.0, 'kernel': 'sigmoid'}

# %% ensembles 
ensembles = [] 
ensembles.append(('AB' , AdaBoostClassifier())) 
ensembles.append(('GBM' , GradientBoostingClassifier())) 
ensembles.append(('RF' , RandomForestClassifier())) 
ensembles.append(('ET' , ExtraTreesClassifier())) 
results = [] 
names = [] 
for name, model in ensembles: 
    kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True) 
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring) 
    results.append(cv_results) 
    names.append(name) 
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
# AB: 0.782721 (0.072445)
# GBM: 0.772059 (0.123071)
# RF: 0.790074 (0.064153)
# ET: 0.873897 (0.049134)
# %% compare algorithms
# Compare Algorithms 
fig = pyplot.figure() 
fig.suptitle(' Ensemble Algorithm Comparison' ) 
ax = fig.add_subplot(111) 
pyplot.boxplot(results) 
ax.set_xticklabels(names)
pyplot.show()

# %%
# prepare the model 
scaler = StandardScaler().fit(X_train) 
rescaledX = scaler.transform(X_train) 
model = KNeighborsClassifier(n_neighbors=1) 
model.fit(rescaledX, Y_train) 

# estimate accuracy on validation dataset 
rescaledValidationX = scaler.transform(X_validation) 
predictions = model.predict(rescaledValidationX)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions)) 
print(classification_report(Y_validation, predictions))
# 0.8095238095238095
# [[21  6]
#  [ 2 13]]
#               precision    recall  f1-score   support

#            M       0.91      0.78      0.84        27
#            R       0.68      0.87      0.76        15

#     accuracy                           0.81        42
#    macro avg       0.80      0.82      0.80        42
# weighted avg       0.83      0.81      0.81        42


