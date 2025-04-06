import streamlit as st

PAGES = [
    st.Page("./src/views/home.py",       title='Accueil',        default=True),
    st.Page("./src/views/cleaning.py",   title='Nettoyage',      url_path="cleaning"),
    st.Page("./src/views/eda.py",        title='Analyse',        url_path="eda"),
    st.Page("./src/views/viz.py",        title='Visualisations', url_path="viz"),
    st.Page("./src/views/conclusion.py", title='Conclusion',    url_path="conclusion")
]

MENUS_PAGES_TITLES=[
    'Accueil',
    'Nettoyage',
    'Analyse',
    'Visualisations',
    'Conclusion'
]