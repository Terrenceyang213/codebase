#%%
import numpy as np
q=np.random.rand(9000,9000)
q[3,0]=np.nan
#%%
q=np.random.rand(9000,9000)
q[3,0]=np.nan
def nan2last(x):
    sp = x.shape
    y = x.copy()
    for i in range(1,sp[0]):
        ix = np.nonzero(np.isnan(x[i,:]))[0]
        y[i,ix] = x[i-1,ix]
    return y
%time w=nan2last(q)

#%%
# q[3,0]=np.nan
from wttool import nan2last

%time w2=nan2last(q)

#%%
q[3,0]=np.nan
from wttool import nan2last2
%time w3=nan2last2(q)


# %%
