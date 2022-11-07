
import numpy as np
import matplotlib.pyplot as plt
from ctypes import sizeof
from heapq import heappush
from PIL import Image
import os

cell_size = 50
img_name = 'img/sth.bmp'
im = Image.open(img_name, 'r')
width, height = im.size
#list2d=[[0 for i in range(width)] for j in range(height)]
list2d = [[0]*width]*height
print(len(list2d)*len(list2d[0]))
print(list2d[10][10])
pixel_values = list(im.getdata())

cells_horizontal = width//cell_size
cells_vertical = height//cell_size
#print(pixel_values)

print(width)
print(height)
print(pixel_values[500*83+114])
print(len(pixel_values))
for i in range(width*height):
    list2d[i%500][i//500] = pixel_values[i]
    #print('[%d][%d]'%(i//500,i%500))
#print(pixel_values)


x=[]
y=[]


for i in range(height*width):
    if (pixel_values[i]==0):
        x.insert(0,i%width)
        y.insert(0, height - i//height)
        
        
cnt = 0              
for i in range(cells_vertical):
    for j in range(cells_horizontal):
        x=2*2        
        
        
        
        
        
        
        
        
print(x)
print(len(x))
plt.xlim([0,width])
plt.ylim([0,height])
cmd = 'display ' + img_name + '&'
os.system(cmd)
plt.figure(1)
plt.plot(x,y,'b.', linewidth=1)
plt.figure(2)

plt.show()
#print(list2d)
        
        
        