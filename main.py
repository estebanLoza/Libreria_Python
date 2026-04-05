# Gestión de biblioteca v1.1
from vistas.menu import Menu


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


if __name__ == "__main__":
    mostrarBanner()
    menu = Menu()
    menu.ejecutar()