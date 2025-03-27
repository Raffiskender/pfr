import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def load_view():    
    # Titre principal
    st.title("Objectifs du projet")

    # Introduction
    st.write("""
    L'objectif principal d'un projet de Data Analyse est de découvrir des informations pertinentes à partir de données brutes, en utilisant des outils statistiques et de visualisation. Cela implique une série d'étapes méthodologiques qui permettent de préparer, nettoyer, analyser et visualiser les données.
    """)


    # 1. Nettoyage des données
    st.subheader("1. Nettoyage des données")
    st.write("""
    Avant toute analyse, les données doivent être nettoyées.
    Au programme de cette étape : 
    - **Traitement des valeurs manquantes** : Remplir, imputer ou supprimer les valeurs manquantes en fonction du contexte.
    - **Correction des incohérences** : Identifier et rectifier les erreurs de saisie ou les doublons.
    - **Normalisation et transformation des données** : Mise à l'échelle des variables, conversion des formats de données, et agrégation des données si nécessaire.
    """)

    # 2. EDA & Analyse descriptive
    st.subheader("2. EDA & Analyse descriptive")
    st.write("""
    L'Exploratory Data Analysis (EDA) permet d'explorer la structure des données et de 
    mieux comprendre leurs caractéristiques statistiques.
    🔹 Calcul des statistiques de base (moyenne, médiane, écart-type, etc.).
    🔹 Identification des distributions des variables.
    🔹 Calcul des **corrélations** entre variables pour identifier les relations potentielles.
    """)
  
    # 3. Visualisation des données
    st.subheader("3. Visualisation des données")
    st.write("""
    Les visualisations permettent de mieux comprendre les tendances et les relations dans les données. 
    Nous utiliserons des graphiques adaptés comme les histogrammes, les nuages de points et les heatmaps pour représenter les corrélations.
    """)

    # 4. Conclusions
    st.subheader("4. Conclusions")
    st.write("""
    À la fin du projet, nous résumerons les principaux enseignements tirés des analyses. 
    Ces conclusions permettront de proposer des recommandations pour améliorer la prise de décision et guider les actions futures.
    """)

    # # Objectif 5 : Communication des résultats
    # st.header("5. Communication des résultats")
    # st.write("""
    # Une fois l'analyse terminée, il est crucial de **communiquer les résultats** de manière claire et convaincante. Cela inclut la rédaction de rapports et la présentation des conclusions aux parties prenantes sous forme de :
    # - **Tableaux de bord interactifs** : Utilisation d'outils comme Power BI, Tableau ou Streamlit pour créer des visualisations dynamiques.
    # - **Rapports** : Rédaction de rapports détaillant les processus d'analyse.
    # - **Présentations** : Synthétiser les résultats sous forme de présentations.
    # """)