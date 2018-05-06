from tkinter import *
from tkinter.ttk import *

class Calc_Window(Frame) :

    def __init__(self, master = None):
        super().__init__(master)
        self.setup_interface()

    def evaluate_and_show(self, event) :
        val = str(eval(event.widget.get()))
        self.result.set('Result : ' + val)

    def setup_interface(self) :
        self.master.minsize(width = 400, height = 200)
        self.pack(fill = BOTH, expand = True)

        instr = Label(self,
                text = "Type your expression and hit enter to evaluate",
                wraplength = self.master['width'])

        instr.pack(side = 'top', expand = True)

        field = Entry(self)
        field.bind('<Return>', self.evaluate_and_show)
        field.pack(side = 'top', expand = True)

        self.result = StringVar()
        res_label = Label(self, textvariable = self.result)
        res_label.pack(side = 'top', expand = True)

if __name__ ==  '__main__' :
    root = Tk()
    app = Calc_Window(root)
    app.mainloop()
