#!/usr/bin/python3
"""class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        """Returning private attribute 'width'"""
        return self.__width
    @property
    def height(self):
        """Returning private attribute 'height'"""
        return self.__height
    @property
    def x(self):
        """Returning private attribute 'x'"""
        return self.__x
    @property
    def y(self):
        """Returning private attribute 'y'"""
        return self.__y

#Update the class Rectangle by adding validation of all setter
    @width.setter
    def width(self, value):
        """Setting private attribute 'width'"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        
    @height.setter
    def height(self, value):
        """Setting for private attribute 'height'"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setttr
    def x(self, value):
        """Setting for private attribute 'x'"""
        if (type(value) is not int):
            raise TypeError ("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Setting for private attribute 'y'"""
        if (type(value) is not int):
            raise TypeError ("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.y):
            print("")
        for h in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

def update(self, *args, **kwargs):
    if args and len(args) != 0:
        index = 0
        for arg in args:
            if index == 0:
                self.id = arg if arg is not None else self.id
            elif index == 1:
                self.width = arg
            elif index == 2:
                self.height = arg
            elif index == 3:
                self.x = arg
            elif index == 4:
                self.y = arg
            index += 1

    elif kwargs and len(kwargs) != 0:
        for key, value in kwargs.items():
            if key == "id":
                if value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

def to_dictionary(self):
    dict = {'id': self.id, 'width': self.width,
            'height': self.height, 'x': self.x,
            'y': self.y}
    return dict
