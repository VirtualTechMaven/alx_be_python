#!/usr/bin/python3
"""
Module: polymorphism_demo
This module demonstrates polymorphism and method overriding in Python OOP.
It defines a Shape base class and derived classes Rectangle and Circle.
"""

import math


class Shape:
    """
    Base class representing a geometric shape.
    """

    def area(self):
        """
        Method to calculate the area of a shape.
        Should be overridden by all subclasses.

        Raises:
            NotImplementedError: If subclass does not implement this method.
        """
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    """

    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.

        Args:
            length (float or int): The length of the rectangle.
            width (float or int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    """
    Derived class representing a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float or int): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
