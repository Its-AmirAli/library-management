from books import *
from members import *

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

        new_book = Book(title, author, year, book_id)
        self.books.append(new_book.data)

    def add_member(self):
        name = input("your name : ")
        password = input("password : ")
        membar_id = self.id_generate("member")

        new_member = Member(membar_id, name, password)
        self.members.append(new_member.data)

    def show_data(self, type):
        if type == "books":
            for book in self.books:
                for key, valu in book.items():
                    print(f"{key} = {valu}")
                print("---------------")

        if type == "members":
            for member in self.members:
                for key, valu in member.items():
                    print(f"{key} = {valu}")
                print("---------------")


