import streamlit as st
# from src.controllers.auth import auth
# from src.controllers.signup import signup

# from src.router import redirect

def load():
    st.title('Login')

load()



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

