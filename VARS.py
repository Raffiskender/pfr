import streamlit as st

MENUS_LABEL_MATCH_ROUTES={
    'Accueil'       :'home',
    'Nettoyage'     :"cleaning",
    'Analyse'       :"eda",
    'Visualisations':"viz",
    'Conclusion'    :"conclusion",
    'Admin'         :"admin",
    'Login'         :"login",
    'Signin'        :"signin",
    'Options'       :"options",
    'Mon compte'    :"account",
    'Logout'        :'logout',
}

PAGES = []
for key, value in MENUS_LABEL_MATCH_ROUTES.items():
    if key == "Accueil":
        PAGES.append(st.Page(f"./src/views/{value}.py", title=key, default=True))
    else:
        PAGES.append(st.Page(f"./src/views/{value}.py", title=key, url_path=value))
