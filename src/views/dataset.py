import streamlit as st
import pandas as pd
import base64

def load_view():
    st.title('Page du Jeux de données')
    df = pd.read_csv('./data/anxiety_attack_dataset.csv')
    df_clean = pd.read_csv('./data/clean_data.csv')
    st.markdown("""
    ## Données sur les crises d'anxiété"
    Ci-dessous les données brutes chargées depuis Kaggle.
    """)
    with st.expander("Afficher les données brutes"):
        st.dataframe(df)
    
    st.markdown("""
    ## Données nettoyées
    Ci-dessous les données nettoyées. Nottez qu'elles étaient propres à l'origine. J'ai juste ajouté quelques get_dummies pour faciliter l'exploiattion des données.   
    """)
    with st.expander("Afficher les données nettoyées"):
        st.dataframe(df_clean)

    st.markdown("""
    ## Description des données
    Les données présentent les données de 12000 sur des patients ayant eu une crise d'anxiété. Les colonnes sont les suivantes:
    - Age
    - Sexe
    - Métier
    - Heures de sommeil
    - Activité physique
    - Consommation de caféine
    - Consommation d'alcool
    - Tabagisme
    - Antécédents familiaux
    - Niveau de stress
    - Fréquence cardiaque pendant une crise
    - Fréquence respiratoire
    - Niveau de transpiration
    - Étourdissements
    - Médication
    - Séance de thérapie
    - Événement de vie récent
    - Qualité de l’alimentation
    - Gravité de la crise
                
    """)
    with open("src/assets/images/db_diagram.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())
    
    text = f"""
    ## présentation de la base de données
    Ci-dessous un diagramme de la base de données représentant les liaisons entre les tables
    <img class="db_diagram_img" src="data:image/png;base64, {image_as_base64.decode("utf-8")}" alt="Diagramme de la base de données"/>
    """
    st.markdown(text, unsafe_allow_html=True)