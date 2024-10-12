class Library:
    """A class to represent a library."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private attribute to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)  # Append the Book instance to the list

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()  # Mark the book as checked out
                return True  # Return True if the checkout was successful
        return False  # Return False if the book is not available

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()  # Mark the book as available again
                return True  # Return True if the return was successful
        return False  # Return False if the book was not found

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]  # Filter available books
        for book in available_books:
            print(book)  # Print each available book

