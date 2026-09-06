from books import Book
from members import Member

class Library:
    def __init__(self):
        self.books = [{
        "title": "Python",
        "author": "Jadi",
        "year": 2025,
        "book_id": 50501001
    },
    {
        "title": "Clean Code",
        "author": "Robert Martin",
        "year": 2008,
        "book_id": 50501002
    }]
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

    def wait_for_continue(self):
        input("\n\tPress Enter to return to menu.")

    def add_book(self):
        while True:
            title = input("\ttitle : ")
            author = input("\tauthor : ")
            year = input("\tyear : ")

            approval = input(f"\t{title} by {author} in ({year}). \
do you want to save this? (y/n)").lower()

            if approval in ["y", "yes"]:
                book_id = self.id_generate("book")
                new_book = Book(title, author, year, book_id)
                self.books.append(new_book.to_dict())
                print("\tBook added successfully.")

                self.wait_for_continue()

                break
            elif approval in ["n", "no"]:
                print("\tEnter boobk information again. ")
            else:
                print("\tPlease enter y/yes or n/no.")
            
    def add_member(self):
        name = input("\tyour name : ")
        while True:
            phone_number = input("\tphone number(+989123456789) : ")
            if phone_number.startswith("+989") \
                and len(phone_number) == 13 \
                and phone_number[4:].isdigit():
                break
            else:
                print("\tplease enter your number in (+989123456789) format. ")

        while True:
            password1 = input("\tpassword : ")
            password2 = input("\tre-enter password : ")
            if password1 == password2:
                password = password1
                member_id = self.id_generate("member")
                break
            else:
                print("\tpassword does not match. try again.")

        new_member = Member(member_id, name, password, phone_number)
        self.members.append(new_member.to_dict())

        print(
            f"\n\tmember {name}, {phone_number} created successfully."
            f"\nyour id is {member_id}, please remember your id."
            )

        self.wait_for_continue()

    def show_data(self, type_of_data):
        if type_of_data == "books":
            if not self.books:
                print("\tno book found.")
            else:
                for book in self.books:
                    for key, value in book.items():
                        print(f"\t{"-" * 15}")
                        print(f"\t{key} = {value}")

        if type_of_data == "members":
            if not self.members:
                print("\tno member found.")
            else:
                for member in self.members:
                    print(f"\t{"-" * 15}")
                    print(
                        f"\tID : {member["member_id"]}"
                        f"\n\tname : {member["name"]}"
                        f"\n\tphone number : {member["phone_number"]}"
                    )

        print(f"\t{"-" * 15}")

        self.wait_for_continue()
