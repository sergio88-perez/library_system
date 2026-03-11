class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def mostrar_info (self):
        print (f"Usuario : {self.nombre}")
        print (f"Id Usuario : {self.id_usuario}")
        print (f"Libros prestado : {len(self.libros_prestados)}")


        