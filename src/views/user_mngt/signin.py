import streamlit as st
from src.controllers.user_controller import UserController
from email.utils import parseaddr
import re



def is_mail_valid(email):
    nom, adresse = parseaddr(email)
    return '@' in adresse and '.' in adresse.split('@')[-1]

def is_password_strong(password):
    passwd_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,22}$'
    return isinstance(re.fullmatch(passwd_regex, password), re.Match)

def create_username_from_mail(email):
    return email.split('@')[0]

def create_new_user(l, e, p):
    return UserController(l, p, e).create_user()

def load():
    st.title('S\'enregistrer')
    with st.container(key="signin_form_container"):
        with st.form(key = 'informations_form'):
            st.write("Entrez vos informations")
            username = st.text_input('Nom d\'utilisateur', key='username_input')
            email = st.text_input('Email *')
            password = st.text_input('Mot de passe *', type='password')
            st.write('Le mot de passe doit faire 8 charactères, contenir au moins caractère spécial et 1 chiffre')
            verif = st.text_input('Valider *', type='password')
            st.html("<p>* : champs obligatoires</p>")

            if st.form_submit_button('s\'enregistrer', use_container_width=True):
                if not email:
                    st.warning('Entrez une adresse email')
                elif not is_mail_valid(email):
                    st.warning('Entrez une adresse mail valide')
                elif not password:
                    st.warning('Entrez un mot de passe')
                elif not is_password_strong(password):
                    st.warning("Le mot de passe n'est pas assez fort")
                elif password != verif:
                    st.warning('Les mots de passes ne correspondent pas')
                else:
                    if not username:
                        username = create_username_from_mail(email)
                    
                    new_user = create_new_user(username, email, password)
                    if new_user[0]:
                        st.warning(f'Nouvel utilisateur {username} enregistré, vous pouvez à présent vous connecter')
                    else:
                        st.warning(f'Erreur : {new_user[1]}')

load()


# st.header("Styled Radio Buttons")
# st.radio("Pick a choice:", ["Choice A", "Choice B", "Choice C"], key="styled_radio")

# st.header("Buttons")
# st.button("I'm a green button", key="green")
# st.button("Click Me!", key="pulse")

# st.text_input("Enter your favorite quote:", key='the_input_prout')