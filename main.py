import streamlit as st
import json

from src.utils.navigation import Navigation
from src.controllers.session_manager import SessionManager

from src.utils import css_inject
from src.views import home, goal, dataset, analysis, conclusion, options, login, logout, page_404, page_403
from src.router import get_route



def load_session():
    session = SessionManager()
    token = session.get_cookie()
    st.session_state.SESSION = {}
    st.session_state.SESSION['email'] = ''
    if token:
        print(token)
        st.session_state.SESSION['email'] = 'coucou'
    #user_data = session.verify_token(token) if token else None
    else:
        print('pas de session en cours')

def navigation():  
    route = get_route()
    session_is_open = st.session_state.SESSION['email'] != ""
    
    match route:
        case "home":
            home.load_view()
        case "login":
            login.load_view()
        case "goal":
            if session_is_open:
                goal.load_view()
            else:
                page_403.load_view()
        case "dataset":
            if session_is_open:
                dataset.load_view()
            else:
                page_403.load_view()
        case "analysis":
            if session_is_open:
                analysis.load_view()
            else:
                page_403.load_view()
        case "conclusion":
            if session_is_open:
                conclusion.load_view()
            else:
                page_403.load_view()
        case "options":
            if session_is_open:
                options.load_view()
            else:
                page_403.load_view()
        case "logout":
            if session_is_open:
                logout.load_view()
            else:
                page_403.load_view()
        case _:
            page_404.load_view()


st.set_page_config(layout="centered", page_title='Anxiety attack')
load_session()

nav = Navigation()
nav.display_navbar()

css_inject.inject_custom_css()

navigation()
