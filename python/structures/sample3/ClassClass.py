'''
Name: class_class.py
template class
'''


class Parent(object):
    '''I am a parent class. Not very exciting but useful to show 
    basic inheritence
    '''

    def __init__(self, Mother='Anne', Father='Andy', Value=5):
        '''Setting the default values when the class is instantiated'''
        self.greeting = ("P: My starting parents are {0} and {1}.".
                         format(Mother, Father))
        self.Mother = Mother
        self.Father = Father
        self.Value = Value

    def __repr__(self):
        return 'P repr: Value = {0}'.format(self.Value)

    def __str__(self):
        # __str__ makes string versions of the object.  
        # if __str___ is not defined, this object will act like __str__=__repr__
        return 'P str: Mother={mom}, Father={dad}, Value={Value}'.format(
            mom=self.Mother,
            dad=self.Father,
            Value=self.Value)

    def mother(self):
        if hasattr(self, 'Mother') and self.Mother is not None:
            return "P: My mother is {0}.".format(self.Mother)
        else:
            return "P: Are you my mother?"

    def Greeting(self):
        return ("P: My starting parents are {0} and {1}.".
                format(self.Mother, self.Father))


class ChildA(Parent):
    def __init__(self, Mother=None, Father=None, Value=3):
        '''Setting the default values when the class is instantiated'''
        super().__init__()  # this will get self.greeting & self.value from Parent
        self.greeting = "Hi, I'm a child object."  # Parent's self.greeting will be overridden
        self.Mother = Mother  # Parent's self.Mother will be overridden
        if not hasattr(self, 'Father') or self.Father is None:
            self.Father = Father
        self.Value = self.Value + Value

    def __str__(self):
        return 'str = {}'.format(self.greeting)

    def mother(self):
        if hasattr(self, 'Mother') and self.Mother is not None:
            return "C: My mother is {0}.".format(self.Mother)
        else:
            return "C: Are you my mother?"


class ChildB(Parent):
    pass


# Tests
if __name__ == '__main__':
    print('Here is the parent greeting string')
    parent = Parent(Mother='Jill', Father='Jack')
    print('> P1: {}'.format(parent.greeting))

    print('Here are 3 ways to print the value of __str__')
    print('> P2a: {}'.format(parent))
    print('> P2b: {}'.format(parent.__str__))
    print('> P2c: {}'.format(str(parent)))

    print('Here are 2 ways to print the value of __repr__')
    print('> P3a: {}'.format(parent.__repr__))
    print('> P3b: {}'.format(repr(parent)))

    print("Here is the doc string, even though a method wasn't defined "
          "in the class")
    print('> P4: {}'.format(parent.__doc__.strip()))
    print('-' * 50)

    # ###############################
    childA = ChildA('Linda')
    childB = ChildB()

    print('Here we get the greeting defined in the child class.')
    print('> Child A: {}'.format(childA.greeting))
    print("Notice what happens when the greeting isn't defined in the child class. "
          'It inherits the greeting method from the parent class.')
    print('> Child B1: {}'.format(childB.Greeting()))
    childB.Mother = 'Maryanne'
    print('Now we will definte a new Mother in the child ({}).'.format(
        childB.Mother))

    print('Notice that the greeting string is not changed when the Mother is redefined')
    print('> Child B2: {}'.format(childB.greeting))
    print('However, the Greeting() method is dynamic and will change')
    print('> Child B3: {}'.format(childB.Greeting()))
    print('-' * 50)

    # ###############################
    print("Now let's use super() to override the child's method.")
    print('Notice that both the parent and child method use the Mother defined '
          'in the child instance')
    print('First we ask the child class method for its mother')
    print('> Child A1: {}'.format(childA.mother()))
    print('Now we use suoer() to ask its parent class method for its mother')
    print('> Child A2: {}'.format(super(ChildA, childA).mother()))
    childA.Mother = 'Anne'
    print('Now we will definte a new Mother in the child ({}).'.format(
        childA.Mother))
    print('Again we will first we ask the child class method for its mother')
    print('> Child A3: {}'.format(childA.mother()))
    print('And then use suoer() to ask its parent class method for its mother')
    print('> Child A4: {}'.format(super(ChildA, childA).mother()))
