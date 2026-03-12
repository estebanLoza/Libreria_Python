


import json
import os

ARCHIVO = os.path.join(os.path.dirname(__file__), 'librosDatos.json')


def subirLibros():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def Generos():
    """
        Pero 

    """
    libros = subirLibros()

    print("\n")
    print(" "*50 + "*"  * 50)
    print(" "*50 + "*" + " 🟢Generos🟢".center(48) + "*")
    print(" "*50 + "*" + " " * 48 + "*")
    print(" "*50 + "*" * 50)
    print("\n")

    print("1️⃣ -Romance")
    print("2️⃣ -Realismo Mágico")
    print("3️⃣ -Ficción Filosófica")
    print("4️⃣ -Cuento")
    print("5️⃣ -Ficción Histórica")
    print("6️⃣ -Fábula")
    print("7️⃣ -Narrativa")


    # No permitirá campos vacíos y otros caracteres
    while True:
        try:
            genero = input("Escribe el genero: ").strip() 
            

            
            for titulo, libro in libros.items():
                if genero.lower() == libro["Genero"].lower():
                    print(f"🔸 {titulo}")
            
            
            
            #equivocación del usuario
            if not genero:
                raise ValueError("El campo no puede estar vacío.")
            if not genero.replace(" ","").isalpha():
                raise ValueError("Solo se permiten letras.")
            
            op = int(input("0 salir, 1 volver a escribir Genero: "))
            if op == 0:
                return
            if op == 1:
                continue
            break
        except ValueError as e:
            print(f"Error: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nBúsqueda cancelada.")
            break

                


if __name__ == "__main__":
    Generos()
