#%% tag: ml;workflow pipeline;james brownlee;


#%% tag: ml; workflow pipeline; 工作流; 数据管道;
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

estimators = []
estimators.append(('standardize',StandardScaler()))
estimators.append(('lda',LinearDiscriminantAnalysis()))
model = Pipeline(estimators)

kfold = KFold(n_splits=10, random_state=7, shuffle= True)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7669685577580315

# Notice how we create a Python list of steps that are provided to the Pipeline 
# for process the data. Also notice how the Pipeline itself is treated like an 
# estimator and is evaluated in its entirety by the k-fold cross validation procedure.
# Running the example provides a summary of accuracy of the setup on the dataset.

#%% tag: ml; feature extraction; 特征提取; 数据管道;
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

from quantframe.sampconf import dataset_root
filename = dataset_root+"/pima-indians-diabetes.data.csv"
colnames = ['preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
df = read_csv(filename, names=colnames)
array = df.values   
X = array[:, 0:8]   
Y = array[:,8]

features = [] # <>
features.append(('pca',PCA(n_components=3)))
features.append(('select_best', SelectKBest(k=6)))
feature_union = FeatureUnion(features)

estimators = []
estimators.append(('feature_union',feature_union))
estimators.append(('logistic',LogisticRegression(max_iter=1000)))
model = Pipeline(estimators)

kfold = KFold(n_splits=10, random_state=7, shuffle= True)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
# 0.7721633629528366

# %%
