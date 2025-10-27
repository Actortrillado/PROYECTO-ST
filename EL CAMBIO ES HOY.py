#importa streamlit
import streamlit as st
#le agrega el titulo a la pagina
st.set_page_config(
    page_title="TU CUERPO IDEAL",
    page_icon=":bomb"
    ) 
# Es una lista de páginas.
pg = st.navigation(["Proyecto ST.py", "imc_app.py", "Creadores.py"])

pg.run()



