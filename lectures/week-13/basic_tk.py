from tkinter import *
# ttk is a slightly more modern look
# calling like this overrides older
# tkinter code
from tkinter.ttk import *
from PIL import ImageTk

import getopt

class Basic_App_Window(Frame) :

    def __init__(self, master = None):
        super().__init__(master)
        self.initialize()
        self.setup_interface()

    def initialize(self) :
        try:
            opts, args = getopt.getopt(sys.argv[1:],'a:',['action_text='])
        except getopt.GetoptError as err:
            print("Usage : python basic_tk.py [-a, --action_text] <text>.")
            self.master.quit()

        self.action_text = "Hello Everyone!"
        self.display_text = StringVar()

        for opt, val in opts:
            if opt in ('-a', '--action_text'):
                self.action_text = val

    def setup_interface(self) :
        # self.master is set in super().__init__(master)
        self.master.minsize(width = 400, height = 200)
        self.pack(fill = BOTH, expand = True)

        button = Button(self, text = "Push Me")
        button['command'] = self.toggle_text
        button.pack(anchor = NW)

        quit_button = Button(self, text = 'Quit',
                        command = self.master.quit)
        quit_button.pack(side = 'bottom')

        action_label = Label(self, textvariable = self.display_text)
        action_label.pack(side = 'top')

        self.canvas = Canvas(self)
        self.canvas.pack(side = 'top', fill = BOTH, expand = True)

        # let's draw something
        self.canvas.create_oval(100,100,140,140)
        self.canvas.create_line(0,0,100,400)
        self.canvas.create_polygon(40,30,150,50,20,120)
        self.canvas.create_arc(160,50,240,140,
                                start = 0, extent = 150,
                                fill = 'blue')
        self.image = ImageTk.PhotoImage(file = 'MandelbrotM_Colors.png')
        self.canvas.create_image(0, 0, anchor = NW, image = self.image)

    def toggle_text(self) :
        if self.display_text.get() == '' :
            self.display_text.set(self.action_text)
        else :
            self.display_text.set('')

if __name__ ==  '__main__' :
    root = Tk()
    app = Basic_App_Window(root)
    app.mainloop()
