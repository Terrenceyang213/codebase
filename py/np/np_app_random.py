# %% tags:numpy;np;random;随机数
import numpy as np

# random.multivariate_normal   # 多元正态随机

# random.rand(d0, d1, …, dn) 	
                        # 产生均匀分布的随机数 	dn为第n维数据的维度

# random.randn(d0, d1, …, dn) 	
                        # 产生标准正态分布随机数 	dn为第n维数据的维度

# random.randint(low[, high, size, dtype]) 	
                        # 产生随机整数 	low：最小值；high：最大值；size：数据个数

# random.random_sample([size]) 	
                        #在[0,1）内产生随机数 	size：随机数的shape，可以为元祖或者列表，[2,3]表示2维随机数，维度为（2,3）

# random.random([size]) # 同random_sample([size]) 	同random_sample([size])

# random.ranf([size]) 	# 同random_sample([size]) 	同random_sample([size])

# random.sample([size]))# 同random_sample([size]) 	同random_sample([size])

# random.choice(a[, size, replace, p]) 	
                        # 从a中随机选择指定数据 	a：1维数组 size：返回数据形状

# random.bytes(length) 	# 返回随机位 	length：位的长度


#%% tags:numpy;np;random;常用随机分布
# 函数名称	函数功能	
# beta(a, b[, size]) 	贝塔分布样本，在 [0, 1]内。 	 
# binomial(n, p[, size]) 	二项分布的样本。 	 
# chisquare(df[, size]) 	卡方分布样本。 	 
# dirichlet(alpha[, size]) 	狄利克雷分布样本。 	 
# exponential([scale, size]) 	指数分布 	 
# f(dfnum, dfden[, size]) 	F分布样本。 	 
# gamma(shape[, scale, size]) 	伽马分布 	 
# geometric(p[, size]) 	几何分布 	 
# gumbel([loc, scale, size]) 	耿贝尔分布。 	 
# hypergeometric(ngood, nbad, nsample[, size]) 	超几何分布样本。 	 
# laplace([loc, scale, size]) 	拉普拉斯或双指数分布样本 	 
# logistic([loc, scale, size]) 	Logistic分布样本 	 
# lognormal([mean, sigma, size]) 	对数正态分布 	 
# logseries(p[, size]) 	对数级数分布。 	 
# multinomial(n, pvals[, size]) 	多项分布 	 
# multivariate_normal(mean, cov[, size]) 	多元正态分布。 	 
# negative_binomial(n, p[, size]) 	负二项分布 	 
# noncentral_chisquare(df, nonc[, size]) 	非中心卡方分布 	 
# noncentral_f(dfnum, dfden, nonc[, size]) 	非中心F分布 	 
# normal([loc, scale, size]) 	正态(高斯)分布 	 
# pareto(a[, size]) 	帕累托（Lomax）分布 	 
# poisson([lam, size]) 	泊松分布 	 
# power(a[, size]) 	Draws samples in [0, 1] from a power distribution with positive exponent a - 1. 	 
# rayleigh([scale, size]) 	Rayleigh 分布 	 
# standard_cauchy([size]) 	标准柯西分布 	 
# standard_exponential([size]) 	标准的指数分布 	 
# standard_gamma(shape[, size]) 	标准伽马分布 	 
# standard_normal([size]) 	标准正态分布 (mean=0, stdev=1). 	 
# standard_t(df[, size]) 	Standard Student’s t distribution with df degrees of freedom. 	 
# triangular(left, mode, right[, size]) 	三角形分布 	 
# uniform([low, high, size]) 	均匀分布 	 
# vonmises(mu, kappa[, size]) 	von Mises分布 	 
# wald(mean, scale[, size]) 	瓦尔德（逆高斯）分布 	 
# weibull(a[, size]) 	Weibull 分布 	 
# zipf(a[, size]) 	齐普夫分布

#%% tags:numpy;np;random;randint(); 随机整数标量
np.random.randint(100,size=None)
# 16

np.random.randint(1,10,size=None) 
# Out[4]: 8

np.random.randint(1,10,size=(1,5)) 
# array([[9, 9, 4, 9, 8]])

#%% tags:numpy;np;random;rand(); 
np.random.rand()
# Out[12]: 0.3551799900015947

np.random.rand(5)
# array([0.23456081, 0.14399367, 0.70503724, 0.04764928, 0.04896364])

#%% tags:numpy;np;random;choice(); 

np.random.choice([1,2,3,4])
# 4

np.random.choice([1,2,3,4])
# 2

#%% tags:numpy;np;random;multivariate; 多元随机变量
a = np.random.multivariate_normal(
    mean=[0, 3],
    cov=[[1, 0.5],[0.5, 1]],
    size=1000)
# array([[-1.28104074,  3.00228909],
#        [-1.26942349,  2.92222427],
#        [ 0.92625369,  2.52124627],
#        [-0.57462629,  1.62449771],
#        [ 0.28688037,  2.8146925 ],
#        [ 0.3254171 ,  2.70331164],
#        [-0.7366178 ,  2.65254063],
#        [-2.0075996 ,  1.2108896 ],
#        [ 1.84618775,  3.02288973],
#        [-1.30926256,  2.13507995]])

a1 = a[:,0]
np.mean(a1),np.std(a1)
# (0.05160844800204821, 0.8574626638452654)

a2 = a[:,1]
np.mean(a2),np.std(a2)
# (2.8940988980071705, 1.0402762797098768)

np.cov(a1,a2)
# array([[0.91922547, 0.44458961],
#        [0.44458961, 0.92262048]])


