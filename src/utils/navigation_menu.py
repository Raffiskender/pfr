import streamlit as st
from VARS import MENUS_LABEL_MATCH_ROUTES
import base64

class Navigation_menu():
    def __init__(self, page):
        self.page = page
        self.menu_labels=list(MENUS_LABEL_MATCH_ROUTES.keys())
        self.routes=list(MENUS_LABEL_MATCH_ROUTES.values())

        self.switch_page()
        self.load_menu()

    def load_menu(self):
        self.main_menu()
        self.option_menu()
        self.burger_menu()

    def main_menu(self):
        st.radio(label="Menu",
                 options=self.menu_labels,
                 key='menu',
                 index=self.menu_labels.index(self.page._title),
                 label_visibility='hidden',
                 on_change=self.redirect
                 )
    
    def redirect(self):
        print('changed - from redirect')
        st.session_state['next_page'] = st.session_state['menu']
    
    def switch_page(self):
        if "next_page" in st.session_state:
            page = st.session_state["next_page"]
            del st.session_state["next_page"]
            if page in self.menu_labels:
                route = self.routes[self.menu_labels.index(page)]
                st.switch_page(f"src/views/{route}.py")
    
    def option_menu(self):
        with open("src/assets/images/plus.png", "rb") as plus_sign:
            plus_sign_base64 = base64.b64encode(plus_sign.read())
        st.markdown(
        f'''<button class="plus_menu">
                <img src="data:image/png;base64, {plus_sign_base64.decode('utf-8')}"/>
            </button>
        ''', unsafe_allow_html=True)
    
    def burger_menu(self):
        st.markdown(
        '''
            <div>
                <div class="nav_burger_btn">
                    <span class="burger_bar"></span>
                    <span class="burger_bar"></span>
                    <span class="burger_bar"></span>
                </div>
            </div>
        ''', unsafe_allow_html=True
        )