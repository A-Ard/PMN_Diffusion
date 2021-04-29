import numpy as np
import matplotlib.pyplot as plt
N=692
D=0.1
h=0.1
g=0.05


T=np.zeros((N+1,11))

T_1=62
T_11=181

for i in range(0, 10):
    T[0, i] = T_1

for j in range(0,N+1):
    T[j, 0] = T_1
    T[j, 10] = T_11

for j in range(1,N):
    for i in range(1, 10):
        T[j+1,i]=(T[j,i+1]+T[j,i-1])/2




file=open('data.dat','a')
for j in range(0,N+1):
    for i in range(0,10):
        file.write(str(T[j,i])+'  ')
    file.write('\n')
for i in range(0,10):
    file.write(str(round(T[N,i],3))+'\t')


file.close

x=np.linspace(0,10,11)
t=np.linspace(0,N,N+1)
def T(t,x):
    T=T[t,x]
    return T



