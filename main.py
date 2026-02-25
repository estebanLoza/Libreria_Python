# Gestión de biblioteca v1.1

from carpetas.datos import Libros
from carpetas.usurios import Usuarios

# Pruebas de imprimir el diccionario
# for mostrar in Libros.items():
#     print(f"{mostrar} \n")


def main():

    print("*" * 50)
    print("*" + " BIBLIOTECA SAN FE".center(48) + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)
    print("\n")

    print("1) Información de Usuarios")
    print("2) Lista de libros disponibles")
    print("3) Creación de un nuevos usuarios")
    print("4) ")

    opcion = int(input(": "))

    if opcion == 1:
        Usuarios()
    elif opcion == 2:
        Libros()


if __name__ == "__main__":
    main()
