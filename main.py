from library_package import Book, Library

def main():
    library = Library()

    # Create books
    b1 = Book("Python Basics", "Alice Johnson", "001")
    b2 = Book("Advanced Python", "Bob Smith", "002", is_available=False)
    b3 = Book("Data Science 101", "Chris Lee", "003")

    # Add books
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    # List available books
    print("Available Books:")
    for book in library.list_available_books():
      print(book)


    # Find a book
    print("\nFinding 'Python Basics':")
    found = library.find_book("Python Basics")
    print(found)

    # Remove a book
    library.remove_book("002")


if __name__ == "__main__":
    main()
