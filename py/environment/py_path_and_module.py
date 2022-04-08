#%% Python搜索模块的路径是由四部分构成的：
# 程序的主目录、
# PATHONPATH目录、 * 以分号隔开
# 标准链接库目录（sitepackages目录）
# .pth文件的目录， * 每行一个目录
# 这四部分的路径都存储在sys.path 列表中。

# 能修改的是PATHONPATH和在可搜索目录中的.pth文件
# add file: C:\ProgramData\Anaconda3\addition.path
# modify file : C:\base\quantbase\vnpy\vnpy-master\vnpy

import sys
sys.path
# ['c:\\base\\codebase\\python\\environment',
#  '',
#  'c:\\Users\\Terry\\.vscode\\extensions\\ms-toolsai.jupyter-2021.10.1101450599\\pythonFiles',
#  'c:\\Users\\Terry\\.vscode\\extensions\\ms-toolsai.jupyter-2021.10.1101450599\\pythonFiles\\lib\\python',
#  'C:\\ProgramData\\Anaconda3\\python36.zip',
#  'C:\\ProgramData\\Anaconda3\\DLLs',
#  'C:\\ProgramData\\Anaconda3\\lib',
#  'C:\\ProgramData\\Anaconda3',
### 'C:\\base\\quantbase\\vnpy\\vnpy-master\\vnpy', ###############
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages',
#  'd:\\uat\\quant\\quantaxis',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin',
#  'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\IPython\\extensions',
#  'C:\\Users\\Terry\\.ipython']


#%% 包导入基础
# 搜索路径是指Python搜索模块的路径前缀，在import 语句的路径上添加这些路径，以构成模块的绝对路径。
# 通常把存储模块的根目录称作容器目录，记作dir0，容器目录dir0必须包含在搜搜路径中。

# 例如，在dir0目录下，存在dri1/dir2/mod.py模块，那么导入该模块需要设置搜索路径为dir0，
# 并使用import  和路径导入该模块：

# dir0: C:\base\codebase\python : __init__.py所在位置，添加至addtion.pth
# dir1: numpy
# dir2: np_ds_create_arrays

import npy.np_ds_create_arrays

npy.np_ds_create_arrays.data1d
# array([1, 2, 3, 4])

from npy.np_ds_create_arrays import a1
print(a1)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 注：在模块链接上了之后，可以直接转移到定义


#%% __init__.py包文件
# 如果选择使用包导入，就必须多遵循一条约束：包导入语句的路径中，每个目录内都必须有__init__.py文件，否则包导入失败。

# 对于目录结构 dir0/dri1/dir2/mod.py 
import dir1.dir2.mod

# 必须遵守以下规则：
#     dir0是容器目录，不需要__init__.py文件，如果有，也会被忽略。
#     dir0必须列在模块搜索路径列表中，也就是说，dir0必须是主目录，或者列在PYTHONPATH环境变量中等。
#     dir1和dir2都必须包含一个__init__.py文件

# __init__.py文件是当 import 第一次遍历一个包目录时所运行的文件，
# 可以包含Python程序代码，也可以完全是空的。通常情况下，__init__.py文件扮演了包初始化的钩子，
# 替目录产生模块命名空间以及使用目录导入时实现from*行为的角色。

# __init__.py文件中的__all__变量决定 from ... import * 的行为。