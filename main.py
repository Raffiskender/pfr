import streamlit as st
from streamlit.components.v1 import html
from src.utils.navigation import Navigation
from src.controllers.session_controller import SessionController
import time

class Main_page():
    def __init__(self):
        self.css_path='./src/assets/style'
        self.check_session()
        self.page = Navigation().user_navigation()
        self.run()

    def get_page(self):
        return self.page

    def check_session(self):
        if 'user' not in st.session_state:
            session = SessionController()
            user = session.check_user()

            if isinstance(user, dict):
                st.session_state['user'] = {
                    'id' : user['id'],
                    'username' : user['username'],
                    'email' : user['email'],
                    'roles' : user['roles']
                }    
            else : st.session_state['user'] = None

    def load_css(self):
        with open(f'{self.css_path}/new_style.css') as f:
            st.html(f'<style>{f.read()}</style>')
        # with open(f'{self.css_path}/vars.css') as f:
        #     st.html(f'<style>{f.read()}</style>')
        # with open(f'{self.css_path}/style.css') as f:
        #     st.html(f'<style>{f.read()}</style>')
        # with open(f'{self.css_path}/navigation_style.css') as f:
        #     st.html(f'<style>{f.read()}</style>')
        # with open(f'{self.css_path}/texts_style.css') as f:
        #     st.html(f'<style>{f.read()}</style>')

    def load_js(self):
        html(
            f"""
            <script>
                const plus_btn = window.parent.document.querySelector('button.plus_menu');
                const labels = window.parent.document.querySelectorAll('div[role="radiogroup"] label');
                const burger_btn = window.parent.document.querySelector('div.nav_burger_btn');
                
                function show_params_menu() {{
                    const params_menu = window.parent.document.querySelectorAll('div[role="radiogroup"] label:nth-of-type(n+7)');
                    state = plus_btn.classList
                    if (state.contains("active")){{
                        plus_btn.classList.remove('active')
                        for (menu of params_menu){{
                            menu.classList.remove("show_menu")
                        }}
                    }}
                    else{{
                        plus_btn.classList.add("active")
                        for (menu of params_menu){{
                            menu.classList.add("show_menu")
                        }}
                    }}
                }}

                function active_burger_menu() {{
                    const menu = window.parent.document.querySelector('.stRadio:first-of-type')
                    if (burger_btn.classList.contains('active')){{
                        burger_btn.classList.remove('active')
                        menu.classList.remove('active')
                    }}
                    else{{
                        burger_btn.classList.add('active')
                        menu.classList.add('active')
                    }}
                }}
                            
                for (const label of labels) {{
                    label.classList.remove('active');
                    if (label.querySelector('div:nth-of-type(2) > div > p').innerHTML === "{st.session_state.menu}") {{
                        label.classList.add('active');
                    }}
                }}

                plus_btn.addEventListener("click", show_params_menu);
                burger_btn.addEventListener("click", active_burger_menu);
            </script>
        """)

    def run(self):
        self.page.run()


#-- Lancement de l'appli --#
st.set_page_config(layout='wide')

with st.spinner('loading, please wait...'):
    app = Main_page()
    app.load_css()
    # app.load_js()

