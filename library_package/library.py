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
    
    def find_book(self,title):
        for bk in self.books:
            if bk.title.lower() == title.lower():
                return bk
        return None
            
        
    def list_available_books(self):
        available = [bk for bk in self.books if bk.is_available]
        if not available:
            print("No available books")
        return available
         
