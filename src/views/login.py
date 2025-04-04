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
        st.session_state.SESSION_LOGGED = res.logged
        redirect("home")

    
def sign_up():
    res = signup(st.session_state.email, st.session_state.password)
    if not res:
        st.text("E-mail already used. Please, log in.")
    else: 
        st.text("Sign up in progress...")
        redirect("home")



# Initialiser le gestionnaire de session

#session = SessionManager()
# Interface Streamlit
# st.title("🔐 Connexion avec token JWT (via SessionManager)")

# if "user" not in st.session_state:
#     st.session_state["user"] = None

# token = session.get_cookie()
# user_data = session.verify_token(token) if token else None

# if user_data:
#     st.session_state["user"] = user_data["user"]
#     st.success(f"✅ Connecté en tant que {st.session_state['user']}")
#     if st.button("Se déconnecter"):
#         session.delete_cookie()
#         st.session_state["user"] = None
#         st.rerun()

