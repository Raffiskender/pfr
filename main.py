import streamlit as st
from streamlit.components.v1 import html

from src.utils.navigation import Navigation
from src.controllers.session_manager import SessionManager
from streamlit_cookies_controller import CookieController
from src.utils import css_inject
from src.views import home, viz, cleaning, eda, conclusion, options, login, logout, page_404, page_403, admin
from src.router import get_route

def load_session():
    # cookies_ctrl = CookieController()
    # session = SessionManager()
    
    # token = cookies_ctrl.get('user_session')
    # verification = session.verify_token(token)

    # if token and verification:
    #     st.session_state.SESSION_LOGGED = True
    #     st.session_state.IS_ADMIN = verification['is_admin']
    # else:
    #     st.session_state.SESSION_LOGGED = False

    # load_page()
    # st.session_state.SESSION_LOADING = False
    st.session_state.SESSION_LOGGED = True

def load_page():
    nav = Navigation()
    nav.display_navbar()
    navigation()

def navigation():  
    route = get_route()
    
    match route:
        case "home":
            home.load_view()
        case "login":
            login.load_view()
        case "cleaning":
            if st.session_state.SESSION_LOGGED:
                cleaning.load_view()
            else:
                page_403.load_view()
        case "eda":
            if st.session_state.SESSION_LOGGED:
                eda.load_view()
            else:
                page_403.load_view()
        case "viz":
            if st.session_state.SESSION_LOGGED:
                viz.load_view()
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
        case _:
            page_404.load_view()


st.set_page_config(layout="wide", page_title='Anxiety attack')
css_inject.inject_custom_css()

# if 'SESSION_LOGGED' not in st.session_state:
#     st.session_state.SESSION_LOGGED = False
#     load_session()
#     load_page()
    
# else:
load_session()
load_page()

html(
'''
<script>
    // Suppression du iframe d'en haut
    window.parent.document.querySelector('.stIFrame').remove();

    // Dropdown hide / show

    var dropdown = window.parent.document.querySelector("img.dropbtn");
    var dropWindow = window.parent.document.getElementById("myDropdown")
    dropdown.onclick = () => {
        if (dropWindow.style.visibility == "hidden"){
            dropWindow.style.visibility = "visible";
            window.parent.document.addEventListener('click', (event) => {
                if (event.target != dropdown ){
                    dropWindow.style.visibility = "hidden";
                    }
            }, once=true);
        }else{
            dropWindow.style.visibility = "hidden";
        }
    };

    // Burger menu hide / show
    var burger_btn = window.parent.document.querySelector(".nav_burger_btn");
    var burger_nav = window.parent.document.querySelector(".navbar_burger");

    burger_btn.onclick = () => {
        burger_btn.classList.toggle("active");
        burger_nav.classList.toggle("active");
    }
</script>
''')