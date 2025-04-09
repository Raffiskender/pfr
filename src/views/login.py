import streamlit as st
from src.controllers.user_controller import UserController
from src.controllers.session_controller import SessionController
import time

st.title('Login page')



with st.form("login_form"):
    user = False
    st.write("Entrez vos identifiants")
    login = st.text_input("login")
    passwd = st.text_input(label='Mot de passe', type="password")

    if st.form_submit_button('envoyer', use_container_width=True):
        user = UserController().login(login, passwd)

    #retour positif de la db
    if isinstance(user, dict):
        st.session_state['is_logged'] = True
        persist = SessionController().persist(user)
        st.session_state['user'] = user

        if persist[0]:
            st.write(f"Bonjour {user.get('username').capitalize()}")
            st.session_state['next_page'] = 'Accueil'
        else:
            st.write(f'Vous êtes connectés en mode dégradé : {persist[1]}')

    # valeur par défault
    elif user is False:
        st.warning('Entrez un login et un mot de passe')

    # retour null de la db
    elif user is None :
        st.error('Identifiants incorrects')

    # Cas d'erreur
    else:
        st.write(user)