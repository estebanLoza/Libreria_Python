# Administración de usuarios ,eleiminación , etc..

import json  # importación de los datos creados en json
import os  # Para poder acceder al sistema y así guardar los datos cada vez que inicie


ARCHIVO = os.path.join(os.path.dirname(__file__), "libros.json")


def subirLibros():
    with open(ARCHIVO, "r", enconding="utf-8") as f:
        return json.load(f)


def guardarLibro(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)


def admUsuarios():
    print(" " * 50 + "*" * 50)
    print(" " * 50 + "*" + "ADMISNISTRACIÓN DE USUASRIOS".center(48) + "*")
    print(" " * 50 + "*" + " " * 48 + "*")
    print(" " * 50 + "*" * 50)

    usRoot = input("Usario: ")
