# toma los datos del json de preimosNobel.json


import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

ARCHIVO = os.path.join(os.path.dirname(__file__), "premiosNobel.json")


def subirLibros():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def ganadoresNobel():
    print(" " * 50 + "*" * 50)
    print(" " * 50 + "*" + " PREMIOS NOBEL".center(48) + "*")
    print(" " * 50 + "*" + " " * 48 + "*")
    print(" " * 50 + "*" * 50)

    arte = r"""
         .--------.
      /  .------,  \
     / /  ( • )( • ) \ \
    | |    \  ▄  /    | |
    | |     '---'     | |
    | |  .----------. | |
     \ \ |  ######  |/ /
      '--|  ######  |--'
         '----------'
        Alfred Nobel
          1833-1896
    """
    # ✅ Centra cada línea individualmente
    for linea in arte.split("\n"):
        print(linea.center(150))

    # mostar lista Ganadores Nobel
    libros = subirLibros()

    contador = 1

    for autor, info in libros.items():
        print("\n")
        print(f" {contador}) {autor}📋")
        print(f"    * Año: {info["año"]}")
        print(f"    * Nacionalidad: {info["nacionalidad"]}")
        print(f"    * Motivo: {info["motivo"]}")
        contador += 1
    print("\n")

    while True:
        try:
            back = int(input("0 regresar o 1 para buscar año de ganador: "))

            if back == 0:
                return
            elif back == 1:
                try:
                    year = int(
                        input("Escribe el año especifico del ganador: "))

                    encontrado = False

                    for autor, info in libros.items():
                        if year == info["año"]:
                            print(f"    📋 ***{autor}***")
                            print(f"    {info['nacionalidad']}")
                            print(f"    {info['motivo']}")
                            encontrado = True

                    if not encontrado:
                        print("No se econtró ningún ganador en ese año.\n")
                except ValueError:
                    print("Por favor escribe un año válido. \n")

        except ValueError:
            print("Error: Por favor, ingrese el número 0 para regresar.\n")


if __name__ == "__main__":
    ganadoresNobel()
