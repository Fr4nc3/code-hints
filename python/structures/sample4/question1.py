"""

09/30/2016


"""


# DEFINITIONS


class PoundException(Exception):
    def __init__(self):
        # print("Exception raised because '#' found.") # we can print here but
        # here I don't print because the example in the Description print only once
        pass


def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if "#" in name_input:
        raise PoundException


try:
    get_name()
except Exception:  # this is generic exception but also can be PoundException
    print("Exception raised because '#' found.")

# unrelated test
# try:
#     1 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")
