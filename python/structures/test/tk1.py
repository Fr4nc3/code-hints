
# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
#
# content = ttk.Frame(root)
# frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)
#
# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()
# onevar.set(True)
# twovar.set(False)
# threevar.set(True)
#
# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")
#
# content.grid(column=0, row=0)
# frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)
#
# root.mainloop()
#
#
# root=Tk()
# c=Canvas(root)
# c.pack()
# xy=20, 20, 300, 180 #create an arc enclosed by the given rectangle
# c.create_arc(xy, start=0, extent=270, fill="red", outline="yellow")
# c.create_text(100, 100, text="75%")
# c.create_arc(xy, start=270, extent=60, fill="blue", outline="yellow")
# c.create_text(180, 140, text="16.5%")
# c.create_arc(xy, start=330, extent=30, fill="green", outline="yellow")
# c.create_text(280, 120, text="8.5%")
# root.mainloop()
#
#
# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
#
# content = ttk.Frame(root, padding=(3,3,12,12))
# frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name = ttk.Entry(content)
#
# onevar = BooleanVar()
# twovar = BooleanVar()
# threevar = BooleanVar()
#
# onevar.set(True)
# twovar.set(False)
# threevar.set(True)
#
# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")
#
# content.grid(column=0, row=0, sticky=(N, S, E, W))
# frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)
#
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# content.columnconfigure(0, weight=3)
# content.columnconfigure(1, weight=3)
# content.columnconfigure(2, weight=3)
# content.columnconfigure(3, weight=1)
# content.columnconfigure(4, weight=1)
# content.rowconfigure(1, weight=1)
#
# root.mainloop()
#

from tkinter import *

class FirstGUIDemo(Frame):  # Python: inherits from Frame

    def __init__(self, master=None):  #Python: master is parameter for inherited (i.e., Frame's) constructor
        Frame.__init__(self, master)  #Python: parent's constructor; "master" is GUI framework to be used
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.HELLO_BUTTON = Button(self, text="Hello", command=self.greet)
        self.HELLO_BUTTON.pack(side="left")

        self.QUIT_BUTTON = Button(self, text="QUIT", fg="red", bg="blue1", command=self.quit)
        self.QUIT_BUTTON.pack({"side": "right"})

    def greet(self):  # Simple console displayed_text
        print('\n------The application has been requested to say "hello."------')

    def quit(self):
        super().quit()

tk = Tk()  # Ed: a Tk object
app = FirstGUIDemo(master=tk)  # Ed: Frame object bound to the Tk object
app.mainloop()  # Ed: for displaying widgets until termination
tk.destroy()  #Ed: space reclaimed