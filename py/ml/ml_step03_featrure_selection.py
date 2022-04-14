#%% tag:ml;feature selection;特征选择
# from Jason Brownlee <> chapter 8
# 1.Univariate Selection.
# 2.Recursive Feature Elimination.
# 3.Principle Component Analysis.
# 4.Feature Importance.
# http://scikit-learn.org/stable/modules/feature_selection.html

# %% tag:ml; feature; Univariate selection; 
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest # <1>
# <2> Compute chi-squared stats between each non-negative feature and class.
from sklearn.feature_selection import chi2 
                                            
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

# <3> SelectKBest.score_func:Function taking two arrays X and y, 
# <3> and returning a pair of arrays (scores, pvalues) or a single array with scores.
test = SelectKBest(score_func=chi2, k=4) 
fit = test.fit(X,Y)                     # <4>

# summarize scores 
set_printoptions(precision=3) 
print(fit.scores_) 
# [ 111.52  1411.887   17.605   53.108 2175.565  127.669    5.393  181.304]

features = fit.transform(X) 

# summarize selected features
print(features[0:5,:])
# [[148.    0.   33.6  50. ]
#  [ 85.    0.   26.6  31. ]
#  [183.    0.   23.3  32. ]
#  [ 89.   94.   28.1  21. ]
#  [137.  168.   43.1  33. ]]
# plas, test, mass and age


# %% tag:ml;feature; Recursive Feature Elimination; 

from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import RFE # <1>
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

# feature extraction
model = LogisticRegression()
rfe = RFE(estimator=model,n_features_to_select=4)
fit = rfe.fit(X,Y)
print("Num Features: {:d}".format(fit.n_features_ )) 
print("Selected Features: {}".format(fit.support_))
print("Feature Ranking: {}".format(fit.ranking_))
# Num Features: 4
# Selected Features: [ True  True False False False  True  True False]
# Feature Ranking: [1 1 3 4 5 1 1 2]

### 工作原理：发生了什么？

# %% tag:ml;feature; principal component analysis; 主成分分析


from pandas import read_csv
from sklearn.decomposition import PCA
                                            
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

pca = PCA(n_components=3)
fit = pca.fit(X)
# summarize components
print("Explained Variance: {}".format(fit.explained_variance_ratio_))
print(fit.components_)
# Explained Variance: [0.889 0.062 0.026]
# [[-0.002  0.098  0.016  0.061  0.993  0.014  0.001 -0.004]
#  [-0.023 -0.972 -0.142  0.058  0.095 -0.047 -0.001 -0.14 ]
#  [-0.022  0.143 -0.922 -0.307  0.021 -0.132 -0.001 -0.125]]

# %% tag:ml;feature; feature importance; 随机森林
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier

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

model = ExtraTreesClassifier()
model.fit(X,Y)
print(model.feature_importances_)
# [0.11  0.236 0.1   0.079 0.076 0.141 0.117 0.141]

# %%
