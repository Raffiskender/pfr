import streamlit as st

def load_view():
    st.title('404 Page')
    st.markdown('This page doesn\'t exist, please go back to the <a href="/?nav=/home" target="_self">home page</a>', unsafe_allow_html=True)