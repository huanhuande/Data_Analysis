# -*- coding: UTF-8 -*-
# 等高线图(contour plots)

# 首先要明确等高线图是一个三维立体图，所以我们要建立一个二元函数f，
# 值由两个参数控制，(注意，这两个参数都应该是矩阵)。

# 然后我们需要用numpy的meshgrid函数生成一个三维网格，即，
# x轴由第一个参数指定，y轴由第二个参数指定。并返回两个增维后的矩阵，今后就用这两个矩阵来生成图像。

# 接着就用到coutourf函数了，所谓contourf，大概就是contour fill的意思吧，只填充，不描边；
# 这个函数主要是接受三个参数，分别是之前生成的x、y矩阵和函数值；接着是一个整数，大概就是表示等高线的密度了，有默认值；
# 然后就是透明度和配色问题了，cmap的配色方案这里不多研究。

# 随后就是contour函数了，很明显，这个函数是用来描线的。
# 用法可以类似的推出来，不解释了，需要注意的是他返回一个对象，这个对象一般要保留下来个供后续的加工细化。

# 最后就是用clabel函数来在等高线图上表示高度了，传入之前的那个contour对象；然后是inline属性，
# 这个表示是否清除数字下面的那条线，为了美观当然是清除了，而且默认的也是1；再就是指定线的宽度了，不解释，。

from matplotlib.pyplot import *

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)

X,Y=np.meshgrid(x,y)
contourf(X,Y,f(X,Y),8,alpha=.75,cmap=cm.hot)
C=contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)

clabel(C,inline=1,fontsize=10)
show()
