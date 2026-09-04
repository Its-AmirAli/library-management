class Member:
    def __init__(self, member_id, name, password_hash):
        self.member_id = member_id
        self.name = name
        self.password_hash = password_hash
        self.borrowed_books = []

        self.data = {
            "member id" : self.member_id,
            "author" : self.name,
        }