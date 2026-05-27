import streamlit as st
from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

def registrar_instrumental():
    st.title("➕ Registrar Instrumental")

    with st.form("instrumental"):

        nombre = st.text_input("Nombre")

        tipo = st.selectbox(
            "Tipo",
            [
                "Pinza",
                "Separador",
                "Tijera",
                "Óptica"
            ]
        )

        cantidad = st.number_input(
            "Cantidad",
            min_value=1
        )

        ubicacion = st.text_input("Ubicación")

        guardar = st.form_submit_button("Guardar")

        if guardar:

            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS instrumental (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    tipo TEXT,
                    cantidad_total INTEGER,
                    cantidad_disponible INTEGER,
                    estado TEXT,
                    ubicacion TEXT
                )
                '''
            )

            cursor.execute(
                '''
                INSERT INTO instrumental
                (
                    nombre,
                    tipo,
                    cantidad_total,
                    cantidad_disponible,
                    estado,
                    ubicacion
                )
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (
                    nombre,
                    tipo,
                    cantidad,
                    cantidad,
                    "Disponible",
                    ubicacion
                )
            )

            conn.commit()

            st.success("✅ Instrumental registrado")
