
class User:

    def __init__(self, username, fullname, email, phone, state=True):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.state = state

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return []
