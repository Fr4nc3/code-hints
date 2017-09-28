"""
Fr4nc3
09/26/2016
This program implement  Pet Dog Cat BigDog SmallDog,HouseCat, StrayCat
"""

import random

"""
Implement Classes here
"""


class Pet:
    """
    Pet main class defined attribute description
    """

    def __init__(self, description="pet object"):
        self.description = description

    def speak(self):
        """
        speak empty method
        """
        pass


class Dog(Pet):
    """
     Children class of Pet
     set description value to pet.__init__
    """

    def __init__(self, description="dog object"):
        super().__init__(description)

    def sit(self):
        print("The dog sits")


class Cat(Pet):
    """
     Children class of Pet
     set description value to pet.__init__
    """

    def __init__(self, description="cat object"):
        super().__init__(description)

    def speak(self):
        print("Meow")


class BigDog(Dog):
    """
     Children class of Dog
     set description value to Dog.__init__
    """

    def __init__(self, description="large, muscular dog"):
        super().__init__(description)

    def speak(self):
        print("Woof")


class SmallDog(Dog):
    """
     Children class of Dog
     set description value to Dog.__init__
    """

    def __init__(self, description="A tiny, cute dog"):
        super().__init__(description)

    def speak(self):
        print("Yip")


class HouseCat(Cat):
    """
     Children class of Cat
     set description value to Cat.__init__
    """

    def __init__(self, description="A cat with fluffy, white fur"):
        super().__init__(description)

    def purr(self):
        print("Purrrr")


class StrayCat(Cat):
    """
     Children class of Cat
     set description value to Cat.__init__
    """

    def __init__(self, description="A cat with tousled, striped fur"):
        super().__init__(description)


def isvalid(test):
    return None if not test.isdigit() else int(test)  #


"""
Test the classes here
"""
# Shadowing testing
# Pet.description = "Pet overridden"
# Dog.description = "dog"
# SmallDog.description = "petit chien"
# print(Pet.description)
# print(Dog.description)
# print(SmallDog.description)
# #Pet.speak()  # this fails
# pet1 = BigDog("Big dog Test")
# print(pet1.description)


# This line treats class definitions as objects. Isn't that cool?
petClasses = [BigDog, SmallDog, HouseCat, StrayCat]
# ask the user to input how many pets to generate
question = "How many pets to generate: "
numberOfPets = isvalid(input(question))

while numberOfPets is None:  # to avoid any non numeric
    numberOfPets = isvalid(input(question))

for petCount in range(0, numberOfPets):
    # This line creates new objects from the stored class definitions!
    pet = petClasses[random.randrange(4)]()
    print("Pet number {}".format(petCount))
    print(pet.description)
    pet.speak()
    if isinstance(pet, Dog):
        pet.sit()
    elif isinstance(pet, HouseCat):  # this can be if only
        pet.purr()
