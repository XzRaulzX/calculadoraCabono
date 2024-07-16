import streamlit as st
from login import login
from main import main_page


st.set_page_config(
page_title="Calculadora de Carbono",
page_icon=":fire:", 
layout="wide" # Emoji de un trozo de carbón
)

# Inicializa el estado de sesión si no existe
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main_page()
else:
    login("./data/credenciales.json")
