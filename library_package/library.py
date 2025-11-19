from .book import Book
class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,book:Book):
        self.books.append(book)
        print(f"book added{book}")
    
    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn:
                self.books.remove(book)
                print(f"Book removed: {book.title}")
            return
        print("Book not found.")
                
