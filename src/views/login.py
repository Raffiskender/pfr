import streamlit as st
from src.controllers.auth import auth
from src.controllers.signup import signup


from src.router import redirect
def load_view():
    st.title('Login')

    st.text_input('Email', '', key='email')
    st.text_input('Password', '', type='password', key='password', on_change=login)
    col1, col2 = st.columns([1, 1], gap="small")
    with col1:
        st.button('Login', on_click=login)
    with col2:
        st.button('Sign up', on_click=sign_up)


def login():
    res = auth(st.session_state.email, st.session_state.password)
    if not res:
        st.text("Wrong Account")
    else: 
        redirect("home")
    
def sign_up(email, password):
    res = signup(email, password)
    if not res:
        st.text("E-mail already used. Please, log in.")
    else: 
        st.text("Sign up in progress...")
        redirect("home")