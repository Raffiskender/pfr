import streamlit as st
from streamlit.components.v1 import html
from src.utils.navigation_menu import Navigation_menu
from VARS import PAGES

class Main_page():
    def __init__(self):
        self.declare_pages()
        self.css_path='./src/assets/style'
        self.page = self.declare_pages()
        self.run()

    def declare_pages(self):
       return st.navigation(PAGES)

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
                const labels = window.parent.document.querySelectorAll('div[role="radiogroup"] label');
                    for (const label of labels) {{
                        label.classList.remove('active');
                        if (label.querySelector('div:nth-of-type(2) > div > p').innerHTML === "{st.session_state.menu}") {{
                            label.classList.add('active');
                    }}
                }}
            </script>
        """)

    def run(self):
        self.page.run()


#-- Lancement de l'appli --#
st.set_page_config(layout='wide')

app = Main_page()
app.load_css()

navigation = Navigation_menu()
navigation.main_menu(app.get_page())

app.load_js()