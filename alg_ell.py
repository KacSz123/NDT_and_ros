import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from scipy.stats import multivariate_normal


from mymath import *
def GetListsOfEllipses(cell_s, img_name):
    cell_size = cell_s
    #img_name = 'img/123.bmp'

    im = PIL.Image.open(img_name, 'r')
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
    ellsRL=[]  
    ells2P=[]
    ellsOrin=[]    
    for i in range(cells_vertical):
        for j in range(cells_horizontal):
            counter = 0  
            for k in range(cell_size):
                for l in range(cell_size):
                    if(pixel_values[(i*cell_size+k)*width + j*cell_size+l] == 0):
                        counter = counter +1
                        current_x.append((j*cell_size)+l)
                        current_y.append((height-(i*cell_size+k)))
            if(counter>3):
                ymi,ysigma = GetMuSigmaFromEqSqrt(current_y)
                if(ysigma<0.0001):
                     ysigma = 0.1
                xmi,xsigma = GetMuSigmaFromEqSqrt(current_x)
                if(xsigma<0.0001):
                     xsigma = 0.1

                ang2P=GetBeginEnd(current_x,current_y)
                angRL=RegLinp(current_x,current_y,xmi,ymi)
                ellsRL.append( Ellipse(xy=(xmi, ymi), width=2*xsigma, height=2*ysigma,angle=angRL,
                                     edgecolor='b', fc='None', lw=1))
                ells2P.append( Ellipse(xy=(xmi, ymi), width=2*xsigma, height=2*ysigma,angle=ang2P,
                                     edgecolor='b', fc='None', lw=1))
                
            current_x.clear()
            current_y.clear()
    return ells2P, ellsRL
