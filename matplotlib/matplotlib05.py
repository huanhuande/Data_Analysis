# -*- coding: UTF-8 -*-
#３Ｄ图
# 有点麻烦，需要用到的时候再说吧，不过原理也很简单，跟等高线图类似，先画图再描线，最后设置高度，都是一回事。


import numpy
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig=figure()
ax=Axes3D(fig)
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)

X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.cm.hot)
ax.contour(X,Y,Z,zdir='z',offset=-2,cmap=plt.cm.hot)
ax.set_zlim(-2,2)
show()
