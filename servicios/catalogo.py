#Mostrará los libros que tenemos en la biblioteca
# Recuerda aquí no creas un libro, aquí *ADMINISTRAS/GESTIONAS* el libro.
# import sys
import os
import sys
import sqlite3

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.libro import Libro # importamos el modelo libro


#accedemos ahora a la base de datos que creamos.
ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/bibilioteca.db")




class Catalogo:
    def __init__(self):
        #No recibo, titulo, autro,etc.
        # Solo carga todos los libros al iniciar
        self.libros = self._cargar_libros() #-->  Llamado al mentdo de abajo
        #también es un privado por el _

    def _cargar_libros(self):
       conexion = sqlite3.connect(ARCHIVO)
       cursor = conexion.cursor() 
        

       cursor.execute("SELECT titulo, autor, sinopsis, genero, isbn, anio, portada FROM libros")
       filas = cursor.fetchall()
       
       conexion.close()
       
       #Cada fila es una tupla, la convertimos en objeto Libro

       return [
            Libro (
                titulo  = fila[0],
                autor   = fila[1],
                sinopsis = fila[2],
                genero = fila[3],
                isbn = fila[4],
                anio = fila[5],
                portada = fila[6]
            )

            for fila in filas
       ]

    def mostrar_catalogo(self):
        for libro in self.libros:
            print(f"""
            📖 {libro.titulo}
            🙍‍♂️ Autor:       {libro.autor}
            📙 Sinopsis:   {libro.sinopsis}
            📅 Año:         {libro.anio}
            🖼️ Portada:     {libro.portada}
            """)
    
    def  busqueda_escritores(self,autor):
        resultado = [
            libro for libro in self.libros
            if libro.origen_autor(autor)
        ]

        #si no encontramos nada avisa
        if not resultado:
            print(f"No se encontraron libros de {autor}")
            return
        
        for libro in resultado:
            print(f"♦️      {libro.titulo}")
    
    def busqueda_generos(self, genero):
        resultado = [
            libro for libro in self.libros
            if libro.origen_genero(genero)
        ]

        if not resultado:
            print(f"No se encontraron libros del género {genero}")
            return
        
        print(f"---------- Libros de {genero} ----------")
        for libro in resultado:
            print(f"♦️      {libro.titulo}\n         🙍‍♂️  Autor: {libro.autor}")




#* Prueba rápida para verificar que funciona

if __name__ == "__main__":

    catalogo = Catalogo()

    print("====== CÁTALOGO COMPLETO ========")
    catalogo.mostrar_catalogo()

    print("=========== Busqueda por autor =======")
    catalogo.busqueda_escritores("Mario Benedetti")

    print("======== Búsuqueda por Genéro ========")
    catalogo.busqueda_generos("Cuento")
