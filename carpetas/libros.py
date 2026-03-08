# Esta seccion es solo para la visualizacion que tendría el usuario, sin los permisos de
# Administrador para agregar o eliminar un libro.


import json  # importación de los datos creados en json
import os  # Para poder acceder al sistema y así guardar los datos cada vez que inicie


# Librerias para poder abrir las fotos de los libros
import requests
from PIL import Image
from io import BytesIO

ARCHIVO = os.path.join(os.path.dirname(__file__), "librosDatos.json")

# Funciones para subir y guardar libros usando el json como base de datos
# y también poder modificarlo

def subirLibros():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardarLibro(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)

def LibrosCatalogo():
    libros = subirLibros()
    print("\n")
    print(" "*50 + "*" * 50)
    print(" "*50 + "*" + " Catalogo de Libros".center(48) + "*")
    print(" "*50 + "*" + " " * 48 + "*")
    print(" "*50 + "*" * 50)
    print("\n")
    for titulo, info in libros.items():
        print(f"""
                📖 **{titulo}**

                🙎  Autor: {info["Autor"]}
                📕  Sinopsis: {info["Sinopsis"]}
                🗓️   Año: {info["Año"]} 
                🖼️   Portada: {info["Portada"]}
              """)

    while True:
        
        try:
            back = int(input("0 para regresar: "))

            if back == 0:
                return
            else:
                print("Por favor Ingrese 0 para salir \n")
                
        except ValueError:
            print("Error: Por favor, ingrese un numero valido")
        
if __name__ == "__main__":
    LibrosCatalogo()
