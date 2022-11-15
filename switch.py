import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from scipy.stats import multivariate_normal


from mymath import *
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

# Seperated out config of plot to just do it once
def config_plot():
    fig, ax = plt.subplots()
    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='Graph One')
    return (fig, ax)

class matplotlibSwitchGraphs:
    def __init__(self, master, elrl, el2p):
        self.master = master
        self.frame = Frame(self.master)
        self.fig, self.ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        self.graphIndex = 0
        self.canvas = FigureCanvasTkAgg(self.fig, self.master)  
        self.ellsRL = elrl  
        self.ells2P = el2p
        self.config_window()
        self.draw_graph_one()
        self.frame.pack(expand=YES, fill=BOTH)


    def config_window(self):
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.button = Button(self.master, text="Quit", command=self._quit)
        self.button.pack(side=BOTTOM)
        self.button_switch = Button(self.master, text="Switch Graphs", command=self.switch_graphs)
        self.button_switch.pack(side=BOTTOM)


    def draw_graph_one(self):     
        self.ax.clear()  
        
        for e in self.ellsRL:
                self.ax.add_artist(e)
                e.set_facecolor('gray')  
        self.ax.set(title='Ellipse with reglinp (LSE)')
        plt.xlim([0,1000])
        plt.ylim([0,1000])  
        self.canvas.draw()

    def draw_graph_two(self):    
        self.ax.clear() 
        for e in self.ells2P:
                self.ax.add_artist(e)
                e.set_facecolor('blue')    
        self.ax.set(title='Ellipse based on 2 points')
        plt.xlim([0,1000])
        plt.ylim([0,1000])  
        self.canvas.draw()

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        #key_press_handler(event, self.canvas, toolbar)

    def _quit(self):
        self.master.quit()  # stops mainloop

    def switch_graphs(self):
        # Need to call the correct draw, whether we're on graph one or two
        self.graphIndex = (self.graphIndex + 1 ) % 2
        if self.graphIndex == 0:
            self.draw_graph_one()
        else:
            self.draw_graph_two()
        


def main():
    cell_size = 50
    img_name = 'img/123.bmp'

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

    root = Tk()
    matplotlibSwitchGraphs(root,ellsRL,ells2P)
    root.mainloop()
    ells2P.clear()
    ellsRL.clear()
    pixel_values.clear()
if __name__ == '__main__':
    main()