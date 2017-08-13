# -*- coding: UTF-8 -*-
# 填充图
# 这里主要是用到了fill_between函数。这个函数很好理解，
# 就是传入x轴的数组和需要填充的两个y轴数组；然后传入填充的范围，用where=来确定填充的区域；
# 最后可以加上填充颜色啦，透明度之类修饰的参数。
#
# 当然fill_between函数还有更加高级的用法，详见 fill_between用法 或者help文档。

from matplotlib.pylab import *
x=linspace(-3,3,100)
y1=np.sin(x)
y2=np.cos(x)
fill_between(x,y1,y2,where=(y1>=y2),color='red',alpha=0.25)
fill_between(x,y1,y2,where=(y1>y2),color='green',alpha=0.25)
plot(x,y1)
plot(x,y2)
show()