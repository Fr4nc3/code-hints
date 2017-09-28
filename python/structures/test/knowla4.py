import tkinter
from tkinter import ttk
from tkinter import *

fragment_file = open('frags.txt')
more_fragments = True


def get_next_fragment():
    '''
    Invariant:  more_fragments = True/False according to "there is at least one line in frags.txt"
    Precondition: If more_fragments is True, each line of frags.txt consists of a (text) fragment
        ending in a non-blank character
    Postcondition: old(more_fragments) = False AND return = "NO MORE FRAGMENTS"
    -OR- old(more_fragments) = True AND return = the unread line (without newline)
    '''
    global more_fragments

    # First part of Postcondition
    if not more_fragments:
        return "NO MORE FRAGMENTS"

    # Second part of postcondition (more_fragments)
    new_fragment = fragment_file.readline()
    if new_fragment[-1:] == '\n':  # not last line
        return new_fragment[:-1]  # omit newline
    else:  # last line
        more_fragments = False  # for invariant
        return new_fragment  # (no newline present)


# content_frame and inner_frame (4x4 grid, 400(w)x 100 pixels) placed in grid
root = tkinter.Tk()  # reference to the GUI toolkit
content_frame = ttk.Frame(root)  # overall Frame
inner_frame = ttk.Frame(content_frame, borderwidth=5, width=400, height=100)  # within content_frame
content_frame.grid(column=0, row=0)  # for inner widget that expands as needed; placed at (0, 0)
inner_frame.grid(column=0, row=0, columnspan=4, rowspan=4)  # may span 4 columns and rows

# displayed_text appears in 4 columns starting 0,0; consists of committed_text + proposed_fragment
committed_text = ''
proposed_fragment = get_next_fragment()
new_display = committed_text + ' ' + proposed_fragment
displayed_text = tkinter.Message(content_frame, text=new_display, relief=RAISED, width=350, font=12)
displayed_text.grid(column=0, row=0, columnspan=4)


# Accept Button, with action incorporate_proposed_fragment(), at bottom right

def incorporate_proposed_fragment():
    # committed_text includes proposed_fragment
    global committed_text, proposed_fragment  # accessing variables outside this method; see [2]
    committed_text += ' ' + proposed_fragment
    # proposed_fragment is the fragment following old(proposed_fragment) in frags.txt
    proposed_fragment = get_next_fragment()
    displayed_text.configure(text=committed_text + ' ' + proposed_fragment)


accept_button = tkinter.Button(root, text="ACCEPT", command=incorporate_proposed_fragment)
accept_button.grid(column=2, row=2)


# Reject Button, with action replace_proposed_fragment(), at right of Accept button

def replace_proposed_fragment():
    proposed_fragment = get_next_fragment()
    displayed_text.configure(text=committed_text + ' ' + proposed_fragment)


reject_button = tkinter.Button(root, text="REJECT", command=replace_proposed_fragment)
reject_button.grid(column=3, row=2)

root.mainloop()  # initiate the UI
