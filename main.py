import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
N=60
D=0.1
h=0.1
g=0.05
T_1=62
T_11=181


T=np.full((N+1,11),fill_value=T_1)




for j in range(0,N+1):
    T[j, 0] = T_1
    T[j, 10] = T_11

for j in range(1,N):
    for i in range(1, 10):
        T[j+1,i]=(T[j,i+1]+T[j,i-1])/2



file=open('data.dat','w')
for j in range(0,N+1):
    for i in range(0,11):
        file.write(str(T[j,i])+'  ')
    file.write('\n')



file.close


x=np.linspace(0,10,11)
t=np.linspace(0,N,N+1)
x, t = np.meshgrid(x, t)



fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(t, x, T)


plt.savefig('wykres.png')



