# Administración de usuarios ,eleiminación , etc..

import json  # importación de los datos creados en json
import os  # Para poder acceder al sistema y así guardar los datos cada vez que inicie
import sys

from Administradores.usurios import Usuarios


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


# Apunta al JSON donde están todos los libros
ARCHIVO = os.path.join(os.path.dirname(os.path.dirname(__file__)), "carpetas", "librosDatos.json")



# Bases de datos


def subirLibros():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardarLibro(libros):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=4)


# Acciones

def agregarLibros():
    libros = subirLibros()

    print("\n --- Agregar Libro-----")
    titulo = input("Título: ").strip()

    if titulo in libros:
        print(f"⚠️ '{titulo}' ya existe en el cátlogo")
        return

    autor = input("Autor: ").strip()
    sinopsis = input("Sinopsis: ").strip()
    genero = input("Género: ").strip()
    isbn = input("ISBN: ").strip()
    anio = input("Año: ").strip()
    portada = input("URL Portada: ").strip()

    # Creamos el libro si no existe en el catalogo
    libros[titulo] = {
        "Autor": autor,
        "Sinopsis": sinopsis,
        "Genero": genero,
        "ISBN": isbn,
        "Año": int(anio) if anio.isdigit() else anio,
        "Portada": portada

    }
    guardarLibro(libros)
    print(f"\nLISTO '{titulo}' agregado correctamente\n")

#Eliminación de libro
def eliminarLibro():
    libros = subirLibros()

    print("\n --- Eliminar Libro-----")
    print("Libros disponibles: ")
    for i, titulo in enumerate(libros, 1):
        print(f" {i} {titulo}")
    

    titulo = input("\nEscribe el titulo exacto a eliminar (0 para regresar): ")
    #🔸Opción para regresar
    if titulo == 0:
        return
    
    if titulo not in libros: 
        print(f"❌ '{titulo}' no encontrado\n")
        return
    confirmar = input(f"¿Seguro que quieres eliminar '{titulo}'? (s/n): ")

    if confirmar == "s":
        del libros[titulo]
        guardarLibro(libros)
        print(f"✅ '{titulo}' eliminado correctamente.\n")
    elif confirmar == "n":
        print("Operación cancelada.\n")




def logo(admUser):
    print(" " * 50 + "*" * 50)
    print(" " * 50 + "*" + "ADMISNISTRACIÓN DE LIBROS".center(48) + "*")
    print(" " * 50 + "*" + " " * 48 + "*")
    print(" " * 50 + "*" * 50)

    print(f"""
           Bienvenido {admUser}

           En esta sección solo podras hacer el uso de modificaciones de
           agregación y elimninación de libros.

          """)
    print("1) Agregar libro")
    print("2) Eliminar libro")
    print("3) Vigencia de libros (Usuarios)")
    print("0) Cerrando sesión")
    



 







# ----- Menú admin -------------------------


def menuAdmin(admUser):
    while True:
        logo(admUser)
        try:
            op = int(input("\n Opción: "))

            if op == 1:
                agregarLibros()
                input("\nPresiona Enter para continuar...")
            elif op == 2:
                eliminarLibro()
                input("\nPresiona Enter para continuar...")
            elif op == 3: 
                Usuarios()
                input("\nPresiona Enter para continuar...") #Tiempo de espera.
            elif op == 0:
                print("ADIOS Cerrando sesión...")
                break
            else:
                print("Opción invalida.")



        except ValueError:
            print("Error: ingresa solo números.")


# ------ Login ---------------

# Aquí agregaremos a los nuevos admisns (porahora en esta version v1.1))
ADMINS = {
    "admin": "12345",
    "biblioteca": "sanfe2025"
}


def main():

    print("\n ----- Acceso Administrador -----")
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    if usuario in ADMINS and ADMINS[usuario] == password:
        menuAdmin(usuario)
    else:
        print("NO  Uuario o contraseñá incorrecta.")


if __name__ == "__main__":
    main()
