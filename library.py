from books import *

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.next_book_id = 1000
        self.next_member_id = 1000

    def id_generate(self, item_type):
        if item_type == "book":
            self.next_book_id += 1
            return int("5050" + str(self.next_book_id))
        if item_type == "member":
            self.next_member_id += 1
            return int("2020" + str(self.next_member_id))

    def add_book(self):
        title = input("tilte : ")
        author = input("author : ")
        year = input("year : ")
        book_id = self.id_generate("book")

        book = Book(title, author, year, book_id)
        self.books.append(book)