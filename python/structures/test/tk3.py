import tkinter
from tkinter import ttk
from tkinter import messagebox


# adapted from http://stackoverflow.com/questions/17757451/simple-ttk-combobox-demo

class ComboBoxDemo:
    def __init__(self, parent):
        self.parent = parent
        self.box = ttk.Combobox()
        self.display_combo()  # work delegated

    def display_combo(self):
        # A Combobox with values 'First value', 'Second value', 'Third value' is on the console        # Combobox inherits from Sequence--on which indexing is allowed
        self.box['values'] = ('First value', 'Second value', 'Third value')
        self.box.grid(column=0, row=0)  # position of display *
        self.box.current(0)  # index of value showing (as default) in the single line window

        def echo_to_console(an_event):
            print(self.box.get())
            messagebox.showinfo(message=self.box.get())

        self.box.bind('<<ComboboxSelected>>', echo_to_console)


if __name__ == '__main__':
    root = tkinter.Tk()
    app = ComboBoxDemo(root)
    root.mainloop()
