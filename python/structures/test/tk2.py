from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def create_checkbox(a_border_width=5, a_height=350):
    '''
    Postcondition 1 (Check Boxes Defined): student/auditor, and admin _box are check boxes
    Postcondition 7 (Check Boxes in Position): The text field is top right in the Window, the check boxes are vertically
    at the left, ok_button and reconfigure_button and cancel_button are at lower left, student_type_listbox at bottom
    center-right, and slider at bottom right AND the UI is showing
    '''

    # Postcondition 1 (Frame Defined)
    root = Tk()
    the_content = ttk.Frame(root)
    the_frame = ttk.Frame(the_content, borderwidth=a_border_width, relief="sunken", width=200, height=a_height)

    # Postcondition 2 (Check Boxes Defined)

    # student/auditor/admin_bool are BooleanVars initialized False
    student_bool = BooleanVar()
    auditor_bool = BooleanVar()
    admin_bool = BooleanVar()

    student_bool.set(False)
    auditor_bool.set(False)
    admin_bool.set(False)

    student_box = ttk.Checkbutton(the_content, text="Student", variable=student_bool)
    auditor_box = ttk.Checkbutton(the_content, text="Auditor", variable=auditor_bool)
    admin_box = ttk.Checkbutton(the_content, text="Admin", variable=admin_bool)

    label1 = ttk.Label(the_content, text="hello")

    # Postcondition 3 (Button Defined)
    # ok_button
    def simulated_entered(a_student_value):
        print("\n===> Data entered:.... Student?: " + str(student_bool.get()))
        messagebox.showinfo(message='alert')
        exit(0)

    ok_button = ttk.Button(the_content, text="OK", command=lambda: simulated_entered(student_bool.get()))

    # Postcondition 4 (Widgets in Position)

    the_content.grid(column=0, row=0)
    the_frame.grid(column=0, row=0, columnspan=3, rowspan=3)
    student_box.grid(column=0, row=0)
    auditor_box.grid(column=0, row=1)
    label1.grid(column=3, row=2)
    admin_box.grid(column=0, row=2)
    ok_button.grid(column=3, row=3)

    root.mainloop()


create_checkbox()
