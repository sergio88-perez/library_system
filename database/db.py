import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "biblioteca.db")

def conectar():

    conexion = sqlite3.connect(DB_PATH)

    return conexion

def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros(
        codigo INTEGER PRIMARY KEY,
        titulo TEXT,
        autor TEXT,
        prestado INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id_usuario INTEGER PRIMARY KEY,
        nombre TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prestamos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_libro INTEGER,
    id_usuario INTEGER,
    FOREIGN KEY (codigo_libro) REFERENCES libros(codigo),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
    )
    """)

    conexion.commit()
    conexion.close()