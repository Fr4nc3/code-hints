
from tkinter import *

# Simple example of a Menu

class MenuExample(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):

        # Post1 (Frame has Menu Bar): This Frame with menu bar menu_bar is on console

        # Post2 (2 Menus): menu_bar has two identical drop-down menus

        # Post 3 (3 Choices): Each menu's label/actions are "Some Category" / print echo,
        # "Another Category" / print echo, and "Exit" / exit app

        self.parent.title("Simple menu")  # Frame title

        # Post1 (Frame has Menu Bar)
        menu_bar = Menu(self.parent)
        self.parent.config(menu=menu_bar)

        # Post2 (2 Menus)
        demo_menu = Menu(menu_bar)  # menu that will be added to drop-down
        menu_bar.add_cascade(label="My First Drop-Down Menu", menu=demo_menu)
        menu_bar.add_cascade(label="My Second (Identical) Drop-Down Menu", menu=demo_menu)

        # Post 3 (3 Choices)

        def print_to_console_some():
            print("Some Category clicked")
        demo_menu.add_command(label="Some Category", command=print_to_console_some)

        def print_to_console_another():
            print("Another Category clicked")
        demo_menu.add_command(label="Another Category", command=print_to_console_another)

        def onExit():
            self.quit()
        demo_menu.add_command(label="Exit", command=onExit)


def main_function():
    root = Tk()
    root.geometry("450x250+600+400")  # sets size for window + positions it on screen
    # width, height of window, x screen coordinate, y coordinate
    app = MenuExample(root) 
    app.mainloop()


if __name__ == '__main__':
    main_function()