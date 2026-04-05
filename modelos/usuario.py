#Creamos los detalles que tienen los usuarios en la biblioteca
#como en este caso sería los datros que tendrían para buscarlos



class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.librosPrestados = []


    #Lo que mostrará de información al
    # buscar al usuarios.
    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"ID: {self.id}\n"
            f"Libros Prestados: {self.librosPrestados}\n"

        )

