import streamlit as st
import pandas as pd
def create_sub_vehiculo():
    dataframe = pd.DataFrame([["Vehículo", "8137KZX", "07/05/2024", "14/06/2024", "5km", ""]])

    # Asignar los nombres de las columnas al DataFrame
    dataframe.columns = ["Tipo", "Vehículo", "Fecha de inicio", "Fecha de fin", "Consumo", "Emisiones"]

    # Mostrar la tabla en Streamlit
    st.table(dataframe)

