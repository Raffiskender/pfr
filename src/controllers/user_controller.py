import streamlit as st
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader
from src.models.user_model import UserModel
from dotenv import load_dotenv
import os

class UserController:
    def __init__(self):
        pass

    def login(self, login, password):
        with UserModel(login, password) as db:
            user = db.find_by_email_or_username()

        if isinstance(user, UserModel):
            return {
                'id' : user.get_id(),
                'username' : user.get_username(),
                'email' : user.get_email(),
                'roles' : user.get_roles()
            }
        else : return user
