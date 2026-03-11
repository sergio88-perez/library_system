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

    cursor.execute("""
    SELECT libros.codigo, libros.titulo, usuarios.nombre
    FROM libros
    LEFT JOIN prestamos ON libros.codigo = prestamos.codigo_libro
    LEFT JOIN usuarios ON prestamos.id_usuario = usuarios.id_usuario
    """)

    libros = cursor.fetchall()

    if len(libros) == 0:
        print("No hay libros registrados")

    for libro in libros:

        codigo = libro[0]
        titulo = libro[1]
        usuario = libro[2]

        if usuario:
            estado = f"Prestado a {usuario}"
        else:
            estado = "Disponible"

        print("Codigo:", codigo)
        print("Titulo:", titulo)
        print("Estado:", estado)
        print("----------------")

    conexion.close()

def ver_usuarios():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    if len(usuarios) == 0:
        print("No hay usuarios registrados")

    for usuario in usuarios:

        print("ID:", usuario[0])
        print("Nombre:", usuario[1])
        print("------------------")

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

def prestar_libro(codigo_libro, id_usuario):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT prestado FROM libros WHERE codigo = ?",
        (codigo_libro,)
    )

    libro = cursor.fetchone()

    if libro is None:
        print("Libro no encontrado")

    elif libro[0] == 1:
        print("Libro ya prestado")

    else:

        cursor.execute(
            "UPDATE libros SET prestado = 1 WHERE codigo = ?",
            (codigo_libro,)
        )

        cursor.execute(
            "INSERT INTO prestamos (codigo_libro, id_usuario) VALUES (?, ?)",
            (codigo_libro, id_usuario)
        )

        conexion.commit()

        print("Libro prestado correctamente")

    conexion.close()

def devolver_libro(codigo_libro):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE libros SET prestado = 0 WHERE codigo = ?",
        (codigo_libro,)
    )

    cursor.execute(
        "DELETE FROM prestamos WHERE codigo_libro = ?",
        (codigo_libro,)
    )

    conexion.commit()

    print("Libro devuelto")

    conexion.close()

def ver_prestamos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT usuarios.nombre, libros.titulo
    FROM prestamos
    JOIN usuarios ON prestamos.id_usuario = usuarios.id_usuario
    JOIN libros ON prestamos.codigo_libro = libros.codigo
    """)

    prestamos = cursor.fetchall()

    if len(prestamos) == 0:
        print("No hay prestamos")

    for p in prestamos:
        print(p[0], "tiene el libro:", p[1])

    conexion.close()

