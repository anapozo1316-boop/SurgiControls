import streamlit as st
import pandas as pd
from database.db import get_connection

conn = get_connection()

def buscar_instrumental():
    st.title("🔍 Buscar Instrumental")

    busqueda = st.text_input("Buscar")

    if busqueda:

        query = '''
        SELECT * FROM instrumental
        WHERE nombre LIKE ?
        '''

        resultados = pd.read_sql_query(
            query,
            conn,
            params=(f"%{busqueda}%",)
        )

        st.dataframe(
            resultados,
            use_container_width=True
        )
