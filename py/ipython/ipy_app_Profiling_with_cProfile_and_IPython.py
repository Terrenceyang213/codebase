#%% 
# %timeit This magic command is meant for benchmarking (comparing the execution times of different versions of a function)
# cProfile breaks down the execution time into the contributions of all called functions
import numpy as np

#%% cprofile:%%prun
def step(*shape):
    # Create a random n-vector with +1 or -1 values.
    return 2 * (np.random.random_sample(shape)<.5) - 1

#%% profile code with ipython
# %prun
%%prun -s cumulative -q -l 10 -r 
# We profile the cell, sort the report by "cumulative time", limit it to 10 lines, and save it to a file named "prun0".

n = 10000
iterations = 50
x = np.cumsum(step(iterations, n), axis=0)
bins = np.arange(-30, 30, 1)
y = np.vstack( [np.histogram(x[i,:], bins)[0] for i in range(iterations)])

#%% profile code with shell
# $ python -m cProfile -o profresults myscript.py
# The file profresults will contain the dump of the profiling results of myscript.py.
import pstats
p = pstats.Stats('profresults')
p.strip_dirs().sort_stats("cumulative").print_stats()


#%% profile with line_profiler
import numpy as np
%load_ext line_profiler

#%% 
%%writefile simulation.py
import numpy as np

def step(*shape):
    # Create a random n-vector with +1 or -1 values.
    return 2 * (np.random.random_sample(shape)<.5) - 1

def simulate(iterations, n=10000):
    s = step(iterations, n)
    x = np.cumsum(s, axis=0)
    bins = np.arange(-30, 30, 1)
    y = np.vstack([np.histogram(x[i,:], bins)[0]
                   for i in range(iterations)])
    return y

#%%
from simulation import simulate
%lprun -T lprof0 -f simulate simulate(50)
print(open('lprof0', 'r').read())

#%% 
from quantframe.indicator.hurst import RSanalysis
%lprun -T lprof0 -f RSanalysis().run RSanalysis().run(np.random.random(100000))
print(open('lprof0', 'r').read())


#%% memory profile
%load_ext memory_profiler

#%% 
%%writefile memscript.py
def my_func():
    a = [1] * 1000000
    b = [2] * 9000000
    del b
    return a

#%%
from memscript import my_func
%mprun -T mprof0 -f my_func my_func()

#%% 使用memit
%%memit import numpy as np
np.random.randn(1000000)