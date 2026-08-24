class Member:
    def __init__(self, member_id, name, username, password_hash):
        self.member_id = member_id
        self.name = name
        self.username = username
        self.password_hash = password_hash
        self.borrowed_books = []

