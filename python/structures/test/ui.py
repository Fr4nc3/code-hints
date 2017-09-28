# As seen by the test-taker

import tkinter
from tkinter import ttk
from tkinter import *



import sqlite3
import random
'''
Post: Database fragment.db contains the fragments of source.txt as per locations of "@"
'''

### fragment.db is a database with cursor cursor_frags

fragment_db = sqlite3.connect('fragment.db')
cursor_frags = fragment_db.cursor()

### Table fragment_table exists in fragment.db with int/text fields named "id" /"fragment"

try:
    cursor_frags.execute('CREATE TABLE fragment_table (id int, fragment text)')
except Exception:
    print("(already open)")

### source_as_tuple consists of the source.txt fragments delimited by "@" in a random order

fileR = open('source.txt')
source_text = fileR.read()
source_as_tuple = source_text.split('@')
random.shuffle(source_as_tuple)

### fragment_table consists of source_as_tuple, consecutively numbered by field "id"

for fragment_index in range(0, source_as_tuple.__len__()):
    tuple = source_as_tuple[fragment_index]
    insert = "INSERT INTO fragment_table VALUES (" + \
             str(fragment_index + 1) + ", '" + tuple + "')"
    cursor_frags.execute(insert)
fragment_db.commit()  # changes committed

### cursor_to_records consists of the records of fragment_table

conn = sqlite3.connect('fragment.db')
cursor_to_records = conn.cursor()
cursor_to_records.execute('SELECT * FROM fragment_table WHERE id>0')
fragment_db.close()


def get_next_fragment():  # ---------------------------------------------------
    # record of cursor_to_records returned that follows the last one returned
    next = cursor_to_records.fetchone()
    return next  # ------------------------------------------------------------

''' Postconditions:
1.	The user has committed to committed_text as the source material (in proper order)
2.	proposed_fragment is proposed to the user as the next fragment
3.	done_indication appears* when all proposals have been exhausted
* i.e., instead of a proposed new fragment
'''
committed_text = ''
proposed_fragment = ''
done_indication = ' DONE!'


def create_ui():
    # Post: UI appears, showing committed text proposed next fragment in context, accept and reject buttons

     # GUI framework (root, content_frame, inner_frame) defined, inner_frame 4x4 grid, 400(w)x 100 pixels
    root = tkinter.Tk()  # reference to the GUI toolkit
    content_frame = ttk.Frame(root)  # overall Frame
    # within content_frame:
    inner_frame = ttk.Frame(content_frame, borderwidth=5, width=400, height=100)  
    content_frame.grid(column=0, row=0)  # for inner widget that expands as needed; placed at (0, 0)
    inner_frame.grid(column=0, row=0, columnspan=4, rowspan=4)  # may span 4 columns and rows

    # displayed_text appears in 4 columns starting at row 0, column 0
    # displayed_text shows committed_text followed by proposed_fragment
    global committed_text, proposed_fragment
    committed_text = ''
    proposed_fragment = str(get_next_fragment()[1])
    new_display = committed_text + ' ' + proposed_fragment
    displayed_text = tkinter.Message\
            (content_frame, text=new_display, relief=RAISED, width=350, font=12)
    displayed_text.grid(column=0, row=0, columnspan=4)

    # For use by ACCEPT button:
    def incorporate_proposed_fragment():    
        # Post1: committed_text includes proposed_fragment
        # Post2: proposed_fragment is the fragment following old(proposed_fragment) in source.txt

        # Post1:
        global committed_text, proposed_fragment  # altering variable outside this method; see [2]
        committed_text += ' ' + proposed_fragment

        # Post2:
        next_fragment = get_next_fragment()
        if next_fragment is not None:
            proposed_fragment = str(next_fragment[1])
        else:
            proposed_fragment = done_indication
        # "Message in Place" restored
        displayed_text.configure(text=committed_text + ' ' + proposed_fragment)  

    # ACCEPT button at lower right performs incorporate_proposed_fragment on click
    accept_button = tkinter.Button(root, text="ACCEPT", command=incorporate_proposed_fragment)
    accept_button.grid(column=2, row=2)

    # For use by REJECT button
    def replace_proposed_fragment():    
        next_fragment = get_next_fragment()
        global done_indication
        if (next_fragment is not None) & (next_fragment is not done_indication):
            proposed_fragment = str(next_fragment[1])
        else:
            proposed_fragment = ''
        # "Message in Place" restored
        displayed_text.configure(text=committed_text + ' ' + proposed_fragment) 


    # REJECT Button is right of ACCEPT button, performs replace_proposed_fragment on click
    reject_button = tkinter.Button(root, text="REJECT", command=replace_proposed_fragment)
    reject_button.grid(column=3, row=2)

    root.mainloop()  # initiate the UI



create_ui()