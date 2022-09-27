import pandas as pd
import numpy as np

data = np.loadtxt('FFssFF.N.SGL.360K.Ramp.dat')

# select first and second column array
x = data[:,0]
y = data[:,1]

top =[]
bottom = []
mid =int(len(x)/2)

for i in range(mid,0,-1):
    top.append(y[i])
for i in range(mid,int(len(x))):
    bottom.append(y[i])
ans = (np.array(top) + np.array(bottom))/2

xbottom = []
for j in range(mid, int(len(x))):
    xbottom.append(x[j])
zaxis = np.array(xbottom)

file = np.stack((zaxis, ans), axis=1)

np.savetxt('avg.N.SGL.360K.Ramp.dat',file, fmt='%.2f', delimiter=' ')


