import streamlit as st
from streamlit_option_menu import option_menu

from dashboard.resumen import create_resume
from dashboard.alcances import create_alcance
from dashboard.edificios import create_edificio
from dashboard.vehiculos import create_vehiculo
from dashboard.consumos import create_consumo

from data_recolection.edificios import create_sub_edificio
from data_recolection.empleados import create_sub_empleado
from data_recolection.importacion import create_sub_importacion
from data_recolection.proveedores import create_sub_proveedores
from data_recolection.vehiculos import create_sub_vehiculo
from data_recolection.viajes import create_sub_viaje

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Carbono",
    page_icon=":fire:", 
    layout="wide" # Emoji de un trozo de carbón
)

# Título de la aplicación
st.title("Calculadora de Carbono")

# CSS para el control de versiones en el pie del menú lateral
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            color: grey;
        }
        .menu-title {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Menú lateral
with st.sidebar:
    # st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/Coal_anthracite.jpg", width=100)
    submenu = None
    menu = option_menu("Dashboard", ["Resumen", "Alcances", "Edificios", "Vehiculos", "Consumos"],
                       icons=['grid', 'filter', 'building', 'car-front', 'plug'],
                       menu_icon="cast", default_index=0)

    submenu = option_menu("Recolección de datos", ["Recoleccion de datos","Edificios", "Vehiculos", "Empleados", "Viajes de negocios", "Proveedores", "Importacion en masa"],
                          icons=["",'building', 'car-front', 'person', 'briefcase', 'truck', 'cloud-upload'],
                          menu_icon="upload", default_index=0)
    
    st.markdown('<div class="footer">v0.0.1 - Álvaro</div>', unsafe_allow_html=True)


# Carga de datos del menú de dashboard
if menu == "Resumen":
    create_resume()
elif menu == "Alcances":
    create_alcance()
elif menu == "Edificios":
    create_edificio()
elif menu == "Vehiculos":
    create_vehiculo()
elif menu == "Consumos":
    create_consumo()


# Carga de datos del menú de recoleccion de datos
if submenu == "Edificios":
    create_sub_edificio()
elif submenu == "Vehiculos":
    create_sub_vehiculo()
elif submenu == "Empleados":
    create_sub_empleado()
elif submenu == "Viajes de negocios":
    create_sub_viaje()
elif submenu == "Proveedores":
    create_sub_proveedores()
elif submenu == "Importacion en masa":
    create_sub_importacion()

st.markdown('<div class="footer">v0.0.1 - Álvaro</div>', unsafe_allow_html=True)
