import streamlit as st

from src.utils.navigation import Navigation
from src.controllers.session_manager import SessionManager
from streamlit_cookies_controller import CookieController
from src.utils import css_inject
from src.views import home, goal, dataset, analysis, conclusion, options, login, logout, page_404, page_403, admin
from src.router import get_route



def load_session():
    session = SessionManager()
    cookies_ctrl = CookieController()
    token = cookies_ctrl.get('user_session')
    verification = token and session.verify_token(token)
    
    if verification:
        return (1, verification['is_admin'])
    else:
        return False

def navigation():  
    route = get_route()
    
    match route:
        case "home":
            home.load_view()
        case "login":
            login.load_view()
        case "goal":
            if st.session_state.SESSION_LOGGED:
                goal.load_view()
            else:
                page_403.load_view()
        case "dataset":
            if st.session_state.SESSION_LOGGED:
                dataset.load_view()
            else:
                page_403.load_view()
        case "analysis":
            if st.session_state.SESSION_LOGGED:
                analysis.load_view()
            else:
                page_403.load_view()
        case "conclusion":
            if st.session_state.SESSION_LOGGED:
                conclusion.load_view()
            else:
                page_403.load_view()
        case "options":
            if st.session_state.SESSION_LOGGED:
                options.load_view()
            else:
                page_403.load_view()
        case "logout":
            if st.session_state.SESSION_LOGGED:
                logout.load_view()
            else:
                page_403.load_view()
        case "logout":
            if st.session_state.SESSION_LOGGED & st.session_state.IS_ADMIN:
                admin.load_view()
            else:
                page_403.load_view()
        case _:
            page_404.load_view()


st.set_page_config(layout="centered", page_title='Anxiety attack')
css_inject.inject_custom_css()
try:
    st.session_state.SESSION_LOGGED = False
    data = load_session()
    if data:
        st.session_state.SESSION_LOGGED = data[0]
        st.session_state.IS_ADMIN = data[1]

finally:
    nav = Navigation()
    nav.display_navbar()
    navigation()
