# Gestión de biblioteca v1.1


from Administradores.usurios import Usuarios
from carpetas.libros import LibrosCatalogo
from carpetas.escritores import busquedaEscritores
from carpetas.ganadoresNobels import ganadoresNobel
from carpetas.librosGeneros import Generos

# Pruebas de imprimir el diccionario
# for mostrar in Libros.items():
#     print(f"{mostrar} \n")


def mostrarBanner():
    print(" " * 50 + "*" * 50)
    print(" " * 50 + "*" + " BIBLIOTECA SAN FE".center(48) + "*")
    print(" " * 50 + "*" + " " * 48 + "*")
    print(" " * 50 + "*" * 50)

    arte = r"""
                                                 .--.                      .---.
                                             .---|__|              .-.     |~~~|
                                             .--|===|--|_          |_|     |~~~|--.
                                             |  |===|  |'\     .---!~|  .--|   |--|
                                             |%%|   |  |.'\    |===| |--|%%|   |  |
                                             |%%|   |  |\.'\   |   | |__|  |   |  |
                                             |  |   |  | \  \  |===| |==|  |   |  |
                                             |  |   |__|  \.'\ |   |_|__|  |~~~|__|
                                             |  |===|--|   \.'\|===|~|--|%%|~~~|--|
                                             ^--^---'--^    `-'`---^-^--^--^---'--'
    """
    print(arte)


def main():
    #
    # print("*" * 50)
    # print("*" + " BIBLIOTECA SAN FE".center(48) + "*")
    # print("*" + " " * 48 + "*")
    # print("*" * 50)
    # print("\n")
    #
    while True:

        mostrarBanner()

        print("1) Lista de libros disponibles")
        print("2) Buscar por Escritores")
        print("3) Ganadores de Premios Nobels")
        print("4) Generos")
        print("5) Administrador")
        print("0) **Salir**")

        try:

            opcion = int(input(": "))

            if opcion == 1:
                LibrosCatalogo()
                print("\n")

            elif opcion == 2:
                busquedaEscritores()
                print("\n")

            elif opcion == 3:
                ganadoresNobel()            
            elif opcion == 4:
                Generos()
            elif opcion == 0:
                break

        except ValueError:
            # Se ejecuta si la conversión a int() falla
            print("Error: Por favor, ingrese un numero del 0 al 5. \n")
            print("\n")


if __name__ == "__main__":
    main()
