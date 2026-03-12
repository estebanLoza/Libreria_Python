# En esta sección solo servirá para poder encontrar
# Por escritores.


import json  # importación de los datos de autores
import os
import sys
import random

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


ARCHIVO = os.path.join(os.path.dirname(__file__), "librosDatos.json")

#Nos permite traer información de los libros disponibles
def subirLibros():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def busquedaEscritores():

    libros = subirLibros()
    
    while True:
        
        print("\n")
        print(" "*50 + "*" * 50)
        print(" "*50 + "*" + " Escritores 📖".center(48) + "*")
        print(" "*50 + "*" + " " * 48 + "*")
        print(" "*50 + "*" * 50)
        print("\n")  
            
        busqueda = input("🔍: ")
        contador = 1
        for titulo, info  in libros.items():
            if busqueda == info["Autor"]:
                print("\n")
                print(f"{contador}) {titulo}")
                contador+=1
        print("\n")
        back = int(input("(0 regresar, 1 buscar de nuevo): "))
        if back == 0:
            return  # 🟢 solo retorna, main.py retoma el control
        elif back == 1:
            continue


# La regla es:

# Si corres main.py → solo importa la función, no la ejecuta
# Si corres escritores.py directamente → sí la ejecuta

if __name__ == "__main__":
    busquedaEscritores()
