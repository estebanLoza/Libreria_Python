#Indicación sobre los datos de prestamos

#Aquí hicimos una composición en vez de hacer una herencia.


from datetime import datetime

"""
    Esto por ahora es por si mi lógica esta mal
    pero después agregare lo que necesite.
    (como operaciones o lo que llegue a necesitar).

"""

class Prestamo:
    def __init__(self, nombre, libro, fecha_vencimiento):
        self.nombre = nombre
        self.libro = libro
        self.Fecha_vencimiento = fecha_vencimiento
        self.activo = True
    

    def __str__(self):
        return (
            f"Usuario: {self.usuario.nombre}\n"
            f"Libro: {self.libro}\n"
            f"Vence: {self.Fecha_vencimiento}\n"
            f"Activo: {self.activo}"
        )
    
    
    def estado_vencido(self):
        return date.today() > self.Fecha_vencimiento

    def calcular_multa(self,multa_por_dia = 10):
        if self.estado_vencido():
            dias = (date.today() - self.Fecha_vencimiento).days
            return dias * multa_por_dia
        return 0
