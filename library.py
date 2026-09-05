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
        title = input("\ttilte : ")
        author = input("\tauthor : ")
        year = input("\tyear : ")
        book_id = self.id_generate("book")

        approval = input(f"\t{title} from {author} in {year}. \
do you want to save this? (y/n)").lower

        if approval in ["y", "yes"]:
            new_book = Book(title, author, year, book_id)
            self.books.append(new_book.data)
            print("\tBook added successfully.")

    def add_member(self):
        name = input("\tyour name : ")
        while True:
            password1 = input("\tpassword : ")
            password2 = input("\tre-enter password : ")
            if password1 == password2:
                password = password1
                break
            else:
                print("\tpassword does not match. try again.")
        membar_id = self.id_generate("\tmember")

        new_member = Member(membar_id, name, password)
        self.members.append(new_member.data)

        print(f"\tmember {name} created successfully.")

    def show_data(self, type):
        if type == "books":
            for book in self.books:
                for key, valu in book.items():
                    print(f"\t{key} = {valu}")
                print("\t---------------")

        if type == "members":
            for member in self.members:
                for key, valu in member.items():
                    print(f"\t{key} = {valu}")
                print("\t---------------")


