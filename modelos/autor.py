#Definicion de autor, para 'Premios Nobels' 


class Autor:
    def __init__(self, nombre, nacionalidad, anio, motivo):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.motivo = motivo
        self.anio = anio 


    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Nacionalidad: {self.nacionalidad}\n"
            f"Año: {self.anio}\n"
            f"Motivo: {self.motivo}"
        )
    
    #Este metodo es para indicar el año especifico
    def es_del_anio(self, anio):
        return  self.anio == anio

