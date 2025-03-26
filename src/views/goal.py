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

    # Objectif 1 : EDA - Exploratory Data Analysis
    st.header("1. Analyse exploratoire des données (EDA)")
    st.write("""
    L'**analyse exploratoire des données** (EDA) est une première étape essentielle pour tout projet de Data Analyse. Elle consiste à comprendre les caractéristiques des données avant de procéder à des analyses plus approfondies. Cette étape permet de découvrir des **relations**, des **tendances**, des **anomalies** et des **patterns** qui peuvent guider les étapes suivantes.

    Les techniques courantes utilisées dans l'EDA incluent :
    - **Détection des valeurs manquantes ou abérantes** : Identification et traitement des valeurs aberrantes ou manquantes.
    - **Statistiques descriptives** : Calcul de mesures de tendance centrale (moyenne, médiane) et de dispersion (écart-type, quartiles) pour obtenir un aperçu des données.
    - **Visualisation des données** : Utilisation de graphiques (histogrammes, boxplots, scatter plots, etc.) pour observer la distribution des variables et les relations entre elles.
    """)

    # Objectif 2 : Préparation des données
    st.header("2. Préparation et nettoyage des données")
    st.write("""
    Une fois l'EDA réalisée, nous allons préparer les données pour les analyses suivantes. Le nettoyage des données est une phase cruciale où l'on s'assure que les données sont cohérentes, complètes et prêtes pour l'analyse.

    Cela inclut :
    - **Traitement des valeurs manquantes** : Remplir, imputer ou supprimer les valeurs manquantes en fonction du contexte.
    - **Correction des incohérences** : Identifier et rectifier les erreurs de saisie ou les doublons.
    - **Normalisation et transformation des données** : Mise à l'échelle des variables, conversion des formats de données, et agrégation des données si nécessaire.
    """)

    # Objectif 3 : Analyse descriptive et statistique
    st.header("3. Analyse descriptive et statistique")
    st.write("""
    L'analyse descriptive permet de résumer les principales caractéristiques des données. En plus des statistiques de base (moyennes, médianes, écarts-types), l'analyse statistique plus avancée permet de tirer des conclusions et de poser des hypothèses.

    Cela comprend :
    - **Calcul des corrélations** : Mesurer les relations entre les différentes variables du jeu de données.
    - **Tests statistiques** : Réaliser des tests de significativité pour vérifier des hypothèses.
    """)

    # Objectif 4 : Visualisation des données
    st.header("4. Visualisation des données")
    st.write("""
    La **visualisation des données** est essentielle pour comprendre et communiquer les résultats des analyses de manière claire et efficace. Cela permet de présenter des informations complexes de manière intuitive et accessible.

    Les visualisations les plus courantes sont :
    - **Graphiques univariés** : Histogrammes, bar charts, box plots pour étudier la distribution d'une seule variable.
    - **Graphiques bivariés** : Scatter plots, heatmaps pour observer les relations entre deux variables.
    """)

    # Objectif 5 : Communication des résultats
    st.header("5. Communication des résultats")
    st.write("""
    Une fois l'analyse terminée, il est crucial de **communiquer les résultats** de manière claire et convaincante. Cela inclut la rédaction de rapports et la présentation des conclusions aux parties prenantes sous forme de :
    - **Tableaux de bord interactifs** : Utilisation d'outils comme Power BI, Tableau ou Streamlit pour créer des visualisations dynamiques.
    - **Rapports** : Rédaction de rapports détaillant les processus d'analyse.
    - **Présentations** : Synthétiser les résultats sous forme de présentations.
    """)