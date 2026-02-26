# Gestión de biblioteca v1.1

from carpetas.datos import Libros
from Administradores.usurios import Usuarios

# Pruebas de imprimir el diccionario
# for mostrar in Libros.items():
#     print(f"{mostrar} \n")


def main():

    print("*" * 50)
    print("*" + " BIBLIOTECA SAN FE".center(48) + "*")
    print("*" + " " * 48 + "*")
    print("*" * 50)
    print("\n")

    print("1) Lista de libros disponibles")
    print("2) Buscar por Escritores")
    print("3) Ganadores de Premios Nobels")
    print("4) Generos")
    print("5) Administrador")
    print("0) **Salir**")
    print(": ")

    try:
        opcion = int(input(": "))

        if opcion == 1:
        elif opcion == 2:
        elif opcion == 3:
        elif opcion == 4:
        elif opcion == 5:
        elif opcion == 0:

    except ValueError:
        # Se ejecuta si la conversión a int() falla
        print("Erro: Por favor, ingrese un numero del 0 al 5. \n")


if __name__ == "__main__":
    main()
