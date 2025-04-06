import streamlit as st
from src.views import home, cleaning, eda, viz, conclusion, page_404
from ROUTES import ROUTES_MATCH_MENU

class Router:
    def __init__(self):
        pass
    
    def get_route():
        url = st.query_params.get("page")
        if url is None:
            url = 'home'
        return url
    
    def redirect(new_route):
        routes = list(ROUTES_MATCH_MENU.keys())

        match new_route:
            case _ if new_route == routes[0]:
                home.load()
            case _ if new_route == routes[1]:
                cleaning.load()
            case _ if new_route == routes[2]:
                eda.load()
            case _ if new_route == routes[3]:
                viz.load()
            case _ if new_route == routes[4]:
                conclusion.load()
            case '404':
                page_404.load()

        st.query_params.update(page=new_route)
