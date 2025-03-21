import streamlit as st
import datetime
import jwt

from streamlit_cookies_controller import CookieController

class SessionManager:
    def __init__(self):
        pass
        #load_dotenv()
        #self.secret_key = os.getenv("SECRET_KEY", "clé_par_defaut_pour_dev")

    #Crée un token JWT valable 1 semaine
    def create_token(self, username):
        payload = {
            "user": username.user,
            "email": username.email,
            "is_admin": username.is_admin,
            "activated": username.activated,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }
        self.set_cookie(payload)
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def verify_token(self, token):
        """Vérifie et décode le token JWT"""
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None  # Token expiré
        except jwt.InvalidTokenError:
            return None  # Token invalide

    def set_cookie(self, token):
        # Crée un cookie avec le token JWT
        cookie_controller = CookieController()
        cookie_name = "user_session"
        cookie_controller.set(cookie_name, token)

    def get_cookie(self):
        cookie_controller = CookieController()
        cookie_name = "user_session"
        if cookie_controller.get(cookie_name):
            print(f"Le cookie {cookie_name} existe avec la valeur : {cookie_controller.get(cookie_name)}")
            return cookie_controller.get(cookie_name)
        
        else :
            print(f"Le cookie {cookie_name} n'existe pas")
            return False

    def delete_cookie(self):
        """Supprime le cookie (déconnexion)"""
        st.query_params.update(auth="")
        st.session_state.pop("set_cookie", None)

