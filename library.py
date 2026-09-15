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
        return None

    def add_book(self, title, author, year):
        book_id = self.id_generate("book")
        new_book = Book(title, author, year, book_id)
        self.books.append(new_book.to_dict())

    def add_member(self, name, password, phone_number):
        member_id = self.id_generate("member")
        new_member = Member(member_id, name, password, phone_number)
        self.members.append(new_member.to_dict())

    def get_data(self, type_of_data):
        if type_of_data == "books":
            return self.books

        if type_of_data == "members":
            return self.members
        return None

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

            elif category == "book id":
                if search_term == book["book_id"]:
                    search_result.append(book)

            elif category == "all":
                if search_term in book["title"].lower() or \
                    search_term in book["author"].lower():
                    search_result.append(book)

        return search_result
