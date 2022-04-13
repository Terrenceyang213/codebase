#%% tags:ml; algorithm tuning; james brownlee;
# Models can have many parameters and finding the best combination of parameters can be treated as a search problem

#%% tags:ml; grid search parameter tuning; algorithm tuning;
import numpy as np
from pandas import read_csv
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV


from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

alphas = np.array([1, 0.1, 0.01, 0.001, 0.0001, 0])
param_grid = dict(alpha=alphas) # <1>{'alpha':[1, 0.1, 0.01, 0.001, 0.0001, 0]}
model = Ridge(max_iter=1000)
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(X,Y)
print(grid.best_score_)
print(grid.best_estimator_.alpha)
# 0.27610844129292433
# 1.0

# %% tags: random search parameter tuning; 
import numpy as np
from pandas import read_csv
from scipy.stats import uniform
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV


from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]


param_grid = {'alpha':uniform()} # <1>
model = Ridge(max_iter=1000)
rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, \
    n_iter=100, random_state=7)
rsearch.fit(X,Y)
print(rsearch.best_score_)
print(rsearch.best_estimator_.alpha)
# 0.27610755734028547
# 0.9779895119966027

# %%
