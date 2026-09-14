from books import Book
from members import Member

class Library:
    def __init__(self):

        # these are test data
        self.books = [
            {
            "title": "Python",
            "author": "Jadi",
            "year": 2025,
            "book_id": 50501001,
            "is_borrowed" : False,
            "borrowed_by" : None,
            "borrowed_date" : None
            },
            {
            "title": "Clean Code",
            "author": "Robert Martin",
            "year": 2008,
            "book_id": 50501002,
            "is_borrowed" : True,
            "borrowed_by" : 20201001,
            "borrowed_date" : "2026/03/26"
            }
        ]

        self.members = [
            {
                "member_id" : 20201001,
                "name" : "AmirAli",
                "phone_number" : "+989123456789",
                "membership_date" : "2026/03/25",
                "password" : "12345"
            }
        ]

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
        input(f"\n{8*" "}Press Enter to return to menu.")

    def add_book(self):
        while True:
            title = input(f"{8*" "}title : ")
            author = input(f"{8*" "}author : ")
            year = input(f"{8*" "}year : ")

            approval = input(f"{8*" "}{title} by {author} in ({year}). \
do you want to save this? (y/n)").lower()

            if approval in ["y", "yes"]:
                book_id = self.id_generate("book")
                new_book = Book(title, author, year, book_id)
                self.books.append(new_book.to_dict())
                print(f"{8*" "}Book added successfully.")

                self.wait_for_continue()

                break
            elif approval in ["n", "no"]:
                print(f"{8*" "}Enter boobk information again. ")
            else:
                print(f"{8*" "}Please enter y/yes or n/no.")
            
    def add_member(self):
        name = input(f"{8*" "}your name : ")
        while True:
            phone_number = input(f"{8*" "}phone number(+989123456789) : ")
            if phone_number.startswith("+989") \
                and len(phone_number) == 13 \
                and phone_number[4:].isdigit():
                break
            else:
                print(f"{8*" "}please enter your number in (+989123456789) format. ")

        while True:
            password1 = input(f"{8*" "}password : ")
            password2 = input(f"{8*" "}re-enter password : ")
            if password1 == password2:
                password = password1
                member_id = self.id_generate("member")
                break
            else:
                print(f"{8*" "}password does not match. try again.")

        new_member = Member(member_id, name, password, phone_number)
        self.members.append(new_member.to_dict())

        print(
            f"\n\tmember {name}, {phone_number} created successfully."
            f"\nyour id is {member_id}, please remember your id."
            )

        self.wait_for_continue()

    def show_data(self, type_of_data):
        option_num = 1
        if type_of_data == "books":
            if not self.books:
                print(f"{8*" "}no book found.")
            else:
                for book in self.books:
                    print(f"{8*" "}{"-" * 15}")
                    print(f"{6*" "}{option_num}.")
                    option_num += 1

                    print(
                        f"{8*" "}Title : {book["title"]}\n"
                        f"{8*" "}Aothur : {book["author"]}\n"
                        f"{8*" "}Year : {book["year"]}\n"
                        f"{8*" "}Is Borrowed : {"NO" if book["is_borrowed"] else "Yes"}"
                        )

        if type_of_data == "members":
            if not self.members:
                print(f"{8*" "}no member found.")
            else:
                for member in self.members:
                    print(f"{8*" "}{"-" * 15}")
                    print(f"{6*" "}{option_num}.")
                    option_num += 1

                    print(
                        f"{8*" "}Member ID : {member["member_id"]}\n"
                        f"{8*" "}Name : {member["name"]}\n"
                        f"{8*" "}Phone Number : {member["phone_number"]}\n"
                        f"{8*" "}Membership Date : {member["membership_date"]}\n"
                    )

        print(f"{8*" "}{"-" * 15}")

        self.wait_for_continue()

    def search_books(self, category, search_term):
        search_term = search_term.lower()
        search_result = []

        for book in self.books:
            if category == "title":
                if search_term in book["title"].lower():
                    search_result.append(book)
            
            elif category == "author":
                if search_term in book["author"].lower():
                    search_result.append(book)
            
            elif category == "all":
                if search_term in book["title"].lower() or \
                    search_term in book["author"].lower():
                        search_result.append(book)

        return search_result


