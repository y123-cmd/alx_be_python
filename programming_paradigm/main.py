from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    if library.check_out_book("1984"):
        print("\nChecked out '1984'.")
    else:
        print("\n'1984' is not available for checkout.")

    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    if library.return_book("1984"):
        print("\nReturned '1984'.")
    else:
        print("\n'1984' was not checked out.")

    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
