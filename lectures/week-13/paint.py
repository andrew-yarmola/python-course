from tkinter import *
from tkinter.ttk import *

class Paint_Window(Frame) :

    def __init__(self, master = None):
        super().__init__(master)
        self.setup_interface()

    def paint(self, event) :
       x1, y1 = ( event.x - 1.5 ), ( event.y - 1.5 )
       x2, y2 = ( event.x + 1.5 ), ( event.y + 1.5 )
       event.widget.create_oval( x1, y1, x2, y2, fill = 'green' )

    def setup_interface(self) :
        self.master.minsize(width = 400, height = 200)
        self.pack(fill = BOTH, expand = True)

        instr = Label(self,
                text = "Draw on the canvas using your mouse",
                wraplength = self.master['width'])

        instr.pack(side = 'top', expand = True)

        canvas = Canvas(self)
        canvas.pack(fill = BOTH, expand = True)
        canvas.bind('<B1-Motion>', self.paint)

if __name__ ==  '__main__' :
    root = Tk()
    app = Paint_Window(root)
    app.mainloop()
