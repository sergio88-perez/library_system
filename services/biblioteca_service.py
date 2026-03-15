from database.db import conectar

def registrar_libro(titulo, autor, codigo):
    conexion = conectar()
    cursor = conexion.cursor()

    # Verificar si el libro ya existe en la base de datos
    existente = cursor.execute(
        "SELECT codigo FROM libros WHERE codigo = ?",
        (codigo,)
    ).fetchone()

    if existente:
        conexion.close()
        raise ValueError("Ya existe un libro con ese código")

    cursor.execute(
        "INSERT INTO libros (codigo, titulo, autor, prestado) VALUES (?, ?, ?, ?)",
        (codigo, titulo, autor, 0)
    )

    conexion.commit()
    conexion.close()
    return "Libro registrado correctamente"

def registrar_usuario(nombre, id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()

    # Verificar si el usuario ya existe en la base de datos
    existente = cursor.execute(
        "SELECT id_usuario FROM usuarios WHERE id_usuario = ?",
        (id_usuario,)
    ).fetchone()

    if existente:
        conexion.close()
        raise ValueError("Ya existe un usuario con ese id")

    cursor.execute(
        "INSERT INTO usuarios (id_usuario, nombre) VALUES (?, ?)",
        (id_usuario, nombre)
    )

    conexion.commit()
    conexion.close()
    return "Usuario registrado correctamente"

def ver_libros():
    conexion = conectar()
    cursor = conexion.cursor()

    # Obtener todos los libros de la base de datos
    filas = cursor.execute("""
        SELECT codigo, titulo, autor, prestado
        FROM libros
        ORDER BY codigo
    """).fetchall()

    conexion.close()
    return [dict(fila) for fila in filas]

def ver_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()

    # Obtener todos los usuarios de la base de datos
    filas = cursor.execute("""
        SELECT id_usuario, nombre
        FROM usuarios
        ORDER BY id_usuario
    """).fetchall()

    conexion.close()
    return [dict(fila) for fila in filas]

def ver_prestamos():
    conexion = conectar()
    cursor = conexion.cursor()

    # Obtener todos los préstamos de la base de datos
    filas = cursor.execute("""
        SELECT p.codigo_libro, l.titulo, p.id_usuario, u.nombre
        FROM prestamos p
        JOIN libros l ON p.codigo_libro = l.codigo
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        ORDER BY p.codigo_libro
    """).fetchall()

    conexion.close()
    return [dict(fila) for fila in filas]

def prestar_libro(codigo_libro, id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()

    # Verificar si el libro existe
    libro = cursor.execute(
        "SELECT * FROM libros WHERE codigo = ?",
        (codigo_libro,)
    ).fetchone()

    if not libro:
        conexion.close()
        raise ValueError("Libro no encontrado")

    # Verificar si el usuario existe
    usuario = cursor.execute(
        "SELECT * FROM usuarios WHERE id_usuario = ?",
        (id_usuario,)
    ).fetchone()

    if not usuario:
        conexion.close()
        raise ValueError("Usuario no encontrado")

    if libro["prestado"] == 1:
        conexion.close()
        raise ValueError("El libro ya está prestado")

    cursor.execute(
        "INSERT INTO prestamos (codigo_libro, id_usuario) VALUES (?, ?)",
        (codigo_libro, id_usuario)
    )

    cursor.execute(
        "UPDATE libros SET prestado = 1 WHERE codigo = ?",
        (codigo_libro,)
    )

    conexion.commit()
    conexion.close()
    return "Libro prestado correctamente"

def devolver_libro(codigo_libro):
    conexion = conectar()
    cursor = conexion.cursor()

    # Verificar si el libro está prestado
    prestamo = cursor.execute(
        "SELECT * FROM prestamos WHERE codigo_libro = ?",
        (codigo_libro,)
    ).fetchone()

    if not prestamo:
        conexion.close()
        raise ValueError("Ese libro no está prestado")

    cursor.execute(
        "DELETE FROM prestamos WHERE codigo_libro = ?",
        (codigo_libro,)
    )

    cursor.execute(
        "UPDATE libros SET prestado = 0 WHERE codigo = ?",
        (codigo_libro,)
    )

    conexion.commit()
    conexion.close()
    return "Libro devuelto correctamente"