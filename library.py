class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.borrower = None 
       

    def borrow(self, borrower_name):
        if self.available:
            self.available = False
            self.borrower = borrower_name
            print(f"{borrower_name} borrowed the book '{self.title}'")
        else:
            print("The book is already borrowed by someone else.")


    def return_book(self):
        if not self.available:
            self.available = True
            borrower_name = self.borrower
            self.borrower = None
            print(f"The book '{self.title}' has been returned by {borrower_name}")
        else:
            print("The book is not borrowed.")

class Library:
    def __init__(self):
        self.books = []
        self.available_books = [
            ("Learning JavaScript Design Patterns", "Addy Osmani"),
            ("The joy of PHP", "Alan Forbes"),
            ("Linux Pocket Guide: Essential Commands", "Daniel J.Barrett")
        ]

        for title, author in self.available_books:
            self.add_book(title, author)

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def search_book(self, keyword):
        found_books = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def view_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books available for borrowing.")

    def view_returned_borrowers(self):
        returned_borrowers = set()
        for book in self.books:
            if not book.available:
                returned_borrowers.add(book.borrower)
        if returned_borrowers:
            print("Returned Borrowers:")
            for borrower in returned_borrowers:
                print(f"- {borrower}")
        else:
            print("No borrowers have returned books yet.")


