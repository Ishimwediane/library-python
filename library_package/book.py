class Book:
    def __init__(self,title,author,isbn,is_available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_available=is_available
        
    def __str__(self):
        if self.is_available:
            status="Available"
        status="Not Available"
        return f"{self.title} by {self.author} ISBN: {self.isbn} and {status}"