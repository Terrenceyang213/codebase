#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.sandbox.stats.runs import runstest_1samp

#%% yt = yt-1 + \epsilon
s=1
x=[]
for i in range(1000):
    s=s+np.random.randn()
    x.append(s)
plt.plot(x)
plt.show()

# %% yt= yt-1*\epsilon, epsilon~B(n,0.5)
s=1
x=[]
for i in range(1000):
    tmp=np.random.rand()
    if tmp>0.5:
        s*=1.05
        x.append(s)
    else:
        s*=0.95
        x.append(s)
plt.plot(x)
plt.show()
# %%
