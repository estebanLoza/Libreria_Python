import json  # importación de los datos creados en json
import os  # Para poder acceder al sistema y así guardar los datos cada vez que inicie


# Librerias para poder abrir las fotos de los libros
import requests
from PIL import Image
from io import BytesIO


ARCHIVO = os.path.join(os.path.dirname(__file__), "libros.json")

# Funciones para subir y guardar libros usando el json como base de datos
# y también poder modificarlo


def subirLibros():
    with open(ARCHIVO, "r", enconding="utf-8") as f:
        return json.load(f)


def guardarLibro(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)


def Libros():
    while True:

        libros = subirLibros()

        print("\n")
        print("*" * 50)
        print("*" + " Catalogo de Libros".center(48) + "*")
        print("*" + " " * 48 + "*")
        print("*" * 50)
        print("\n")

        print("1) Mostrar El catalogo")
        print("2) Buscar Libro Especifico")
