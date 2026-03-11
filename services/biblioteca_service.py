from models.libro import Libro
from models.usuario import Usuario

libros = []
usuarios = []

def registrar_libro (titulo, autor, codigo):
    libro = Libro(titulo, autor, codigo)
    libros.append(libro)
    print ("libro registrado correctamente")

def registrar_usuario (nombre, id_usuario):
    usuario = Usuario (nombre, id_usuario)
    usuarios.append(usuario)
    print ("Usuario registrado correctamente")

def buscar_libro (codigo):
    for libro in libros:
        if libro.codigo == codigo:
            return libro
    return None
        
def buscar_usuario (id_usuario):
    for usuario in usuarios:
        if usuario.id_usuario == id_usuario:
            return usuario
    return None

def prestar_libro (codigo_libro, id_usuario):
    libro = buscar_libro (codigo_libro)
    usuario = buscar_usuario (id_usuario)
    if libro and usuario:
        if not libro.prestado:
            libro.prestar()
            usuario.libros_prestados.append(libro)
        else:
            print ("El libro ya esta prestado")
    else:
        print ("Libro o usuario no encontrado")

def devolver_libro (codigo_libro, id_usuario):
    libro = buscar_libro (codigo_libro)
    usuario = buscar_usuario (id_usuario)
    if libro and usuario:
        if libro in usuario.libros_prestados:
            libro.devolver()
            usuario.libros_prestados.remove(libro)
        else:
            print ("El usuario no tiene ese libro")
    else:
        print ("Libro o usuario no encontrado")

