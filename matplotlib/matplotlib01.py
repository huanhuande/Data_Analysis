# -*- coding: UTF-8 -*-
# 散点图(scatter plots)

# 首先介绍一下numpy 的normal函数，很明显，这是生成正态分布的函数。
# 这个函数接受三个参数，分别表示正态分布的平均值，标准差，还有就是生成数组的长度。很好记。
#
# 然后是arctan2函数，这个函数接受两个参数，分别表示y数组和x数组，
# 然后返回对应的arctan(y/x)的值，结果是弧度制。
#
# 接下来用到了绘制散点图的scatter方法，首先当然是传入x和y数组，
# 接着s参数表示scale，即散点的大小；c参数表示color，我给他传的是根据角度划分的一个数组，
# 对应的就是每一个点的颜色（虽然不知道是怎么对应的，不过好像是一个根据数组内其他元素进行的相对的转换
# ，这里不重要了，反正相同的颜色赋一样的值就好了）；最后是alpha参数，表示点的透明度。
#
# 至于scatter函数的高级用法可以参见官方文档 scatter函数 或者help文档。
#
# 最后设置下坐标范围就好了。
from matplotlib.pyplot import *
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
scatter(X,Y, s=75, c=T, alpha=.5)
xlim(-1.5,1.5)
ylim(-1.5,1.5)
show()