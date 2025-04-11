import streamlit as st
from src.controllers.session_controller import SessionController
import time

def load():

    st.title('Logout')
    if st.button('Deconnexion'):
        with st.spinner('Deconnexion'):
            SessionController().logout()
load()