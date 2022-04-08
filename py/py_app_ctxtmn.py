#%%
import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('%s: %0.3f' % (label, end-start))

with timethis('counting'):
    n = 1000000
    while n>0:
        n-=1

# counting: 0.117