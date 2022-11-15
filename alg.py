import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from matplotlib.patches import Ellipse
import math
from scipy.stats import multivariate_normal
#import numpy
def GetMuSigma(x):
    mu_x = np.mean(x)
    sigma_x = np.std(x)
    return mu_x, sigma_x*sigma_x
def gaus2d(x=0, y=0, mx=0, my=0, sx=1, sy=1):
    return 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))
def GetMuSigmaFromEqSqrt(x):
    suma=0
    for i in x:
        suma = suma + i
    mu_x=sum(x)/len(x)
    suma=0
    for i in x:
        suma = suma + (i-mu_x)*(i-mu_x)
    sigma_x=suma/len(x)
    return mu_x, math.sqrt(sigma_x)
        
def GetMuSigmaFromEq(x):
    suma=0
    for i in x:
        suma = suma + i
    mu_x=sum(x)/len(x)
    suma=0
    for i in x:
        suma = suma + (i-mu_x)*(i-mu_x)
    sigma_x=suma/len(x)
    return mu_x, sigma_x
        
def GetMuSigmaFromAngle(x):
    suma=0
    for i in x:
        suma = suma + i
    mu_x=sum(x)/len(x)
    suma=0
    for i in x:
        suma = suma + (i-mu_x)*(i-mu_x)
    sigma_x=suma/len(x)
    return mu_x, sigma_x
def ComputeAngle(xsigma,ysigma):
    return -math.degrees(math.asin(xsigma/math.sqrt(xsigma*xsigma+ysigma*ysigma)))
    
    
                            #################- MAIN -#####################    
def main():
    cell_size = 20
    img_name = 'img/sth.png'

    im = Image.open(img_name, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())

    cells_horizontal = width//cell_size
    cells_vertical = height//cell_size

    print('Dim: x=%d, y=%d, pixells:%d' % (width, height, width*height))
    print('Dim cell:x=%d Cells no. y=%d' % (cell_size, cells_horizontal*cells_vertical))

    x=[]
    y=[]
    for i in range(height*width):
        if (pixel_values[i]==0):
            x.insert(0,i%width)
            y.insert(0, height - i//height)
            
    current_x = []
    current_y = []     
    counter = 0     
    j=0
    ells=[]       
    for i in range(cells_vertical):
        for j in range(cells_horizontal):
            counter = 0  
            for k in range(cell_size):
                for l in range(cell_size):
                    if(pixel_values[(i*cell_size+k)*width + j*cell_size+l] == 0):
                        counter = counter +1
                        current_x.append((j*cell_size)+l)
                        current_y.append((height-(i*cell_size+k)))
            if(counter>5):
                ymi,ysigma = GetMuSigmaFromEqSqrt(current_y)
                if(ysigma<0.0001):
                     ysigma = 0.1
                xmi,xsigma = GetMuSigmaFromEqSqrt(current_x)
                if(xsigma<0.0001):
                     xsigma = 0.1
                
                # print("sigmax= %f sigmay= %f" %(xsigma,ysigma))
                # ang=ComputeAngle(xsigma,ysigma)
                # #ang=0
                # ells.append( Ellipse(xy=(xmi, ymi), width=2*xsigma, height=2*ysigma,angle=ang,
                #                      edgecolor='b', fc='None', lw=1))
                xz,yz = np.meshgrid(current_x,current_y)
                z=gaus2d(xz,yz,xmi,ymi,xsigma,ysigma)
                cs = plt.contourf(xz,yz,z, cmap='Blues')
            current_x.clear()
            current_y.clear()

    #fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    #for e in ells:
        #ax.add_artist(e)
        #e.set_facecolor('grey')     
    #del ells
        
    cmd = 'display ' + img_name + '&'
    os.system(cmd)  
    plt.xlim([0,width])
    plt.ylim([0,height])           
    plt.show() 
    # plt.figure(2)

    # plt.xlim([0,width])
    # plt.ylim([0,height])

    # plt.plot(x,y,'b.', linewidth=1)
    
    #plt.show()
    # #print(list2d)
    
if __name__ == "__main__":
    main()
    # import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# import os
# from matplotlib.patches import Ellipse
# import math
# from scipy.stats import multivariate_normal
# from mymath import *
# #import numpy


# def ShowOriginal(name):
#     cmd = 'display ' + name + '&'
#     os.system(cmd)  
# def main():
#     cell_size = 50
#     img_name = 'img/p1map.bmp'

#     im = Image.open(img_name, 'r')
#     width, height = im.size
#     pixel_values = list(im.getdata())

#     cells_horizontal = width//cell_size
#     cells_vertical = height//cell_size

#     print('Dim: x=%d, y=%d, pixells:%d' % (width, height, width*height))
#     print('Dim cell:x=%d Cells no. y=%d' % (cell_size, cells_horizontal*cells_vertical))

#     x=[]
#     y=[]
#     for i in range(height*width):
#         if (pixel_values[i]==0):
#             x.insert(0,i%width)
#             y.insert(0, height - i//height)
#     current_x = []
#     current_y = []     
#     counter = 0     
#     j=0
#     ells=[]    
#     ang=0   
#     for i in range(cells_vertical):
#         for j in range(cells_horizontal):
#             counter = 0  
#             for k in range(cell_size):
#                 for l in range(cell_size):
#                     if(pixel_values[(i*cell_size+k)*width + j*cell_size+l] == 0):
#                         counter = counter +1
#                         current_x.append((j*cell_size)+l)
#                         current_y.append((height-(i*cell_size+k)))
#             if(counter>3):
#                 ymi,ysigma = GetMuSigmaFromEqSqrt(current_y)
#                 if(ysigma<0.0001):
#                      ysigma = 0.1
#                 xmi,xsigma = GetMuSigmaFromEqSqrt(current_x)
#                 if(xsigma<0.0001):
#                      xsigma = 0.1

#                 #ang=GetBeginEnd(current_x,current_y)
#                 ang=RegLinp(current_x,current_y,xmi,ymi)
#                 ells.append( Ellipse(xy=(xmi, ymi), width=2*xsigma, height=2*ysigma,angle=ang,
#                                      edgecolor='b', fc='None', lw=1))
                
#             current_x.clear()
#             current_y.clear()

#     fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
#     for e in ells:
#         ax.add_artist(e)
#         e.set_facecolor('grey')     
#     del ells

#     plt.xlim([0,width])
#     plt.ylim([0,height])           
#     # ShowOriginal(img_name)
#     plt.show() 

    
# if __name__ == "__main__":
#     main()