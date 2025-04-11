import streamlit as st
from src.controllers.user_controller import UserController
from src.controllers.session_controller import SessionController
import time
st.title('Login page')


with st.form(key="login_form"):
    st.write("Entrez vos identifiants")
    user = False
    login = st.text_input("Nom d'utilisateur ou mail")
    passwd = st.text_input(label='Mot de passe', type="password")

    if st.form_submit_button('envoyer', use_container_width=True):
        user = UserController(login, passwd).login()

    #retour positif de la db
    if isinstance(user, dict):
        st.session_state['user'] = user
        persist = SessionController().persist(user)
        time.sleep(0.5) # le temps d'écrire dans le session_state

        if persist[0]:
            st.write(f"Bonjour {user.get('username').capitalize()}")
        else:
            st.write(f'Vous êtes connectés en mode dégradé : {persist[1]}')
        st.switch_page('src/views/home.py')

    # valeur par défault
    elif user is False:
        st.warning('Entrez un login et un mot de passe')

    # retour null de la db
    elif user is None :
        st.error('Identifiants incorrects')

    # Cas d'erreur
    else:
        st.write(user)