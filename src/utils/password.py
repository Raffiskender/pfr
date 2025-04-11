import re

class PasswordCheck:
    def __init__(self, password):
        self.password = password
        self.passwd_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,22}$'

    def is_password_strong(self):
        return isinstance(re.fullmatch(self.passwd_regex, self.password), re.Match)
        return True
