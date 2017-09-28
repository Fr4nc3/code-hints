"""
Fr4nc3
This program implement  Parent class and nested classes ChildA ChildB
"""


class Parent:
    def __init__(self):
        self.greeting = "Hi, I'm a parent object"


class ChildA(Parent):
    def __init__(self):
        self.greeting = "Hi, I'm a child object."


class ChildB(Parent):
        pass


parent = Parent()
child_a = ChildA()
child_b = ChildB()

print(parent.greeting)
print(child_a.greeting)
print(child_b.greeting)

print(type(parent))
print(type(child_a))
print(type(child_b))
