import streamlit as st
from streamlit.components.v1 import html
from src.utils.navigation_menu import Navigation_menu
from VARS import PAGES

class Main_page():
    def __init__(self):
        self.css_path='./src/assets/style'
        self.page = self.init_navigation()
        self.run()

    def init_navigation(self):
       return st.navigation(PAGES, position="sidebar", expanded=True)

    def get_page(self):
        return self.page

    def load_css(self):
        with open(f'{self.css_path}/vars.css') as f:
            st.html(f'<style>{f.read()}</style>')
        with open(f'{self.css_path}/style.css') as f:
            st.html(f'<style>{f.read()}</style>')
        with open(f'{self.css_path}/navigation_style.css') as f:
            st.html(f'<style>{f.read()}</style>')
        with open(f'{self.css_path}/texts_style.css') as f:
            st.html(f'<style>{f.read()}</style>')

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

app = Main_page()
app.load_css()

navigation = Navigation_menu()
navigation.load_menu(app.get_page())

app.load_js()