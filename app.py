import streamlit as st
import requests
import numpy as np

st.set_page_config(layout="wide")
st.title("Prédiction de Prêt Bancaire")
API_URL = "apigrantcredit2-ddccfad9cpc3akcx.westeurope-01.azurewebsites.net"

# Création des champs de saisie
col1, col2, col3 = st.columns(3)
