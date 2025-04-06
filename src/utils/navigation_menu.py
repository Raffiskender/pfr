import streamlit as st
from ROUTES import ROUTES_MATCH_MENU
from src.router import Router

class Navigation_menu():
    def __init__(self):
        self.routes = list(ROUTES_MATCH_MENU.keys())
        self.menus = list(ROUTES_MATCH_MENU.values())

    def main_menu(self):
        st.radio("", options=self.menus, key='menu')
        match st.session_state['menu']:
            case _ if st.session_state['menu'] == self.menus[0]:
                Router.redirect(self.routes[0])
            case _ if st.session_state['menu'] == self.menus[1]:
                Router.redirect(self.routes[1])
            case _ if st.session_state['menu'] == self.menus[2]:
                Router.redirect(self.routes[2])
            case _ if st.session_state['menu'] == self.menus[3]:
                Router.redirect(self.routes[3])
            case _ if st.session_state['menu'] == self.menus[4]:
                Router.redirect(self.routes[4])
            case _:
                Router.redirect('404')