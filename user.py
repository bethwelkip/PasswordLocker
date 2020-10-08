

class User:
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
    # def login(self):
    #     pass
    #
    # def password(self):
    #     pass

    def username(self):
        pass

    def save_user(self):
        pass

    @classmethod
    def create_user(cls, username, password):
        user = User(username, password)
        user.save_user()

    def add_credential(self):
        pass

if __name__ == '__main__':
    print("type cu to create a new account or ")
