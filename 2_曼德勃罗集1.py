import numpy as np
import matplotlib.pyplot as plot 

x0=0 #初始值z0的x0
y0=0 #初始值z0的y0
zoom=3.0 #放大倍率
N=100 #最大迭代次数
R=2 #迭代半径
a=12.0 #绘制图的横轴大小
b=9.0 #绘制图的纵轴大小
step=0.005 #绘制点的步长

def iterate(c,N,R):
    z=c
    for i in range(N):
        if abs(z)>R: 
            return i
        z = z*z+c
    return N

x=np.arange(-a/(2.0*zoom)+x0,a/(2.0*zoom)+x0,step)
y=np.arange(b/(2.0*zoom)+y0,-b/(2.0*zoom)+y0,-step)
cx,cy=np.meshgrid(x, y)
c = cx + cy*1j
ufunc=np.frompyfunc(iterate,3,1)
Z=ufunc(c,N,R).astype(np.float)
plot.imshow(Z,extent=(-a/2.0,a/2.0,-b/2,b/2.0))
cb = plot.colorbar(orientation='vertical',shrink=1)
cb.set_label('iteration counts')
plot.show()