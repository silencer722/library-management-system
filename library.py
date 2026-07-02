class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book in self.books:
            print("This book already exists.")
            return False
        self.books.append(book)
        return True
    def remove_book(self, book):
        if book not in self.books:
            print('Book not found.')
            return False
        self.books.remove(book)
        return True

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Library with {len(self)} books"