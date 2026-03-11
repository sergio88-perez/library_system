class Libro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.prestado = False

    def prestar (self):
        if not self.prestado:
            self.prestado = True
            print ("El libro fue prestado correctamente")

        else:
            print ("El libro se encuentra prestado")

    def devolver (self):
        if self.prestado:
            self.prestado = False
            print ("El libro fue devuelto correctamente")

        else:
            print ("El libro no se encuentra prestado")

    def mostrar_info (self):
        estado = "Prestado" if self.prestado else "Disponible"
        print (f"Titulo : {self.titulo}")
        print (f"Autor : {self.autor}")
        print (f"Codigo : {self.codigo}")
        print (f"Estado : {estado}")

    pass

    