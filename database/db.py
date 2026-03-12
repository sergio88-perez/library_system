import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "biblioteca.db"

def conectar():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        codigo INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        prestado INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prestamos (
        codigo_libro INTEGER,
        id_usuario INTEGER,
        FOREIGN KEY (codigo_libro) REFERENCES libros(codigo),
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    )
    """)

    conexion.commit()
    conexion.close()