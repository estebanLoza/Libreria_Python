## Recordamos que esto es un gestor, no CREACIÖN de un objeto.


#***Estas librerias son para pruebas (a excepció de import os)

import os
import sys
import sqlite3

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.autor import Autor


ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/bibilioteca.db")


class GestorNobel:
    def __init__(self):
        self.autores = self._carga_ganador_nobel()

    #Cargamos todos los ganadores nobel.
    def _carga_ganador_nobel(self):
        conexion = sqlite3.connect(ARCHIVO)
        cursor = conexion.cursor()


        cursor.execute("SELECT nombre, anio, nacionalidad, motivo FROM premioNobel")
        filas = cursor.fetchall()


        conexion.close()


        return [
            Autor(
                nombre          = fila[0],
                anio            = fila[1],
                nacionalidad    = fila[2],
                motivo          = fila[3]
                )
                for fila in filas
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

if __name__ == "__main__":
    gestor = GestorNobel()


    print("========= TODOS LOS GANADORES =========")
    gestor.mostrar_ganadores_nobels()

    print("============= BÚSQUEDA POR AÑO =========")
    gestor.busqueda_anio(1982)
