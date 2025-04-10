import streamlit as st
from src.controllers.session_controller import SessionController
import time

def load():
    with st.spinner('deconnexion'):
        st.title('logout')
        SessionController().logout()
        # time.sleep(0.5) # le temps de changer le sessionstate avant la redirection
        # st.switch_page('src/views/home.py')
load()