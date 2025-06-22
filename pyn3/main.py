# main.py

from book_management import PhysicalBook, EBook, display_books
from library_management import User, Library


def main():
    b1 = PhysicalBook("B001", "Python Cơ Bản", "Nguyễn Văn A", 3, "mới")
    b2 = PhysicalBook("B002", "Lập trình Java", "Trần Văn B", 2, "cũ")
    b3 = PhysicalBook("B003", "C++ Nâng Cao", "Lê Văn C", 1, "mới")
    b4 = EBook("E001", "Machine Learning", "Hoàng Văn D", 5, "PDF")
    b5 = EBook("E002", "Deep Learning", "Phạm Thị E", 4, "EPUB")

    lib = Library()
    for book in [b1, b2, b3, b4, b5]:
        lib.add_book(book)

    u1 = User("U001", "Ngọc")
    u2 = User("U002", "Minh")

    u1.borrow_book(b1)
    u1.borrow_book(b4)
    u2.borrow_book(b2)
    u2.borrow_book(b5)

    u1.return_book(b1)

    print("\nList sách trong thư viện (theo tiêu đề):")
    for book in lib:
        print(book.get_info())

    print("\n_ Hiển thị thông tin sách (đa hình):")
    display_books(lib.books)

    print("\n_ Danh sách sách đang mượn:")
    print(f"{u1.name}: {u1.get_borrowed_books()}")
    print(f"{u2.name}: {u2.get_borrowed_books()}")


if __name__ == "__main__":
    main()
