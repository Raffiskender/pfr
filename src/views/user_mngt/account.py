import streamlit as st
from src.utils.password import PasswordCheck
from src.controllers.user_controller import UserController

def toggle_change_password_btn():
    st.session_state.change_password_btn = not st.session_state.change_password_btn

def load():
    if 'change_password_btn' not in st.session_state:
        st.session_state.change_password_btn = False


    display_pwd_form = False
    st.title('Mon compte')

    st.write("Bienvenue dans la page de l'utilisateur")
    st.write(f'Votre nom d\'utilisateur : {st.session_state['user']['username']}')
    st.write(f'Votre mail : {st.session_state['user']['email']}')
    st.write(f'Niveau : {st.session_state['user']['roles'][-1]}')

    st.button('Changer de mot de passe', on_click=toggle_change_password_btn)

    if st.session_state.change_password_btn:
        with st.form(key="change_pwd"):
            old_pwd = st.text_input('Mot de passe actuel', type='password')
            new_pwd = st.text_input('Nouveau mot de passe', type='password')
            verif = st.text_input('Vérification', type='password')

            if st.form_submit_button('Changer'):
                if old_pwd == "" or new_pwd == '':
                    st.warning('Entrez un mot de passe')
                elif new_pwd != verif:
                    st.warning('Les mots de passes ne correspondent pas')
                elif not PasswordCheck(new_pwd).is_password_strong():
                    st.warning('Le nouveau mot de passe doit contenir un caractère spécial, une majuscule, un chiffre et un caractère minuscule')
                else : 
                    change = UserController(st.session_state['user']['email'], old_pwd).change_pwd(new_pwd)
                    if change[0]:
                        st.warning('Votre mot de passe a été changé')
                    elif change[1]==None:
                        st.error(f'Erreur : Mot de passe incorrect')
                    else :
                        st.error(f'Erreur : {change[1]}')


    
load()