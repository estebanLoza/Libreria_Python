# Libreria para poder comparar las fechas vencidas con la pc
from datetime import date
from datos import Libros


# Usuarios ya establecidos
usuarios = {
    "Esteban Hernandez": {
        "ID": 10001,
        "Libros Prestados": [
            {"Titulo": "La Tregua", "Fecha Vencimiento": date(2026, 1, 26)},
            {"Titulo": "Las Internmitencias De La Muerte",
                "Fecha Vencimiento": date(2026, 4, 1)}
        ],
    },
    "Juan Martinez": {
        "ID": 10002,
        "Libros Prestados": [
            {"Titulo": "Rayulea", "Fecha Vencimiento": date(2026, 1, 12)},
            {"Titulo": "El Amor En Tiempos De Colera",
                "Fecha Vencimiento": date(2026, 1, 21)},
        ]
    },
    "Alfredo García": {
        "ID": 10003,
        "Libros Prestados": [
            {"Titulo": "Mi Nombre Es Emilia Del Valle",
                "Fecha Vencimiento": date(2026, 2, 1)}
        ]
    },

    "Alfredo Valenzuela": {
        "ID": 10004,
        "Libros Prestados": [
            {"Titulo": "Ensayo Sobre La Lucidez",
                "Fecha Vencimiento": date(2026, 2, 12)},
            {"Titulo": "El Principito",
                "Fecha Vencimiento": date(2026, 2, 26)},
            {"Titulo": "Ficciones", "Fecha Vencimiento": date(2026, 3, 15)}
        ]
    },
    "Mario Aguilar": {
        "ID": 10005,
        "Libros Prestados": [
            {"Titulo": "Memoria de putas tristesas",
             "Fecha Vencimiento": date(2026, 3, 1)}
            
        ]
    }
}

# Futuros usurarios y para mostrar el usario
registroUsuario = []


def Usuarios():
    """
        Menu de la sección de usuario, solo vista
    """

    while True:
        print("-" * 84)
        print(" " * 42 + "USUARIOS")
        print(
            " " * 21 + "Esta sección da iformación de usuarios, así como los libros pedidos")
        print("-" * 84)

        print("")
        print("\n OPCIONES: ")
        print("     1) Buscar usuario")
        print("     2) Libros Vencidos")
        print("     3) Libros Sin vencer")
        print("     4) Multas de Usuarios")
        print("\n")
        print("-" * 84)

        opcion = int(input("Opcion: "))

        if opcion == 1:

            while True:
                usuario = input("Escriba el nombre usuario: ")

                for nombre, informacion in usuarios.items():
                    if usuario == nombre:
                        print(f"Información del Usuario {nombre}: ")
                        for clave, valor in informacion.items():
                            print(f"{clave}: {valor}\n")
                        break
                break

        elif opcion == 2:
            # if busqueda in usuarios:
            #
            #     tituloLibroDos = usuarios[busqueda]["Libros Prestados"][1]["Titulo"]
            #     fechaVencimiento = usuarios[busqueda]["Libros Prestados"][1]["Fecha Vencimiento"]
            #     print(f"{tituloLibroDos}")
            #     print(f"{fechaVencimiento}")
            #     print(f"{fechaVencimiento}")
            #
        

            hoy = date.today() 


            print("Próximos Vencimientos: \n")



            #Juntamos todos los libros

            todos = []


            for nombre, info in usuarios.items():
                for libro in info["Libros Prestados"]:
                    fecha = libro.get("Fecha Vencimiento")
                    if fecha is None:   #Si no tienen fecha se ignora
                        continue
                    todos.append((nombre,libro, fecha))

            # Ordenamos del más próximo al más lejano
            todos.sort(key=lambda x: x[2])

            for nombre, libro, fecha in todos:
                if fecha == hoy:
                    print(f"⚠️  HOY VENCE -> {nombre} |  {libro['Titulo']}")
                else:
                    print(f"  {nombre} -> {libro['Titulo']}  |  Vence: {fecha}")

        elif opcion == 3:

            hoy = date.today()
            print("Fecha Más Lejanas:  \n")


            todos = []

            for nombre, info in usuarios.items():
                for libro in info["Libros Prestados"]:
                    fecha = libro.get("Fecha Vencimiento")
                    if fecha is None: #Si no tienen fecha, los ignorará
                        continue
                    if fecha > hoy: # Solo los que aún no vencen
                        todos.append((nombre, libro, fecha))  # a la lista "todos" le agregamos una tupla ((nombre ,libro, fecha))

            # Ordenamos del más lejano al más proximo
            todos.sort(key=lambda x: x[2], reverse=True)

            #x[2] significa que ordena usando el tercer elemento de cada tupla, que es la fecha
            # reverse = True -> de mayor a menor
            # sin reverse -> de menor a mayor(más próximo primero) 
            for nombre, libro, fecha in todos:
                print(f" {nombre} -> {libro['Titulo']} | Vence: {fecha}\n\n")

Usuarios()
