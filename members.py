class Member:
    def __init__(self, member_id, name, password_hash):
        self.member_id = member_id
        self.name = name
        self.password_hash = password_hash
        self.borrowed_books = []

    def to_dict(self):
        return {
            "member id" : self.member_id,
            "name" : self.name,
        }

