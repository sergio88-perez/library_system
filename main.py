from database.db import crear_tablas
from services.biblioteca_service import *
from utils.menu import mostrar_menu

crear_tablas()

while True:

    mostrar_menu()
    opcion = int(input ("Seleccione una opción: "))

    if opcion == 1:
        titulo = input("Ingresar titulo : ")
        autor = input ("Ingrese nombre de autor : ")
        codigo = int(input ("Ingrese codigo : "))

        registrar_libro (titulo, autor, codigo)

    elif opcion == 2:
        usuario = input ("Ingresar nombre de usuario : ")
        id_usuario = int(input("Ingrese Id de usuario : "))

        registrar_usuario (usuario, id_usuario)

    elif opcion == 3:

        codigo = int(input("Codigo del libro: "))
        usuario = int(input("ID del usuario: "))

        prestar_libro(codigo, usuario)

    elif opcion == 4:
        codigo = int(input("Codigo del libro: "))

        devolver_libro(codigo)

    elif opcion == 5:
        ver_libros()

    elif opcion == 6:
        ver_usuarios()

    elif opcion == 7:
        ver_prestamos()

    elif opcion == 8:
        print ("Saliendo del sistema")
        break

