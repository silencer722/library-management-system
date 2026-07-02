class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        if self.available:
            return f"{self.title} - {self.author} - {self.year} - ✅ Available"
        else:
            return f"{self.title} - {self.author} - {self.year} - ❌ Borrowed"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        print('Sorry, this book is already borrowed.')
        return False

    def return_book(self):
        if not self.available:
            self.available =True
            return True
        print('This book is already in the library.')
        return False