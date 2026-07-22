class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def show_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You borrowed {book.title}")
                else:
                    print("This book is already borrowed.")
                return
        print("Book not found.")


if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Python Basics", "John"))
    library.add_book(Book("Data Science", "Ava"))
    library.show_books()
    library.borrow_book("python basics")
    library.show_books()
