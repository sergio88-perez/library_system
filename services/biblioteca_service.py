from database.db import conectar
from models.libro import Libro
from models.usuario import Usuario

libros = []
usuarios = []

def registrar_libro(titulo, autor, codigo):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO libros VALUES (?, ?, ?, ?)",
        (codigo, titulo, autor, 0)
    )

    conexion.commit()
    conexion.close()

    print("Libro registrado")

def registrar_usuario(nombre, id_usuario):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO usuarios VALUES (?, ?)",
        (id_usuario, nombre)
    )

    conexion.commit()
    conexion.close()

    print("Usuario registrado correctamente")

def ver_libros():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libros")

    libros = cursor.fetchall()

    for libro in libros:

        estado = "Prestado" if libro[3] == 1 else "Disponible"

        print(libro[1], "-", estado)

    conexion.close()

def buscar_libro(codigo):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM libros WHERE codigo = ?",
        (codigo,)
    )

    libro = cursor.fetchone()

    conexion.close()

    return libro
        
def buscar_usuario(id_usuario):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE id_usuario = ?",
        (id_usuario,)
    )

    usuario = cursor.fetchone()

    conexion.close()

    return usuario

def prestar_libro(codigo):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE libros SET prestado = 1 WHERE codigo = ?",
        (codigo,)
    )

    conexion.commit()
    conexion.close()

    print("Libro prestado")

def devolver_libro(codigo):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE libros SET prestado = 0 WHERE codigo = ?",
        (codigo,)
    )

    conexion.commit()
    conexion.close()

    print("Libro devuelto correctamente")

