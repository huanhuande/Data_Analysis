# -*- coding: UTF-8 -*-
#   点阵图
# 这段代码的目的就是将一个矩阵直接转换为一张像照片一样的图，完整的进行显示。
#
# 前面的代码就是生成一个矩阵Z，不作解释。
#
# 接着用到了imshow函数，传人Z就可以显示出一个二维的图像了，图像的颜色是根据元素的值进行的自适应调整，
# 后面接了一些修饰性的参数，比如配色方案（cmap），零点位置（origin）。
#
# 最后用colorbar显示一个色条，可以不传参数，这里传进去shrink参数用来调节他的长度。

from matplotlib.pyplot import *

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=10
x=np.linspace(-3,3,3.5*n)
y=np.linspace(-3,3,3.0*n)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
imshow(Z,interpolation='nearest',cmap='bone',origin='lower')
colorbar(shrink=.92)
show()
