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

def load_hist_plots(df):

    # Les genres
    df_gender = df[['gender_is_female', 'gender_is_male', 'gender_is_other']].sum()
    labels = ['Femmes', 'Hommes', 'Autres']
    df_gender.index = labels
    
    # Le travail
    df_job = df[['job_is_doctor', 'job_is_engineer', 'job_is_other', 'job_is_student', 'job_is_teacher', 'job_is_unemployed']].sum()
    labels = ['Doctors', 'Engineers', 'Others', 'Students', 'Teachers', 'Unemployed']
    df_job.index = labels

    # Les fumeurs
    df_smokers = pd.DataFrame(
        {'count':[
            df[['is_smoker']].sum().item(),
            df.shape[0] - df[['is_smoker']].sum().item()
        ]},
        index=['Oui', 'Non'])

    # Medication
    df_medication = pd.DataFrame(
        {'count':[
            df[['medication']].sum().item(),
            df.shape[0] - df[['medication']].sum().item()
        ]},
        index=['Oui', 'Non'])
    
    # family history
    df_family_history = pd.DataFrame(
        {'count':[
            df[['family_history']].sum().item(),
            df.shape[0] - df[['family_history']].sum().item()
        ]},
        index=['Oui', 'Non'])

    # recently_chocked
    df_recently_chocked = pd.DataFrame(
        {'count':[
            df[['recently_chocked']].sum().item(),
            df.shape[0] - df[['recently_chocked']].sum().item()
        ]},
        index=['Oui', 'Non'])
    
    # dizziness
    df_dizziness = pd.DataFrame(
        {'count':[
            df[['dizziness']].sum().item(),
            df.shape[0] - df[['dizziness']].sum().item()
        ]},
        index=['Oui', 'Non'])


   # Création de la figure avec un Gridspec
    fig = plt.figure(layout=None, figsize=(10, 15))
    # # Création de la grille pour la première ligne avec un ratio 1:2
    gs = fig.add_gridspec(nrows=4, ncols=6, left=0.1, right=0.9, hspace=0.3, wspace=0.7)

    # Première ligne avec ratio de colonnes 1:2
    ax0 = fig.add_subplot(gs[0, 0:2])
    ax1 = fig.add_subplot(gs[0, 2:6])
    ax2 = fig.add_subplot(gs[1, 0:3])
    ax3 = fig.add_subplot(gs[1, 3:6])
    ax4 = fig.add_subplot(gs[2, 0:3])
    ax5 = fig.add_subplot(gs[2, 3:6])
    ax6 = fig.add_subplot(gs[3, 0:3])
    ax7 = fig.add_subplot(gs[3, 3:6])

    # Mise à jour des paramètres globaux de la police pour la cohérence
    plt.rcParams.update({'font.size': 11,  # Taille des titres des axes
                        'axes.labelsize': 11,  # Taille des labels des axes
                        'xtick.labelsize': 11,  # Taille des labels des ticks X
                        'ytick.labelsize': 11,  # Taille des labels des ticks Y
                        'legend.fontsize': 11})  # Taille de la légende

    # Ajustement des espacements
    plt.subplots_adjust(hspace=1, wspace=0.5)

    # Répartition des genres
    ax0.set_title("Genres")
    sns.barplot(x=df_gender.index, y=df_gender, palette="pastel", ax=ax0)
    ax0.set_xlabel('')
    ax0.set_ylabel('')

    # Répartition du travail
    ax1.set_title("Travail")
    sns.barplot(x=df_job.index, y=df_job, palette="pastel", ax=ax1)
    ax1.set_xlabel('')
    ax1.set_ylabel('')

    # Répartition des fumeurs
    ax2.set_title("Fumeurs")
    sns.barplot(x=df_smokers.index, y=df_smokers['count'], palette="pastel", ax=ax2)
    ax2.set_xlabel('')
    ax2.set_ylabel('')

    # Médication
    ax3.set_title("Personnes sous traitement")
    sns.barplot(x=df_medication.index, y=df_medication['count'], palette="pastel", ax=ax3)
    ax3.set_xlabel('')
    ax3.set_ylabel('')

    # Historique familial
    ax4.set_title("Historique familial")
    sns.barplot(x=df_family_history.index, y=df_family_history['count'], palette="pastel", ax=ax4)
    ax4.set_xlabel('')
    ax4.set_ylabel('')

    # Choc récent
    ax5.set_title("Choc récent")
    sns.barplot(x=df_recently_chocked.index, y=df_recently_chocked['count'], palette="pastel", ax=ax5)
    ax5.set_xlabel('')
    ax5.set_ylabel('')

    # Vertiges en crise
    ax6.set_title("Vertiges en crise")
    sns.barplot(x=df_dizziness.index, y=df_dizziness['count'], palette="pastel", ax=ax6)
    ax6.set_xlabel('')
    ax6.set_ylabel('')


    # Affichage dans Streamlit avec un panneau d'extension
    with st.expander('Voir la répartition'):
        st.pyplot(fig)


def load():
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

    load_hist_plots(df)
