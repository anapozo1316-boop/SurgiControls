import os
import sqlite3

def get_connection():
    # Crear carpeta si no existe
    os.makedirs("data", exist_ok=True)

    db_path = os.path.join("data", "surgicontrol.db")

    conn = sqlite3.connect(
        db_path,
        check_same_thread=False
    )

    return conn
