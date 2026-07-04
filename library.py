class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return True

    def remove_book(self, title, author):
        book = self.find_book(title, author)
        if book:
            self.books.remove(book)
            print(f"\n✅ '{book.title}' removed successfully.")
            return True
        print(f"\n❌{title} by {author} was not found.")
        return False

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Library with {len(self)} books"

    def get_books(self):
        return self.books

    def find_book(self, title, author):
        for book in self.books:
            if title == book.title and author == book.author:
                return book
        return None
