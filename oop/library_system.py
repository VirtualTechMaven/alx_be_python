#!/usr/bin/python3
"""
Module: library_system
This module demonstrates inheritance and composition in Python OOP.
It defines classes for a library system with Book, EBook, PrintBook,
and Library classes.
"""


class Book:
    """
    Base class representing a general Book.
    """

    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Return a string representation of the Book instance.

        Returns:
            str: A formatted string with book details.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from the Book class.
    """

    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.

        Args:
            title (str): The title of the eBook.
            author (str): The author of the eBook.
            file_size (int): The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Return a string representation of the EBook instance.

        Returns:
            str: A formatted string with eBook details.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from the Book class.
    """

    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Return a string representation of the PrintBook instance.

        Returns:
            str: A formatted string with print book details.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class demonstrating composition.
    A Library contains and manages multiple Book objects.
    """

    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book (Book, EBook, or PrintBook instance) to the library.

        Args:
            book (Book): The book instance to be added.
        """
        self.books.append(book)

    def list_books(self):
        """
        Print details of all books in the library.
        """
        for book in self.books:
            print(book)
