class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.borrowed = False
        self.borrowed_by = None
        self.borrowed_date = None

    def to_dict(self):
        return {
            "title" : self.title,
            "author" : self.author,
            "year" : self.year,
            "book_id" : self.book_id,
            "is_borrowed" : self.borrowed,
            "borrowed_by" : self.borrowed_by,
            "borrowed_date" : self.borrowed_date
        }

