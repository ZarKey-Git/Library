class Library:
    def __init__(self, book_name, book_author, book_genre, book_id, patron_name, patron_id):
        self.book_name = book_name
        self.book_author = book_author
        self.book_genre = book_genre
        self.book_id = book_id
        self.patron_name = patron_name
        self.patron_id = patron_id
        self.books = []


class BookBorrowed(Library):
    def list_book(self):
        while True:
            book = input("enter book name or for exit enter nothing:")
            self.books.append(book)
            if book == "":
                break
        return self.books

    def patron_info(self):
        return f"{self.patron_name} with id {self.patron_id}"


author = input('''enter Author's name:''')
genre = input('''enter book's genre:''')
b_id = int(input("enter Book id:"))
p_name = input("enter your name:")
p_id = int(input("enter yor id:"))

status = BookBorrowed(None, author, genre, b_id, p_name, p_id)
print(status.patron_info(), "have books:", status.list_book())
