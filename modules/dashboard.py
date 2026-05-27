import streamlit as st
import pandas as pd
from database.db import get_connection

conn = get_connection()

def dashboard():
    st.title("🏥 Dashboard")

    instrumental = pd.read_sql_query(
        "SELECT * FROM instrumental",
        conn
    )

    equipos = pd.read_sql_query(
        "SELECT * FROM equipos",
        conn
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Instrumental",
        len(instrumental)
    )

    col2.metric(
        "Equipos",
        len(equipos)
    )

    st.dataframe(
        instrumental,
        use_container_width=True
    )
