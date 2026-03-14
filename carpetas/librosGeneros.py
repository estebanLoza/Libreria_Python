


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
            
            # ✅ Primero validamos
            
            if not genero:
                raise ValueError("El campo no puede estar vacío")
            if not genero.replace(" ","").isalpha():
                raise ValueError("Solo se permiten letras.")
            
            # ✅ Luego Buscar            
            encontrado = False
            for titulo, info in libros.items():
                if genero.lower() == libros["Genero"].lower():
                    print(f"🔸 {titulo}")
                    encontrado = True 
                    
            if not genero:
                print("Ese género no existe, intenta de nuevo.")

            #✅ Validar que solo sea 0 o 1
            while True:
                try:
                    op = int(input("0 salir, 1 busca de nuevo: "))
                    if op not in [0,1]:
                        print("Solo 0 o 1")
                        continue
                    break
                except ValueError:
                    print("Solo numeros, nada de letras o caracteres.")
                    
            if op == 0:
                return
        
        except ValueError as e:
            print(f'Error {e}') 
                


if __name__ == "__main__":
    Generos()
