import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
from src.models.user_model import UserModel

class UserController:
    def __init__(self, username, password, email=''):
        self.username = username
        self.password=password
        self.email=email

    def login(self):
        with UserModel(self.username, self.password) as db:
            user = db.find_by_email_or_username()

        if isinstance(user, UserModel):
            return {
                'id' : user.get_id(),
                'username' : user.get_username(),
                'email' : user.get_email(),
                'roles' : user.get_roles()
            }
        else : return user
    
    def create_user(self):
        with UserModel(self.username, self.password, self.email) as db:
            new_user = db.insert_new_user()
        if isinstance(new_user, UserModel):
            del new_user
            return True,
        else: return False, new_user # as an error
