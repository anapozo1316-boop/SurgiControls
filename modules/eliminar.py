import streamlit as st
import pandas as pd
from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

def eliminar_instrumental():
    st.title("🗑️ Eliminar")

    instrumental = pd.read_sql_query(
        "SELECT * FROM instrumental",
        conn
    )

    if len(instrumental) == 0:
        st.warning("No hay instrumental registrado")
        return

    seleccion = st.selectbox(
        "Seleccionar",
        instrumental["nombre"]
    )

    instrumento_id = int(
        instrumental[
            instrumental["nombre"] == seleccion
        ]["id"].values[0]
    )

    if st.button("Eliminar"):

        cursor.execute(
            '''
            DELETE FROM instrumental
            WHERE id = ?
            ''',
            (
                instrumento_id,
            )
        )

        conn.commit()

        st.success("✅ Eliminado")
