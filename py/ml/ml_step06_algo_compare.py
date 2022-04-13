#%% tag: ml;algorithm compare
# In the example below 
# six different classification algorithms are compared on a single dataset:
## Logistic Regression
## Linear Discriminat Analysis
## k-Nearest Neighbors
## Classification and Regression Trees
## Naivve Bayes
## Support Vector Machines

#%% tag: ml; algorithm compare; 机器学习算法比较;
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

models = []
maxiter=500
models.append(('LR', LogisticRegression(max_iter=maxiter)))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('CART',DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC(max_iter=maxiter)))

results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = KFold(n_splits=10, random_state=7, shuffle=True)
    cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    print(f'{name}: {cv_results.mean():.4f} ({cv_results.std():.4f})')

fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()
# LR: 0.7722 (0.0497)
# LDA: 0.7670 (0.0480)
# KNN: 0.7110 (0.0508)
# CART: 0.6863 (0.0416)
# NB: 0.7591 (0.0390)
# SVM: 0.7605 (0.0347)


