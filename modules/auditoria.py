import streamlit as st
import pandas as pd
from database.db import get_connection

conn = get_connection()

def ver_auditoria():
    st.title("📜 Auditoría")

    try:
        auditoria = pd.read_sql_query(
            "SELECT * FROM auditoria",
            conn
        )

        st.dataframe(
            auditoria,
            use_container_width=True
        )

    except:
        st.info("No hay registros de auditoría")
