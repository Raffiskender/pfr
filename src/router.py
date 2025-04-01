import streamlit as st
from urllib.parse import unquote
import time

def get_route():
    url = st.query_params.get("page")
    url = url[0] if type(url) == list else url
    route = unquote(url) if url is not None else "home"
    return route

def redirect(new_route, reload=False):
    if new_route[0] != "/":
        new_route = new_route
    st.query_params.update(page=new_route)
