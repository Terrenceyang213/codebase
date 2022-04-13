#%% tags:ml; first project; jason brownlee;
# the classification of iris flowers

# %% 1. prepare problem
## a. load libs
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from numpy import set_printoptions
set_printoptions(precision=4,suppress=True)

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

## b. load dataset
from quantframe.sampconf import dataset_root
filename = dataset_root + '/iris.csv'
names = ['sepal-length' , 'sepal-width' , 'petal-length' , 'petal-width' , 'class']
dataset = read_csv(filename, names=names)


# %% 2. summarize data
## Dimensions of the dataset. 
## Peek at the data itself. 
## Statistical summary of all attributes.
## Breakdown of the data by the class variable

# a. descriptive statistics
## Dimensions of the dataset. 
print(dataset.shape)
(150, 5)

## Peek at the data itself.
print(dataset.head(20))
#     sepal-length  sepal-width  petal-length  petal-width        class
# 0            5.1          3.5           1.4          0.2  Iris-setosa
# 1            4.9          3.0           1.4          0.2  Iris-setosa
# 2            4.7          3.2           1.3          0.2  Iris-setosa
# 3            4.6          3.1           1.5          0.2  Iris-setosa
# 4            5.0          3.6           1.4          0.2  Iris-setosa
# 5            5.4          3.9           1.7          0.4  Iris-setosa
# 6            4.6          3.4           1.4          0.3  Iris-setosa
# 7            5.0          3.4           1.5          0.2  Iris-setosa
# 8            4.4          2.9           1.4          0.2  Iris-setosa
# 9            4.9          3.1           1.5          0.1  Iris-setosa


## Statistical summary of all attributes.
print(dataset.describe())
# 	    sepal-length	sepal-width	petal-length	petal-width
# count	    150.000000	150.000000	150.000000	    150.000000
# mean	    5.843333	3.054000	3.758667	    1.198667
# std	    0.828066	0.433594	1.764420	    0.763161
# min	    4.300000	2.000000	1.000000	    0.100000
# 25%	    5.100000	2.800000	1.600000	    0.300000
# 50%	    5.800000	3.000000	4.350000	    1.300000
# 75%	    6.400000	3.300000	5.100000	    1.800000
# max	    7.900000	4.400000	6.900000	    2.500000


## class distribution 
print(dataset.groupby('class' ).size())
# class
# Iris-setosa        50
# Iris-versicolor    50
# Iris-virginica     50
# dtype: int64


# b. data visualizations
## Univariate plots to better understand each attribute. 
## Multivariate plots to better understand the relationships between attributes.

## Univariate Plots
dataset.plot(kind='box' , subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

dataset.hist()
pyplot.show()

## Multivariate plots
scatter_matrix(dataset) 
pyplot.show()

# %% 3. prepare data
## a. data cleaning
## b. feature selection
## c. data transforms

# %% 4. evaluate algorithms

## a. split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, \
    test_size=validation_size, random_state=seed)

## b. test options and evaluation metric

# We will use 10-fold cross validation to estimate accuracy.
# This will split our dataset into 10 parts, train on 9 and test on 1 and repeat for all combinations of train-test splits. 
# We are using the metric of accuracy to evaluate models. 
# This is a ratio of the number of correctly predicted instances divided by the total number of instances in the dataset multiplied by 100 to give a percentage (e.g. 95% accurate). 
# We will be using the scoring variable when we run build and evaluate each model next.

## c. spot check algorithms
#  Logistic Regression (LR). 
#  Linear Discriminant Analysis (LDA). 
#  k-Nearest Neighbors (KNN). 
#  Classification and Regression Trees (CART). 
#  Gaussian Naive Bayes (NB).
#  Support Vector Machines (SVM)
models = []
models.append(('LR',LogisticRegression(max_iter=1000)))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC()))

results = []
names = []
for name, model in models:
    kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print( f'{name}: {cv_results.mean():.4f}, {cv_results.std():.4f}')
    print(f'{name}:{cv_results}')
# LR: 0.9833, 0.0333
# LDA: 0.9750, 0.0382
# KNN: 0.9833, 0.0333
# CART: 0.9583, 0.0768
# NB: 0.9667, 0.0408
# SVM: 0.9833, 0.0333


## d. compare algorithms
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()

# %% 5. improve accuracy
## a. algorithm tuning
## b. ensembles

# %% 6. finalize model
## a. predictions on validation dataset

# The KNN algorithm was the most accurate model that we tested.lidation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
# 0.9

print(confusion_matrix(Y_validation, predictions))
# [[ 7  0  0]
#  [ 0 11  1]
#  [ 0  2  9]]

print(classification_report(Y_validation, predictions))
#                  precision    recall  f1-score   support

#     Iris-setosa       1.00      1.00      1.00         7
# Iris-versicolor       0.85      0.92      0.88        12
#  Iris-virginica       0.90      0.82      0.86        11

#        accuracy                           0.90        30
#       macro avg       0.92      0.91      0.91        30
#    weighted avg       0.90      0.90      0.90        30


## b. create standalone model on entire training dataset
## c. save model for later use
# %%
