from book_management import Book


class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.name = name
        self.borrowed_books = []

    def get_user_id(self):
        return self.__user_id

    def borrow_book(self, book: Book):
        if book.stock > 0:
            book.update_stock(-1)
            self.borrowed_books.append(book.get_code())
        else:
            print(f"Cannot borrow {book.title}: Out of stock.")

    def return_book(self, book: Book):
        if book.get_code() in self.borrowed_books:
            book.update_stock(1)
            self.borrowed_books.remove(book.get_code())
        else:
            print(f"{self.name} has not borrowed this book.")

    def get_borrowed_books(self):
        return self.borrowed_books


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __iter__(self):
        self._index = 0
        self.books.sort(key=lambda b: b.title)
        return self

    def __next__(self):
        if self._index < len(self.books):
            book = self.books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration
