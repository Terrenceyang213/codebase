
#%% scatter_matrix
import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
url = r"E:/database/SampleData/Datasets/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
scatter_matrix(data)
plt.show()