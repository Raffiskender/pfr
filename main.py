import streamlit as st
from streamlit.components.v1 import html
from src.router import Router


class Main_page():
    def __init__(self):
        self.declare_pages()
        self.css_path='./src/assets/style'
        self.run()
        self.route_match_menu={
            'home'      :'Accueil',
            'cleaning'  :'Nettoyage',
            'eda'       :'Analyse',
            'viz'       :'Visualisation',
            'conclusion':'Conclusion'
        }
        if "first_page_passed" not in st.session_state:
            self.navigate_to_first_page()
            st.session_state["first_page_passed"] = True

    def declare_pages(self):
        self.pages = [
            st.Page("./src/views/home.py", default=True),
            st.Page("./src/views/cleaning.py"),
            st.Page("./src/views/eda.py"),
            st.Page("./src/views/viz.py"),
            st.Page("./src/views/conclusion.py"),
        ]

        self.pg = st.navigation(self.pages)

    def navigation_menu(self):
        routes = list(self.route_match_menu.keys())
        menus = list(self.route_match_menu.values())

        st.radio("", options=menus, key='menu')
        match st.session_state['menu']:
            case _ if st.session_state['menu'] == menus[0]:
                Router.redirect(routes[0])
            case _ if st.session_state['menu'] == menus[1]:
                Router.redirect(routes[1])
            case _ if st.session_state['menu'] == menus[2]:
                Router.redirect(routes[2])
            case _ if st.session_state['menu'] == menus[3]:
                Router.redirect(routes[3])
            case _ if st.session_state['menu'] == menus[4]:
                Router.redirect(routes[4])
            case _:
                Router.redirect('404')

    def navigate_to_first_page(self):
        destination = Router.get_route()
        st.session_state.menu = self.route_match_menu.get(destination)

    def load_css(self):
        with open(f'{self.css_path}/vars.css') as f:
            st.html(f'<style>{f.read()}</style>')
        with open(f'{self.css_path}/style.css') as f:
            st.html(f'<style>{f.read()}</style>')
        with open(f'{self.css_path}/navigation_style.css') as f:
            st.html(f'<style>{f.read()}</style>')
        with open(f'{self.css_path}/texts_style.css') as f:
            st.html(f'<style>{f.read()}</style>')

    def run(self):
        self.pg.run()

#-- Lancement de l'appli --#
st.set_page_config(layout='wide', page_title='Mon app multipage', page_icon=('./src/assets/images/ico.png'))
app = Main_page()
app.load_css()
app.navigation_menu()


#-- ici injection de js --#
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