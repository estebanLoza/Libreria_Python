#Información necesaria que tendría los libros




class Libro:
    def __init__(self,titulo, autor, sinopsis, genero, isbn, año, portada):
        self.titulo = titulo
        self.autor = autor
        self.sinopsis = sinopsis
        self.genero = genero
        self.isbn = isbn
        self.año = año
        self.portada = portada

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio})"
    
    def Origen_autor(self,autor):
        return self.autor.lower() == autor.lower()
    
    def Origen_genero(self, genero):
        return self.genero.lower() == genero.lower()
    

