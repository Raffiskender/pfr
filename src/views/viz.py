import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_view():
    st.title('Visualisation')
    st.write(
    '''
    Ci dessous quelques visualisations intéressante
    ''')

    df = pd.read_csv('./src/assets/data/anxiety_attack_dataset.csv')

    st.subheader("Tables de correlation")
    st.write('choisissez 2 données à corréler :')
    col1, col2 = st.columns(2)
    with col1:
        one = st.radio('Première valeur :', df.select_dtypes(include=['number']).columns)
    with col2:
        two = st.radio('Seconde valeur :', df.select_dtypes(include=['number']).columns)
    # with col3:
    #     one = st.radio('Première valeur :', df.columns)

    st.write('1 :', one)
    st.write('2 :', two)

    corr = df[one].corr(df[two])

    fig = plt.figure(figsize=(8,6))

    sns.scatterplot(data=df, x=one, y=two)
    
    plt.title(f"Corrélation entre X et Y : {corr:.2f}")
    st.pyplot(fig)


    st.subheader("autres visualisations")

    df_ages = df['Age'].value_counts().sort_index(ascending=True)
    st.dataframe(df_ages)
    the_range = st.slider('Ages', min_value=df_ages.index.min(), max_value=df_ages.index.max(), value=(df_ages.index.min(), df_ages.index.max()))
    st.write(the_range)
    fig=plt.figure(figsize=(12,8))

