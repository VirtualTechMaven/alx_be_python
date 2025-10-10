#!/usr/bin/python3
"""
Module: book_class
This module defines a Book class that demonstrates the use of
Python magic methods such as __init__, __del__, __str__, and __repr__.
"""


class Book:
    """
    A class to represent a Book with title, author, and publication year.
    Demonstrates key Python magic methods.
    """

    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method called when the object is about to be deleted.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method for user-friendly display.

        Returns:
            str: A readable description of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the Book object.

        Returns:
            str: A string that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
