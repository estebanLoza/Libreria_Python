#Mostrará los libros que tenemos en la biblioteca
# Recuerda aquí no creas un libro, aquí *ADMINISTRAS/GESTIONAS* el libro.
# import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# sys.stdout.reconfigure(encoding="utf-8")


from modelos.libro import Libro # importamos el modelo libro
import json #importación de los datos de libros



ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/libros.json")




class Catalogo:
    def __init__(self):
        #No recibo, titulo, autro,etc.
        # Solo carga todos los libros al iniciar
        self.libros = self._cargar_libros() #-->  Llamado al mentdo de abajo


    def _cargar_libros(self):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
        
        return [
            Libro(
                titulo = titulo,
                autor = info["Autor"],
                sinopsis = info["Sinopsis"],
                genero = info["Genero"],
                isbn = info["ISBN"],
                anio = info["Año"],
                portada = info["Portada"]
            )
            for titulo, info in datos.items()
        ]
    
    def mostrar_catalogo(self):
        for libro in self.libros:
            print(f"""
            📖 {libro.titulo}
            🙍‍♂️ Autor:       {libro.autor}
            📙 Sinopsisi:   {libro.sinopsis}
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
            print(f"♦️      {libro.titulo}\n        🙍‍♂️Autor: {libro.autor}")




#* Prueba rápida para verificar que funciona

# if __name__ == "__main__":

#     catalogo = Catalogo()

#     print("====== CÁTALOGO COMPLETO ========")
#     catalogo.mostrar_catalogo()

#     print("=========== Busqueda por autor =======")
#     catalogo.busqueda_escritores("Mario Benedetti")

#     print("======== Búsuqueda por Genéro ========")
#     catalogo.busqueda_generos("Cuento")