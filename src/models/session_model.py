import datetime
import jwt
from src.models.database import Database
from dotenv import load_dotenv
import os

from streamlit_cookies_controller import CookieController


class SessionModel:
    def __init__(self):
        load_dotenv()
        self.secret_key = os.getenv("SECRET_KEY")

    #Crée un token JWT valable 1 semaine
    def create_token(self, user):
        payload = {
            "id": user.get('id'),
            "username": user.get('username').capitalize(),
            "email": user.get('email'),
            "roles": user.get('roles'),
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def decode_token(self, token):
        """Vérifie et décode le token JWT"""
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            print('token expiré')
            return None  # Token expiré
        except jwt.InvalidTokenError as e:
            print('token invalide')
            print(e)
            return None  # Token invalide

