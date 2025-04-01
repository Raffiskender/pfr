import streamlit as st
path = "src/assets/styles/"

def inject_custom_css():
    with open(f'{path}styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with open(f'{path}styles_texts.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with open(f'{path}styles_navigation.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with open(f'{path}vars.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
