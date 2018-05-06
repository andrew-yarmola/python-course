from tkinter import *
from tkinter.ttk import *
import numpy as np

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

class Plot_Window(Frame) :

    def __init__(self, master = None):
        super().__init__(master)
        self.initialize()
        self.setup_interface()

    def initialize(self) :
        self.data = np.random.randn(100)

    def setup_interface(self) :
        self.master.minsize(width = 400, height = 200)
        self.pack(fill = BOTH, expand = True)

        self.fig = plt.figure()
        plt.plot(self.data)

        self.plt_canvas = FigureCanvasTkAgg(self.fig, master = self)
        self.plt_canvas.get_tk_widget().pack(fill = BOTH, expand = True)

        self.toolbar = NavigationToolbar2TkAgg(self.plt_canvas, self )
        self.toolbar.pack(side = 'bottom', expand = True)
        self.toolbar.update()

if __name__ ==  '__main__' :
    root = Tk()
    app = Plot_Window(root)
    app.mainloop()
