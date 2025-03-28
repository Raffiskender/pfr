import streamlit as st
from io import StringIO
import pandas as pd
import numpy as np
import random as rnd
from src.models.data_model import DataModel
# visualization
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3 as sqlite3

def load_box_plots(df):
    # Calculer le nombre de colonnes et de lignes pour les subplots
    n_cols = 2  # Nombre de colonnes dans la grille
    n_rows = (len(df.select_dtypes(include=['number']).columns) + n_cols - 1) // n_cols  # Calcul dynamique du nombre de lignes

    # Créer une figure avec des subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 15))

    # Aplatir l'array des axes pour faciliter l'indexation dans la boucle
    axes = axes.flatten()

    # Boucle pour créer un boxplot pour chaque colonne numérique dans le DataFrame
    for i, column in enumerate(df.select_dtypes(include=['number']).columns):
        sns.boxplot(x=df[column], ax=axes[i])
        axes[i].set_title(f"Boxplot {column}")

    # Ajuster les espaces entre les subplots
    plt.tight_layout()

    # Afficher dans Streamlit
    with st.expander('Voir la répartition'):
        st.pyplot(fig)

def load_pie_plots(df):

    # Les genres
    df_gender = df[['gender_is_female', 'gender_is_male', 'gender_is_other']].sum()
    # Le travail
    df_job = df[['job_is_doctor', 'job_is_engineer', 'job_is_other', 'job_is_student', 'job_is_teacher', 'job_is_unemployed']].sum()

    # Les fumeurs
    df_smokers = pd.DataFrame(
        {'count':[
            df[['is_smoker']].sum(),
            df.shape[0] - df[['is_smoker']].sum()
        ]},
        index=['Yes', 'No'])
    
    # Medication
    df_medication = pd.DataFrame(
        {'count':[
            df[['medication']].sum(),
            df.shape[0] - df[['medication']].sum()
        ]},
        index=['Yes', 'No'])
    
    # family history
    df_family_history = pd.DataFrame(
        {'count':[
            df[['family_history']].sum(),
            df.shape[0] - df[['family_history']].sum()
        ]},
        index=['Yes', 'No'])
    
    # recently_chocked
    df_recently_chocked = pd.DataFrame(
        {'count':[
            df[['recently_chocked']].sum(),
            df.shape[0] - df[['recently_chocked']].sum()
        ]},
        index=['Yes', 'No'])
    
    # dizziness
    df_dizziness = pd.DataFrame(
        {'count':[
            df[['dizziness']].sum(),
            df.shape[0] - df[['dizziness']].sum()
        ]},
        index=['Yes', 'No'])


    fig, axes = plt.subplots(4, 2, figsize=(10, 15))

    plt.rcParams.update({'font.size':   11,    # Taille des titres des axes
                     'axes.labelsize':  11,          # Taille des labels des axes
                     'xtick.labelsize': 11,         # Taille des labels des ticks X
                     'ytick.labelsize': 11,         # Taille des labels des ticks Y
                     'legend.fontsize': 11})        # Taille de la légende

    plt.subplots_adjust(hspace=1, wspace=0.5)

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
    
    # Répartition des genres
    axes[0, 0].set_title("Genres")
    labels = ['Female', 'Male', 'Other']
    axes[0, 0].pie(df_gender, labels=labels, colors=colors, autopct='%1.1f%%')

    # Répartition du travail
    axes[0, 1].set_title("Travail")
    labels = ['Doctors', 'Engineers', 'Others', 'Students', 'Teachers', 'Unemployed']
    axes[0, 1].pie(df_job, labels=labels, colors=colors, autopct='%1.1f%%')
   
    # Répartition des fumeurs
    axes[1, 0].set_title("Fumeurs")
    labels = ['Oui', 'Non']
    axes[1, 0].pie(df_smokers['count'], labels=labels, colors=colors, autopct='%1.1f%%')

    # Medication
    axes[1, 1].set_title("Personnes sous traitement")
    labels = ['Oui', 'Non']
    axes[1, 1].pie(df_medication['count'], labels=labels, colors=colors, autopct='%1.1f%%')

    # family history
    axes[2, 0].set_title("Historique familial")
    labels = ['Oui', 'Non']
    axes[2, 0].pie(df_family_history['count'], labels=labels, colors=colors, autopct='%1.1f%%')
   
    # recently chocked
    axes[2, 1].set_title("Choc récent")
    labels = ['Oui', 'Non']
    axes[2, 1].pie(df_recently_chocked['count'], labels=labels, colors=colors, autopct='%1.1f%%')

    # dizziness
    axes[3, 0].set_title("Vertiges en crise")
    labels = ['Oui', 'Non']
    axes[3, 0].pie(df_dizziness['count'], labels=labels, colors=colors, autopct='%1.1f%%')

    plt.tight_layout()

    with st.expander('Voir la répartition'):
        st.pyplot(fig)



def load_view():
    st.title('Analyse exploratoire des données (EDA)')
    st.markdown(
    '''
    > L'analyse exploratoire des données (EDA) consiste à comprendre les ensembles de données en résumant leurs principales caractéristiques, souvent en les représentant visuellement. [...] Grâce au processus d'EDA, nous pouvons formuler l'énoncé du problème ou la définition de notre jeu de données, ce qui est essentiel. *[source : Kaggle]*
    ''')

    st.header('Présentation des données')

    st.write('Dans un premier temps, nous allons extraire les données de la base de donnée et le mettre en forme dans un dataframe. Ce dernier est présent ci-dessous.')
    
    with DataModel() as db:
        df = db.create_dataframe()
    
    with st.expander('voir les données'):
        st.dataframe(df)

    st.header('Préparation')
    
    st.write(f'''Comme elles sortent de la base de donnée, elles ne sont pas formatées :''')
    buffer = StringIO()
    df.info(buf=buffer)
    infos = buffer.getvalue()
    with st.expander('La sorite de df.info() :'):
        st.code(infos)
    
    st.write('On a de la chance, on n\'a pas de dates dans le dataframe. Cependant, certaines colonnes binaires sont devenues des integers (parce que Sqlite ne gère pas les booléens). On va donc les parser en booléens avec ce code :')
    st.code('''
        for column in df.columns:
            if df[column].dtype == 'int64' and df[column].max() == 1 and df[column].min() == 0:
                df[column] = df[column].astype(bool)
    ''')
    for column in df.columns:
        if df[column].dtype == 'int64' and df[column].max() == 1 and df[column].min() == 0:
            df[column] = df[column].astype(bool)
    buffer = StringIO()
    df.info(buf=buffer)
    infos = buffer.getvalue()

    with st.expander('La nouvelle sortie de df.info()'):
        st.code(infos)    

    st.header('Valeurs incohérentes')
    st.write('Les graphiques ci-dessous nous indiqueront si nous avons des valeurs incohérentes dans notre df')
    load_box_plots(df)

    st.write('Manifestement il ne semble pas y avoir de valeurs incohérentes. Du reste, la répartition sur ces colonnes semble correcte.')

    st.header('Répartitions')
    st.write('Nous avons pu voir la répartition via les box-plots sur les colonnes à chiffres. Voyons à présent celle sur les colonnes binaires')

    load_pie_plots(df)
