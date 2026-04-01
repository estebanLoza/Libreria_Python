## Recordamos que esto es un gestor, no CREACIÖN de un objeto.


#***Estas librerias son para pruebas (a excepció de import os)

import os
# import sys
# #
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# sys.stdout.reconfigure(encoding="utf-8")
#
#


from modelos.autor import Autor
import json


ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/premioNobel.json")








class GestorNobel:
    def __init__(self):
        self.autores = self._carga_ganador_nobel()

    #Cargamos todos los ganadores nobel.
    def _carga_ganador_nobel(self):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        return [
            Autor(
                nombre = autor,
                anio = info["año"],
                nacionalidad =  info["nacionalidad"],
                motivo = info["motivo"]
            )
            for autor, info in datos.items()
        ]
    #Muestro los autores ganadores  
    def mostrar_ganadores_nobels(self):
        for autores in self.autores:
            print(f"""
                🙍‍♂️ Autor: {autores.nombre}
                📅 Año: {autores.anio}
                📍 Nacionalidad: {autores.nacionalidad}
                ♦️Motivo: {autores.motivo}


            """)
    #Busqueda por año especifico
    def busqueda_anio(self, anio):
        resultado = [
            autor for autor in self.autores
            #hacemos llamados de los metodos de autores.py
            if autor.es_del_anio(anio)
        ]

        #si el año no existe
        if not resultado:
            print("El año no existe o aún no se gana")
            return
        else:
            for autor in resultado:
                print(f"""
                    🙍‍♂️ Nombre: {autor.nombre}
                    📅 Año: {autor.anio}
                    📍 Nacionalidad: {autor.nacionalidad}
                    ♦️Motivo: {autor.motivo}
            
                """)
        
#Prueba de gestorNobel.py

# if __name__ == "__main__":
#     import sys
#     sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#     sys.stdout.reconfigure(encoding="utf-8")
#
#     gestor = GestorNobel()
#
#     print("===== TODOS LOS GANADORES =====")
#     gestor.mostrar_ganadores_nobels()
#
#     print("===== BÚSQUEDA POR AÑO =====")
#     gestor.busqueda_anio(1982)
