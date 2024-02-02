#!/usr/bin/python3
class Base():
    """This class is the base of all classes in the project.
    It contains the id attribute and the __str__ method."""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects