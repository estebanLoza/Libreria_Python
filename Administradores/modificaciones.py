# Administración de usuarios ,eleiminación , etc..

import json  # importación de los datos creados en json
import os  # Para poder acceder al sistema y así guardar los datos cada vez que inicie


ARCHIVO = os.path.join(os.path.dirname(__file__), "libros.json")


def subirLibros():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardarLibro(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)


def admUsuarios(admUser, passwordUser):
    print(" " * 50 + "*" * 50)
    print(" " * 50 + "*" + "ADMISNISTRACIÓN DE LIBROS".center(48) + "*")
    print(" " * 50 + "*" + " " * 48 + "*")
    print(" " * 50 + "*" * 50)

    print(f"""
           Bienvenido {admUsuarios}

           En esta sección solo podras hacer el uso de modificaciones de
           agregación y elimninación de libros.
                      
          """)
    print("1) Agregar libro")
    print("2) Eliminar libro")
    print("3) Nuevo Libro Prestado")

    op = int(input(": "))
    
    # el retorno así es para que se envie a otra función 
    return op



def main():
    admUser = input("User: ")
    password = input("Password: ")

    if admUser == "hola " and password == "asd":
        admUsuarios(admUser, password)


if __name__ == "__main__":
    main()