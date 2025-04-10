import streamlit as st

def load():
    # Définir l'en-tête HTTP 404 ==> C'est foiré
    # st.markdown('HTTP/1.1 404 Not Found', unsafe_allow_html=True)

    # Du texte
    st.title('404 Page')
    st.markdown('This page doesn\'t exist, please go back to the <a href="/?page=/home" target="_self">home page</a>', unsafe_allow_html=True)

load()