# %% 
import numpy as np
import pandas as pd

# Series is equipped with a set of string processing methods 
# that make it easy to operate on each element of the array. 
# Perhaps most importantly, these methods exclude missing/NA values automatically. 
# These are accessed via the Series’s str attribute 
# and generally have names matching the equivalent (scalar) built-in string methods. For example:
s = pd.Series(
        ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
    )

s.str.lower()
# 0       a
# 1       b
# 2       c
# 3    aaba
# 4    baca
# 5    <NA>
# 6    caba
# 7     dog
# 8     cat
# dtype: string

s.str.upper()
# 0       A
# 1       B
# 2       C
# 3    AABA
# 4    BACA
# 5    <NA>
# 6    CABA
# 7     DOG
# 8     CAT
# dtype: string