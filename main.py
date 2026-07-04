from menu import show_menu
from book import Book
from library import Library
from people import Member

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
library = Library()
member = Member(name, age)


def get_info_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    return title, author


print(f"\n👋 Hello, {member.name}!")
print("📚 Welcome to our Library Management System!")

while True:
    show_menu()

    choice = input("Please enter your choice: ").strip()

    if not choice.isdigit():
        print("❌ Please enter a number.\n")
        continue

    choice = int(choice)

    if choice < 1 or choice > 6:
        print("❌ Invalid choice.\n")
        continue

    if choice == 6:
        print(f"👋Goodbye {member.name}!")
        break
    elif choice == 1:
        title, author = get_info_book()
        year = int(input("year: "))
        book = Book(title, author, year)
        library.add_book(book)
        print(f"\n✅ {book.title} - {book.author} added successfully!")
    elif choice == 5:
        books = library.get_books()
        if not books:
            print("\n📚 No books in the library.")
        else:
            for book in books:
                print(book)
    elif choice == 3:
        title, author = get_info_book()
        book = library.find_book(title, author)
        if not book:
            print(f"\n❌ '{title}' by {author} was not found.")
        else:
            member.borrow(book)
    elif choice == 4:
        title, author = get_info_book()
        book = library.find_book(title, author)
        if not book:
            print(f"\n❌ '{title}' by {author} was not found.")
        else:
            member.return_book(book)
    elif choice == 2:
        title, author = get_info_book()
        library.remove_book(title, author)
