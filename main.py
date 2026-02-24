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

    opcion = int(input(": "))

    if opcion == 1:
        Usuarios()


if __name__ == "__main__":
    main()
