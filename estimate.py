from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt
import random 
#random_float_list = []
size = 10 #m
range = 0.01
x = np.arange(1, size+range+1, range)
wall_y1 = 0*x+1.0
wall_y2 = 0*x+size+1
x2 = x
print(x)
#wall_x1 = np.arange(0, 11, 0.1) + 3
#wall_x2 = np.arange(0, 11, 0.1) + 33
print('Values of x: ', x)
print('Values of y: ', wall_y1)
plt.figure()
plt.plot(x, wall_y1,'b')
plt.plot(x, wall_y2,'b')
#plt.figure()
plt.plot(wall_y1, x,'b')
plt.plot(wall_y2, x,'b')
sn=50
mi=[]
sum=[]
iii=0
cell_range = 0.5
cell_nr = 10/cell_range
ite=[0,1,2,3,4,5,6,7,8,9]
for z in np.arange(0,20,1):
    mi.append(0)
    sum.append(0)
print(mi)
for i in np.arange(0,20): #number of cell
    print(i)
    for j in np.arange(0,50): #in one cell
         mi[i] = mi[i] + x2[50*(i)+j]

    mi[i]=mi[i]/50
    #print(mi[i])
print(mi)

for i in np.arange(0,20):
    for j in np.arange(0,50):
        sum[i] = sum[i] + ((x2[50*(i)+j]-mi[i])*(x2[50*(i)+j]-mi[i]))
    sum[i]=sum[i]/49
print(sum)
# plt.scatter(x, wall_y1)
# plt.scatter(x, wall_y2)
# plt.scatter(wall_y1, x)
# plt.scatter(wall_y2, x)
print(len(wall_y1))
print(len(mi))
plt.title("Identity Function")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()
#print(x)