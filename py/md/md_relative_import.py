# tags:module,relative import

#%% question
# 同一个包中，一个子模块想要导入另一个子模块

#%% solution
# 假设包结构如下
# mypackage/
# mypackage/__init__.py
# mypackage/A/__init__.py
# mypackage/A/spam.py
# mypackage/A/grok.py
# mypackage/B/__init_.py
# mypackage/B/bar.py

# mypackage/A/spam.py 导入同一文件夹下面的grok
from . import grok

# mypackage/A/spam.py 导入不同目录中的bar
from .. import bar

#%% other1 不要硬编码

# mypackage/A/spam.py
from mypackage.A import grok #ok
from . import grok #OK

#%% other2 导入的形式
# 相对导入形式不能超出包的定义范围
from . import grok #OK
import .grok  #ERROR

#%% other3 运行方式
# 以脚本方式运行执行，相对导入会出错
# $python mypackage/A/spam.py #Relative imports fails

# 以模块调用方式运行，相对导入能成功
# $python -m mypackage.A.spam # Relative imports work

# 更多细节看PEP328
#%% other4 


