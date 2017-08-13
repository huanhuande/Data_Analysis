# -*- coding: UTF-8 -*-
# 条形图(bar plots)

# 注意要手动导入pylab包，否则会找不到bar。。。
#
# 首先用numpy的arange函数生成一个[0,1,2,...,n]的数组。（用linspace也可以）
#
# 其次用numpy的uniform函数生成一个均匀分布的数组，
# 传入三个参数分别表示下界、上界和数组长度。并用这个数组生成需要显示的数据。
#
# 然后就是bar函数的使用了，基本用法也和之前的plot、scatter类似，传入横纵坐标和一些修饰性参数。
#
# 接着我们需要用for循环来为柱状图显示数字：用python的zip函数将X和Y1两两配对并循环遍历，
# 得到每一个数据的位置，然后用text函数在该位置上显示一个字符串（注意位置上的细节调整）。
# text传入横纵坐标，要显示的字符串，ha参数制定横向对齐，va参数制定纵向对齐。
#
# 最后调整下坐标范围，并且取消横纵坐标上的刻度以保持美观即可。
#
# 至于bar函数的具体用法可以参照 bar函数用法 或者help文档。

from matplotlib.pyplot import *

n=12
X=np.arange(n)

Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    text(x+0.4,y+0.05,'%.2f' % y,ha='center',va='bottom')

for x,y in zip(X,Y2):
    text(x+0.4,-y-0.05,'%.2f' % y,ha='center',va='top')

xlim(-.5,n)
xticks([])
ylim(-1.25,+1.25)
yticks([])
show()