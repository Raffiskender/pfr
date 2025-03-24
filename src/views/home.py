import streamlit as st


def load_view():

    st.title("Les crises d'anxiété")
    st.markdown("""
    # Données sur les crises d'anxiété
    Cette appli a pour but de présenter un jeu de donnée sur l'anxiété, et de permettre de visualiser les données, de les analyser et de les interpréter.
    Les données sont issues de la compétition Kaggle "Anxiety Attack Prediction" et sont disponibles [ici](https://www.kaggle.com/raffiskender/anxiety-attack-prediction).
    
                
    ## Objectif
    Faire une EDA sur le jeu de données pour en extraire des informations pertinentes.

    ## Étapes suivies
    
    1. définission du problème
    2. acquisition et préparation des données
    3. analyse et exploration des données
    4. modélisation et prédiction
    5. visualisation et présentation des résultats
    6. soumission des résultats
    7. conclusion
                
    """)