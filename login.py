import streamlit as st
import json


def load_credentials(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['credenciales']


def login(filepath):
    st.title("Iniciar Sesion")
    credentials=load_credentials(filepath)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Iniciar Sesion"):
        for cred in credentials:
            if cred['user'] == username and cred['pass'] == password:
                st.session_state["logged_in"] = True
                st.success("Inicio de sesión correcto")
                st.experimental_rerun()  # Redirige a la página principal
            else:
                st.error("Contraseña o usuario invalido")
                continue
                
def logout():
    st.session_state["logged_in"] = False
    st.success("Sesion cerrada correctamente")
    st.experimental_rerun()  # Redirige a la página de login
