#===========================================================
# Importation des librairies
#===========================================================
import pandas as pd
import numpy as np
import streamlit as st
import time
import random
random.seed(123)

#==========================================================
# Construction des elements de la page
#==========================================================



st.markdown("""<h2 style="text-align: left; color: darkblue;
            text-decoration: underline;">About Us</h2>""",
            unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True) #saut de ligne

col1, col2 = st.columns([3, 2])
col2.image("images/logo.png")

text1 = """Créé le 1er Octobre 2021, SDA est spécialisé dans la fourniture 
            de services Cloud, d'IA générative, de Machine Learning et 
            de construction d'infrastructures de données. Nous possédons 
            des experts et spécialistes métiers dans: la Banque-finance, 
            l'Assurance, la Santé et la technologie informatique. Notre modèle business
            innovant s'appuie principalement sur la capitalisation de l'expérience
            client, ce qui nous permet d'améliorer continuellement nos services et 
            produits fournis."""

col1.markdown(f"""<div style="text-align: justify; color: darkblue; font-size: 20px;"
                >{text1}</div>""", unsafe_allow_html=True
                )

st.markdown("<br>", unsafe_allow_html=True)  # Saut de ligne 

st.markdown("""<h2 style="text-align: center; 
                color: darkblue;
                ">Expertises Métiers</h2>""", 
                unsafe_allow_html=True
                )

col1, col2, col3, col4 = st.columns(4)
col1.image("images/bank.jpg")
col1.markdown(f"""<div style="text-align: justify;color: darkblue;
            ">BANQUE</div>""",unsafe_allow_html=True)
col2.image("images/economie.jpg")
col2.markdown(f"""<div style="text-align: justify;color: darkblue;
            ">ASSURANCE</div>""",unsafe_allow_html=True)
col3.image("images/sante.jpg")
col3.markdown(f"""<div style="text-align: justify;color: darkblue;
            ">SANTE</div>""",unsafe_allow_html=True)
col4.image("images/technologie.png")
col4.markdown(f"""<div style="text-align: justify;color: darkblue;
            ">TECHNOLOGIE</div>""",unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # Saut de ligne 

st.markdown("""<h2 style="text-align: center; color: darkblue;
                ">Présentation </h2>""", 
                unsafe_allow_html=True
                )

col = st.columns(1)[0]


col.markdown(
    """
    <div style="text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: rgba(0, 128, 250, 0.5);">
        <p style="font-size: 16px; color: #333;">
            Bonjour, je suis Fanta Sanogo, actuellement en formation de data analyst à l'université Paris 1 Panthéon-Sorbonne niveau Master 1.
        </p> 
        <p style="font-size: 16px; color: #333;">
            Ce projet combine plusieurs compétences (Python, SQL, Streamlit, statistique descriptive, gestion de projet, machine learning, data management,
            text mining) pour faciliter la prise de décisions stratégiques.
        </p>
        <p style="font-size: 16px; color: #333;">
            Mon objectif est d'intégrer un groupe, une start-up ou une entreprise où je pourrais, grâce à mon expertise et mes compétences, contribuer à
            accroître leur notoriété.
        </p>
        <p style="font-size: 16px; color: #333;">
            Je souhaite rejoindre une équipe dynamique dans laquelle je pourrais être une force d'exécution, contribuant à atteindre les objectifs fixés.
        </p>
        <p style="font-size: 16px; color: #333;">
            Naviguez entre les différents onglets pour découvrir les pages de mon projet Streamlit.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)



