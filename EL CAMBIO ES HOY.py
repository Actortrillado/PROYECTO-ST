import streamlit as st

st.set_page_config(
    page_title="TU CUERPO IDEAL",
    page_icon=":bomb"
    ) 
# Es una lista de páginas.
pg = st.navigation(["Proyecto ST.py", "imc_app.py", "creadores.py"])

pg.run()

