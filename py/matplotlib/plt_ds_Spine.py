# %%  坐标轴的移动与隐藏
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl




#%% 坐标轴显示隐藏与移动：ax.spines.set_color("none")/ax.xaxis.set_ticks_position()/ax.spines.set_position()
x = np.linspace(-10, 10, 500)
y = np.sin(x) / x

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(x, y, linewidth=2)

# remove top and right spines
# axes的上轴与右轴一般为边框
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')

# remove top and right spine ticks
ax.xaxis.set_ticks_position('bottom') #tick刻度/spine轴
ax.yaxis.set_ticks_position('left')

# move bottom and left spine to x = 0 and y = 0
# axes下轴与左轴为笛卡尔坐标系
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
    
ax.set_xticks([-10, -5, 5, 10])
ax.set_yticks([0.5, 1])

# give each label a solid background of white, to not overlap with the plot line
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_bbox({'facecolor': 'white',
                    'edgecolor': 'black'})
    
fig.tight_layout()
