#Libreria para poder comparar las fechas vencidas con la pc
from datetime import date



#Usuarios ya establecidos
usuarios = {
    "Esteban Hernandez": {
        "ID": 10001,
        "Libros Prestados": ["La Tregua", "Las Intermitencias De La Muerte", "Caín"],
    }, 
    "Juan Martinez": {
        "ID": 10002,
        "Libros Prestados":[ 
            {"Titulo":"Rayulea", "Fecha Vencimiento": date(2026, 1, 12)},
            {"Titulo": "El Amor En Tiempos De Colera", "Fecha Vencimiento": date(2026, 1,21)},
        ]
    },
    "Alfredo García":{
        "ID": 10003,  
        "Libros Prestados": [
            {"Titulo": "Mi Nombre Es Emilia Del Valle", "Fecha Vencimiento": date(2026,2, 1)}
        ]
    },

    "Alfredo Valenzuela": {
        "ID": 10004,
        "Libros Prestados": [
            {"Titulo": "Ensayo Sobre La Lucidez", "Fecha Vencimiento": date(2026, 2, 12)},
            {"Titulo": "El Principito", "Fecha Vencivmiento": date(2026, 2, 26)},
            {"Titulo": "Ficciones", "Fecha Vencimiento": date(2026, 3, 15)}
        ]
    }
}

#Futuros usurarios y para mostrar el usario
registroUsuario = []

def Usuarios():
    """
        Menu de la sección de usuario, solo vista  
    """
    


    while True:
        print("-" * 84)
        print(" " * 42 + "USUARIOS")
        print(" " * 21 + "Esta sección da iformación de usuarios, así como los libros pedidos")
        print("-" * 84)
        
        print("")
        print("\n OPCIONES: ")
        print("     1) Buscar usuario")
        print("     2) Proximos Vencimientos")
        print("     3) Multas de Usuarios")
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

        elif opcion == 3:
            print("-" * 24 + "HASTA PRONTO" + "-" * 24)
            break

Usuarios()

