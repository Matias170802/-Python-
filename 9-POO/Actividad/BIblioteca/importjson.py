import json

class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año_publicacion})"
    
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []

    def mostrar_libros_disponibles(self):
        if not self.libros_disponibles:
            print("No hay libros disponibles en esta biblioteca.")
        else:
            print("Libros disponibles en la biblioteca:")
            print("-------------------------------------------------------------------------------------------")
            for libro in self.libros_disponibles:
                print(libro)

    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Se ha prestado el libro '{titulo}'")
                return
        print(f"El libro '{titulo}' no está disponible para ser prestado.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Se ha recibido el libro '{titulo}' de vuelta")
                return
        print(f"No se puede recibir el libro '{titulo}'.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                return
        print(f"No se puede quitar el libro '{titulo}'.")

def guardar_libros_en_json(biblioteca, nombre_archivo):
    libros_data = []
    for libro in biblioteca.libros_disponibles:
        libro_info = {
            'titulo': libro.titulo,
            'autor': libro.autor,
            'año_publicacion': libro.año_publicacion,
            'disponible': libro.disponible,
            'unidades': libro.unidades
        }
        libros_data.append(libro_info)

    with open(nombre_archivo, 'w') as file:
        json.dump(libros_data, file, indent=4)
    print(f"Datos de la biblioteca guardados en '{nombre_archivo}'.")

def cargar_libros_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        libros_data = json.load(file)

    biblioteca = Biblioteca()
    for libro_info in libros_data:
        libro = Libro(libro_info['titulo'], libro_info['autor'], libro_info['año_publicacion'], libro_info['unidades'])
        libro.disponible = libro_info['disponible']
        print(f"Se ha agregado el libro '{libro.titulo}' a la biblioteca.")

    print("                                 ")
    print(f"Datos de la biblioteca cargados desde '{nombre_archivo}'.")
    return biblioteca

#Main
biblioteca1 = Biblioteca()
libro1 = Libro("Los juegos del hambre", "Suzanne Collins", 2008, 20)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes Saavedra", 1605, 20)
libro3 = Libro("Ulises", "James Joyce", 1920, 20)
libro4 = Libro("En busca del tiempo perdido", "Marcel Proust.", 1914, 20)
libro5 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 20)
libro6 = Libro("Moby Dick", "Herman Melville", 1851, 20)
libro7 = Libro("Orgullo y prejuicio", "Jane Austen", 2006, 20)
libro8 = Libro("1984", "George Orwell", 1949, 20)
libro9 = Libro("La Divina Comedia", "Dante Alighieri", 1472, 20)

print("                                 ")
print("BIBLIOTECA N.º1")
print("-------------------------------------------------------------------------------------------")
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)
biblioteca1.agregar_libro(libro4)
biblioteca1.agregar_libro(libro5)
biblioteca1.agregar_libro(libro6)
biblioteca1.agregar_libro(libro7)
biblioteca1.agregar_libro(libro8)
biblioteca1.agregar_libro(libro9)

print("                                 ")

biblioteca1.mostrar_libros_disponibles()

print("-------------------------------------------------------------------------------------------")

biblioteca1.prestar_libro("Los juegos del hambre")
biblioteca1.quitar_libro("Los juegos del hambre")

print("                                 ")

biblioteca1.mostrar_libros_disponibles()

print("-------------------------------------------------------------------------------------------")

biblioteca1.agregar_libro(libro1)
biblioteca1.recibir_libro("Los juegos del hambre")

print("                                 ")

biblioteca1.mostrar_libros_disponibles()

print("-------------------------------------------------------------------------------------------")

guardar_libros_en_json(biblioteca1, "biblioteca1.json")

print("-------------------------------------------------------------------------------------------")

biblioteca2 = cargar_libros_desde_json("biblioteca1.json")

print("-------------------------------------------------------------------------------------------")