import streamlit as st
from VARS import MENUS_PAGES_TITLES

class Navigation_menu():
    def __init__(self):
        self.menus_and_pages_titles = MENUS_PAGES_TITLES

    def main_menu(self, page):
        st.radio(label="Menu",
                 options=self.menus_and_pages_titles,
                 key='menu',
                 index=self.menus_and_pages_titles.index(page._title),
                 label_visibility='hidden',
                 on_change=self.check()
                 )
    
    def check(self):
        if 'menu' in st.session_state:
            match st.session_state.menu:
                case _ if st.session_state['menu'] == self.menus_and_pages_titles[0]:
                    st.switch_page("src/views/home.py")
                case _ if st.session_state['menu'] == self.menus_and_pages_titles[1]:
                    st.switch_page("src/views/cleaning.py")
                case _ if st.session_state['menu'] == self.menus_and_pages_titles[2]:
                    st.switch_page("src/views/eda.py")
                case _ if st.session_state['menu'] == self.menus_and_pages_titles[3]:
                    st.switch_page("src/views/viz.py")
                case _ if st.session_state['menu'] == self.menus_and_pages_titles[4]:
                    st.switch_page("src/views/conclusion.py")
                case _ :
                    st.switch_page("src/views/page_404.py")
