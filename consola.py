from database.db import crear_tablas
from services.biblioteca_service import (
    registrar_libro,
    registrar_usuario,
    ver_libros,
    ver_usuarios,
    ver_prestamos,
    prestar_libro,
    devolver_libro
)
from utils.menu import mostrar_menu

def ejecutar_menu():
    crear_tablas()

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        try:
            if opcion == 1:
                titulo = input("Ingrese título: ")
                autor = input("Ingrese autor: ")
                codigo = int(input("Ingrese código: "))
                print(registrar_libro(titulo, autor, codigo))

            elif opcion == 2:
                nombre = input("Ingrese nombre de usuario: ")
                id_usuario = int(input("Ingrese id del usuario: "))
                print(registrar_usuario(nombre, id_usuario))

            elif opcion == 3:
                codigo = int(input("Código del libro: "))
                usuario = int(input("ID del usuario: "))
                print(prestar_libro(codigo, usuario))

            elif opcion == 4:
                codigo = int(input("Código del libro: "))
                print(devolver_libro(codigo))

            elif opcion == 5:
                libros = ver_libros()
                for libro in libros:
                    estado = "Prestado" if libro["prestado"] == 1 else "Disponible"
                    print(f'{libro["codigo"]} - {libro["titulo"]} - {libro["autor"]} - {estado}')

            elif opcion == 6:
                usuarios = ver_usuarios()
                for usuario in usuarios:
                    print(f'{usuario["id_usuario"]} - {usuario["nombre"]}')

            elif opcion == 7:
                prestamos = ver_prestamos()
                for prestamo in prestamos:
                    print(
                        f'Libro: {prestamo["codigo_libro"]} - {prestamo["titulo"]} | '
                        f'Usuario: {prestamo["id_usuario"]} - {prestamo["nombre"]}'
                    )

            elif opcion == 8:
                print("Saliendo del sistema")
                break

            else:
                print("Opción inválida")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    ejecutar_menu()