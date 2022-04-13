# %% tags:ml; model save and load; jason brownlee;
# pickle
# joblib

#%% tags:ml; model sl; pickle;
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

filename = './save/finalized_model.sav'
dump(model, open(filename,'wb'))

loaded_model = load(open(filename,'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
# 0.7874015748031497

# %% tags:ml; model sl; joblib;
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump
from joblib import load

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

filename = './save/finalized_model_joblib.sav'
dump(model, open(filename,'wb'))

loaded_model = load(open(filename,'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)
# 0.7874015748031497