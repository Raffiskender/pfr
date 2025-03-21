import streamlit as st
import datetime
import jwt

from dotenv import load_dotenv
import os

from streamlit_cookies_controller import CookieController

class SessionManager:
    def __init__(self):
        load_dotenv()
        self.secret_key = os.getenv("SECRET_KEY")

    #Crée un token JWT valable 1 semaine
    def create_token(self, user):
        print(f"from session_manager : {user}")
        payload = {
            "name": user[1],
            "email": user[2],
            "is_admin": user[3],
            "activated": user[4],
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")


    def verify_token(self, token):
        """Vérifie et décode le token JWT"""
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            print('token expiré')
            return None  # Token expiré
        except jwt.InvalidTokenError:
            print('token invalide')
            return None  # Token invalide

    def is_user_connected(self):
        cookies_ctrl = CookieController()
        session_token = cookies_ctrl.get('user_session')
        if session_token:
            return session_token
        return False
