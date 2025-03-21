from src.models.session import Session
from streamlit_cookies_controller import CookieController
import streamlit as st

def auth(login, mdp):
    session = Session(login, mdp)
    session.login()
    if session.logged:
        return session
    else:
        return False

def logout():
    cookies_ctrl = CookieController()
    st.session_state.SESSION_LOGGED = False
    #suppresion des infos du cookie :
    cookies_ctrl.set('user_session', '')
    # et suppression du cookie (si le browser le permet...)
    cookies_ctrl.remove('user_session') 

   # cookies_ctrl.remove('user_session')