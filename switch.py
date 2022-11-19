import matplotlib
from alg_ell import *
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
from tkinter import *
import sys
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler


def ShowOriginal(img_name):
    cmd = 'display ' + img_name + '&'
    os.system(cmd) 

# Seperated out config of plot to just do it once
def config_plot():
    fig, ax = plt.subplots()
    ax.set(xlabel='x', ylabel='y',
           title='Graph One')
    return (fig, ax)

class matplotlibSwitchGraphs:
    def __init__(self, master, elrl, el2p,w,h):
        self.master = master
        self.frame = Frame(self.master)
        self.fig, self.ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        self.graphIndex = 0
        self.canvas = FigureCanvasTkAgg(self.fig, self.master)  
        self.ellsRL = elrl  
        self.ells2P = el2p
        self.we = w
        self.he = h
        self.config_window()
        self.draw_graph_one()
        self.frame.pack(expand=NO, fill=BOTH)


    def config_window(self):
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.button = Button(self.master, text="Quit", command=self._quit)
        self.button.pack(side=BOTTOM,expand=0, fill=X)
        self.button_switch = Button(self.master, text="Switch Graphs", command=self.switch_graphs)
        self.button_switch.pack(side=BOTTOM,expand=0, fill=X)


    def draw_graph_one(self):     
        self.ax.clear()  
        
        for e in self.ellsRL:
                self.ax.add_artist(e)
                e.set_facecolor('gray')  
        self.ax.set(title='Ellipse with line regression (LSE)')
        plt.xlim([0,self.we])
        plt.ylim([0,self.he])  
        self.canvas.draw()

    def draw_graph_two(self):    
        self.ax.clear() 
        for e in self.ells2P:
                self.ax.add_artist(e)
                e.set_facecolor('gray')    
        self.ax.set(title='Ellipse based on 2 points')
        plt.xlim([0,self.we])
        plt.ylim([0,self.he]) 
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

    ells2P=[]
    ellsRL=[]
    print(sys.argv)
    if len(sys.argv)==3:
        ells2P,ellsRL,w,h=GetListsOfEllipses((int(sys.argv[1])), 'img/'+sys.argv[2])
        ShowOriginal('img/'+sys.argv[2])
    else:
        ells2P,ellsRL,w,h=GetListsOfEllipses(25, 'img/img3.bmp')
        ShowOriginal('img/img3.bmp')
    root = Tk()
    matplotlibSwitchGraphs(root,ellsRL,ells2P,w,h)
    root.mainloop()
    ells2P.clear()
    ellsRL.clear()
    #pixel_values.clear() 
    #pixel_values.clear() 
if __name__ == '__main__':
    main()