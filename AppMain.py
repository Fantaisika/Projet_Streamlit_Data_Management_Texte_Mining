#===========================================================
# Importation des librairies
#===========================================================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import cufflinks as cf
import streamlit as st
import time
import random
random.seed(123)

#==========================================================
# Configuration de la page streamlit 
#==========================================================
st.set_page_config(
    page_title="Credit Card Dashboards",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state = "expanded"
)

#==========================================================
#=========================================================
#chargement des fichiers depuis google drive
#===============================================
# Dictionnaire pour stocker les liens des fichiers CSV
file_links = {
    "credit_card_transactions.csv": "https://drive.google.com/uc?id=15EVo4VGeqrZl2BwnwMEypd52lFGELn79",
    "financial_clean.csv": "https://drive.google.com/uc?id=1IsYVfxiNiO-VykQYO1P_-_jhAKI_MztL",
    "fraud_data.csv": "https://drive.google.com/uc?id=1hmHY7yyb6ZhXW9nOVnWAbRRCmpmoPSCI",
    "individual_data_a.csv": "https://drive.google.com/uc?id=1kAKzlJb6fH4zemD82NIp-embIXvdLku3",
    "individual_data_b.csv": "https://drive.google.com/uc?id=1qKMgGGFADyLpsnsL74IqKDcIeWDvhp4A",
    "metadonees1.csv": "https://drive.google.com/uc?id=1bSS-7o9_Az-9sNbxEz7cREkD91W1TH_v",
    "metadonnees2.csv": "https://drive.google.com/uc?id=1-Eo_E8dCjUInsuxk-1OjgycwjN5nggjd",
}

@st.cache_data
def load_data(file_url):
    try:
        return pd.read_csv(file_url)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return None
# Execution des pages
#==========================================================

# Structure des pages de l'application web
pages = [
    st.Page("AboutUs.py", title="Home"),
    st.Page("MetaDonnees.py", title="MétaDonnées"),
    st.Page("StatsDescriptifs.py", title="Statistiques Descriptives"),
    st.Page("TableauBordIndividu.py", title="Suivi des KPIs Individus"),
    st.Page("GeoAnalysisCharts.py", title="GeoAnalyse"),
    st.Page("MacroAnalyseCharts.py", title="MacroAnalyse"),
    st.Page("WordCloud.py", title="WordCloud"),
    st.Page("MachineLearning.py", title="Machine Learning"),
]

pg = st.navigation(pages)
pg.run()
