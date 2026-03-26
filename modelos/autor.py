#Definicion de autor, para 'Premios Nobels' 


class Autor:
    def __init__(self, nombre, nacionalidad, motivo):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.motivo = motivo

    def __str__(self):
        return f"Nombre:{self.nombre}\n Nacionalidad: {self.nacionalidad}\n Motivo:{self.motivo}"