import streamlit as st
from src.controllers.session_manager import SessionManager
from streamlit_cookies_controller import CookieController

def load_view():
    st.title('Bienvenue dans le dashboard des users')
    pw = st.text_input('Tapez votre mot de passe pour un check de sécurité (la page est un peu dangeureuse...) : ', type='password')
    
    session = SessionManager()
    cookie_ctrl = CookieController()
    user_data = session.verify_token(cookie_ctrl.get('user_session'))
    if user_data:
        email = user_data['email']
        session.check_user_password(email, pw)
    