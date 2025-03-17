import streamlit as st

def load_view():
    st.title('403 Page')
    st.markdown('Vous n\'avez pas les droits pour accéder à cette page, veuillez <a href="/?nav=/login" target="_self">vous connecter</a> ou revenir à <a href="/?nav=/home" target="_self">l\'accueil</a>', unsafe_allow_html=True)