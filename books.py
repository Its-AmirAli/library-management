class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.year = year
        self.available = True
    def to_dict(self):
        return {
            "title" : self.title,
            "author" : self.author,
            "year" : self.year,
            "book_id" : self.book_id,
            "is_available" : self.available
        }

