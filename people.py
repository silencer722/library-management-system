class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name.title()} ({self.age} years old)."

class Member(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.borrowed_books = []
        
    def borrow(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print("Book borrowed successfully.")
        else:
            print('Cannot borrow this book.')

class Librarian(Person):
    def add_book(self, library, book):
        return library.add_book(book)

    def remove_book(self, library, book):
        return library.remove_book(book)

    def __str__(self):
        return f"Librarian: {super().__str__()}"
        