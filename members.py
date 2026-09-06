class Member:
    def __init__(self, member_id, name, password_hash, phone_num):
        self.member_id = member_id
        self.name = name
        self.password_hash = password_hash
        self.borrowed_books = []
        self.phone_num = phone_num

    def to_dict(self):
        return {
            "member_id" : self.member_id,
            "name" : self.name,
            "phone_number" : self.phone_num,
            "password" : self.password_hash
        }

