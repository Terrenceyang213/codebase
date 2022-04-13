#%% tags:ml; emsemble; 集成？;
# The three most popular methods for combining the predictions from different models are:
# · Bagging. Building multiple models (typically of the same type) from different subsamples of the training dataset.
# · Boosting. Building multiple models(typically of the same type) each of which learns to fix the prediction errors of a prior model in the sequence of models.
# · Voting. Building multiple models (typically of differing types) and simple statistics(like calculating the mean) are used to combine predictions.

# %% tags:ml; bagging; bagged decision Trees;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

 
kfold = KFold(n_splits=10, random_state=7,shuffle=True)
cart = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(base_estimator=cart \
            , n_estimators=num_trees, random_state=7)

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7578263841421736


# %% tags:ml; bagging; random forest; 随机森林; 
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_trees = 100
max_features = 3
kfold = KFold(n_splits=10, random_state=7, shuffle=True)
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7786739576213261

# %% tags:ml; bagging; extra forests; 
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_trees = 100
max_features = 7
kfold = KFold(n_splits=10, random_state=7, shuffle=True)
model = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features)

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.766866028708134

# %% tags:ml; boosting; adaboost; 
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_trees = 30
seed = 7
kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7552802460697198

# %% tags:ml; boosting; Stochastic Gradient Boosting; 
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

num_trees = 100
seed = 7
kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
model = GradientBoostingClassifier(n_estimators=num_trees, random_state=seed)

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7591934381408066

# %% tags:ml; voting; ensemble;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

kfold = KFold(n_splits=10, random_state=7, shuffle=True)
estimators = []
estimators.append(('logistic',LogisticRegression(max_iter=1000)))
estimators.append(('cart',DecisionTreeClassifier()))
estimators.append(('svm',SVC()))
ensemble = VotingClassifier(estimators)

results = cross_val_score(ensemble, X, Y, cv=kfold)
print(results.mean())
# 0.773479152426521
# %%
