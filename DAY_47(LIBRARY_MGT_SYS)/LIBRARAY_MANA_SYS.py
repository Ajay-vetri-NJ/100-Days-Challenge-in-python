class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title):
        new_book = Book(title)
        self.books.append(new_book)

    def add_member(self, name):
        new_member = Member(name)
        self.members.append(new_member)

    def borrow_book(self, member_name, book_title):
        book = next((b for b in self.books if b.title == book_title and not b.is_borrowed), None)
        if book:
            book.is_borrowed = True
            print(f"{member_name} borrowed '{book_title}'")
        else:
            print(f"'{book_title}' is not available")

    def return_book(self, book_title):
        book = next((b for b in self.books if b.title == book_title and b.is_borrowed), None)
        if book:
            book.is_borrowed = False
            print(f"'{book_title}' has been returned")
        else:
            print(f"'{book_title}' is not borrowed or not found")

    def show_books(self):
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"'{book.title}' - {status}")

library = Library()

library.add_book("The Great Gatsby")
library.add_book("1984")
library.add_book("Pride and Prejudice")

library.add_member("Alice")
library.add_member("Bob")

library.show_books()

library.borrow_book("Alice", "1984")
library.show_books()
library.return_book("1984")
library.show_books()