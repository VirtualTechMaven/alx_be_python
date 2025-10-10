#!/usr/bin/python3
"""
Module: class_static_methods_demo
This module demonstrates the difference between
class methods and static methods in Python using a Calculator class.
"""


class Calculator:
    """
    A simple calculator class to demonstrate
    class and static methods.
    """

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.

        Args:
            a (int or float): First number.
            b (int or float): Second number.

        Returns:
            int or float: Sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.

        Args:
            a (int or float): First number.
            b (int or float): Second number.

        Returns:
            int or float: Product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
