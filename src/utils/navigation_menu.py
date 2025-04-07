import streamlit as st
from VARS import MENUS_LABEL_MATCH_ROUTES

class Navigation_menu():
    def __init__(self):
        self.menu_labels=list(MENUS_LABEL_MATCH_ROUTES.keys())
        self.routes=list(MENUS_LABEL_MATCH_ROUTES.values())

    def main_menu(self, page):
        st.radio(label="Menu",
                 options=self.menu_labels,
                 key='menu',
                 index=self.menu_labels.index(page._title),
                 label_visibility='hidden',
                 on_change=self.redirect()
                 )
    
    def redirect(self):
        if 'menu' in st.session_state:
            for index, value in enumerate(self.menu_labels):
                if st.session_state.menu == value:
                    st.switch_page(f"src/views/{self.routes[index]}.py")