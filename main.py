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
        codigo = int(input("Ingrese codigo : "))
        usuario = int(input("Ingrese Id usuario : "))

        prestar_libro(codigo, usuario)

    elif opcion == 4:
        codigo = int(input("Ingrese codigo : "))
        usuario = int(input("Ingrese Id de usuario : "))

        devolver_libro(codigo, usuario)

    elif opcion == 5:
        if len(libros) == 0:
            print("No hay libros registrados")
        
        for libro in libros:
            libro.mostrar_info()

    elif opcion == 6:
        if len(usuarios) == 0:
            print("No hay usuarios registrados")

        for usuario in usuarios:
            usuario.mostrar_info()

    elif opcion == 7:
        print ("Saliendo del sistema")
        break

