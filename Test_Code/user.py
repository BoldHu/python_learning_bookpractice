class User():
    '''用户类'''
    def __init__(self, first_name, last_name, birthday, location, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name)

    def greet_user(self):
        print(self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
