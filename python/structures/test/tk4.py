from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# partly adapted from http://www.tkdocs.com/tutorial/grid.html

def create_ui(a_border_width=5, a_height=150, a_label=""):
    '''
    Postcondition 1 (Frame Defined): the_frame is a UI Frame with border width a_border_width,
    border width a_border_width, sunken relief, width 200, and height a_height
    Postcondition 2 (Listbox Defined): listbox_example consists of "OPTION 1", "OPTION 2",
    "OPTION 3", and "OPTION 4" with single element selection
    Postcondition 3 (Button Defined): Pressing button ok_button shows on the monitor data entered, and closes the app
    Postcondition 4 (Widgets in Position): The button is at lower left, and listbox_example at bottom
    center-right AND the UI is showing
    '''

    # Postcondition 1 (Frame Defined)
    root = Tk()
    the_content = ttk.Frame(root)

    # Postcondition 2 (Listbox Defined):
    listbox_example = Listbox(selectmode=SINGLE)
    title_options = ["OPTION 1", "OPTION 2", "OPTION 3", "OPTION 4", "OP5"]
    for item in title_options:
        listbox_example.insert(END, item)

    # Postcondition 3 (Button Defined)
    # ok_button
    def ok_entered():
        new_title = title_options[listbox_example.curselection()[0]]
        messagebox.showinfo(title="selecyrf", message="{0} {1}".format(new_title, listbox_example.curselection()[0]))
        print("\n===> Data entered:...." + new_title)
        exit(0)

    ok_button = ttk.Button (the_content, text="OK", command=lambda: ok_entered())

    # Postcondition 3 (Widgets in Position)
    the_content.grid(column=0, row=0)
    ok_button.grid(column=3, row=3)
    listbox_example.grid(column=0, row=5)
    root.mainloop()


create_ui()
