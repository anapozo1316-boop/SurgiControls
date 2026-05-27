import streamlit as st
from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

def registrar_equipo():
    st.title("🩺 Registrar Equipo")

    with st.form("equipo"):

        nombre = st.text_input(
            "Nombre del equipo"
        )

        especialidad = st.selectbox(
            "Especialidad",
            [
                "Ortopedia",
                "Neurocirugía",
                "Cirugía"
            ]
        )

        guardar = st.form_submit_button(
            "Guardar"
        )

        if guardar:

            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS equipos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    especialidad TEXT
                )
                '''
            )

            cursor.execute(
                '''
                INSERT INTO equipos
                (
                    nombre,
                    especialidad
                )
                VALUES (?, ?)
                ''',
                (
                    nombre,
                    especialidad
                )
            )

            conn.commit()

            st.success("✅ Equipo registrado")
