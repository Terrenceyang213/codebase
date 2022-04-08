# %% 
import sympy
sympy.init_printing()
from sympy import I, pi, oo

x = sympy.Symbol("x")
y = sympy.Symbol("y", real=True)
y.is_real
x.is_real is None
sympy.Symbol("z", imaginary=True).is_real

#%%
y = sympy.Symbol("y", positive=True)
sympy.sqrt(x * x)
#sympy.sqrt(x * y)
#sympy.init_printing()

# %%
