import streamlit as st
from streamlit.components.v1 import html
import utils as utl

from src.views import home, goal, dataset, analysis, conclusion, options, login, logout, page_404, page_403
from src.router import get_route

import json


def load_session():
    #Loading Cookies
    with open('session.json') as json_file:
        st.session_state.SESSION = json.load(json_file)

def navigation():  


    route = get_route()

    if route == "/home":
        home.load_view()
    elif route == "/goal":
        if st.session_state.SESSION['email'] != "":
            goal.load_view()
        else:
            page_403.load_view()
    elif route == "/dataset":
        if st.session_state.SESSION['email'] != "":
            dataset.load_view()
        else:
            page_403.load_view()
    elif route == "/analysis":
        if st.session_state.SESSION['email'] != "":
            analysis.load_view()
        else:
            page_403.load_view()
    elif route == "/conclusion":
        if st.session_state.SESSION['email'] != "":
            conclusion.load_view()
        else:
            page_403.load_view()
    elif route == "/options":
        if st.session_state.SESSION['email'] != "":
            goal.load_view()
        else:
            page_403.load_view()
    elif route == "/logout":
        logout.load_view()
    elif route == "/login":
        login.load_view()

    else:
        page_404.load_view()


st.set_page_config(layout="centered", page_title='Anxiety attack')
load_session()
utl.navbar_component()
utl.inject_custom_css()

navigation()
