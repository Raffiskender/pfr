import streamlit as st

def load_view():
    # Définir l'en-tête HTTP 403 ==> C'est foiré !
    # st.markdown('HTTP/1.1 403 Forbidden', unsafe_allow_html=True)

    #Du texte
    st.title('403 Page')
    st.markdown('Vous n\'avez pas les droits pour accéder à cette page, veuillez <a href="/?nav=/login" target="_self">vous connecter</a> ou revenir à <a href="/?nav=/home" target="_self">l\'accueil</a>', unsafe_allow_html=True)