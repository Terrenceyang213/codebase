#%%
import pandas as pd
a=[ ['js',100,'cz',200], \
    ['zj',120,'xs',300], \
    ['zj',150,'xs',200], \
    ['js',200,'cz',200], \
    ['js',110,'wx',180], \
    ['js',300,'sz',250], \
    ['zj',210,'hz',280]  ]

df = pd.DataFrame(a)
df


#     0    1   2    3
# 0  js  100  cz  200
# 1  zj  120  xs  300
# 2  zj  150  xs  200
# 3  js  200  cz  200
# 4  js  110  wx  180
# 5  js  300  sz  250
# 6  zj  210  hz  280



# %%
# 两个条件筛选
df1 = df.copy()
df1.loc[(df1[0]=='js') & (df1[2]=='cz')]

# 	0	1	2	3
# 0	js	100	cz	200
# 3	js	200	cz	200



#%%
# 对筛选结果赋值
df1.loc[(df1[0]=='js') & (df1[2]=='cz'),1]=1000
df1

#    0	1	2	3
# 0	js	1000	cz	200
# 1	zj	120	    xs	300
# 2	zj	150	    xs	200
# 3	js	1000	cz	200
# 4	js	110	    wx	180
# 5	js	300	    sz	250
# 6	zj	210	    hz	280



# %%
# 对筛选结果复制：多列
df1.loc[(df1[0]=='js') & (df1[2]=='cz'),[1,3]]=988
df1
#   0	1	2	3
# 0	js	988	cz	988
# 1	zj	120	xs	300
# 2	zj	150	xs	200
# 3	js	988	cz	988
# 4	js	110	wx	180
# 5	js	300	sz	250
# 6	zj	210	hz	280



# %%
# 对满足条件的不同列，赋以不同的数据。
df1.loc[(df1[0]=='js') & (df1[2]=='cz'),[1,3]]=[1000,2000]
df1


#   0	1	2	3
# 0	js	1000	cz	2000
# 1	zj	120	    xs	300
# 2	zj	150	    xs	200
# 3	js	1000	cz	2000
# 4	js	110	    wx	180
# 5	js	300	    sz	250
# 6	zj	210	    hz	280



# %%
# 对满足条件的列，不同的行赋予不同的值

df1 = df.copy()
df1.loc[df1[0]=='js',1] = range(4)
# df1.loc[df1[0]=='js',1]= range(len(df1.loc[df1[0]=='js',1]))  4在赋值时往往并不可知
df1


#   0	1	2	3
# 0	js	0	cz	200
# 1	zj	120	xs	300
# 2	zj	150	xs	200
# 3	js	1	cz	200
# 4	js	2	wx	180
# 5	js	3	sz	250
# 6	zj	210	hz	280

df1=df.copy()
df1.loc[df1[0]=='js',1]=[31,32,33,34]
df1
#   0	1	2	3
# 0	js	31	cz	200
# 1	zj	120	xs	300
# 2	zj	150	xs	200
# 3	js	32	cz	200
# 4	js	33	wx	180
# 5	js	34	sz	250
# 6	zj	210	hz	280


#%%
# 利用mask进行条件选择
df1=df.copy()
df_mask = pd.DataFrame({1:[True]*7, 2:[True, False, True, False, True, False,True]})
df1.where(df_mask)

#    0	1	2	3
# 0	NaN	100	cz	NaN
# 1	NaN	120	NaN	NaN
# 2	NaN	150	xs	NaN
# 3	NaN	200	NaN	NaN
# 4	NaN	110	wx	NaN
# 5	NaN	300	NaN	NaN
# 6	NaN	210	hz	NaN

# if cond1:
#     exp1
# elif cond2:
#     exp2
# else:
#     exp3

# np.where(cond1, exp1, np.where(cond2, exp2, ...))

df1.where(df_mask, 1000) #1000是False和nan的填值

#      0	1	    2	    3
# 0	1000	100	    cz	    1000
# 1	1000	120	    1000	1000
# 2	1000	150	    xs	    1000
# 3	1000	200	    1000	1000
# 4	1000	110	    wx	    1000
# 5	1000	300	    1000	1000
# 6	1000	210	    hz	    1000


# %%
df.where( (df[0]=='js') & (df[3]==200) )





# %%


# %%
