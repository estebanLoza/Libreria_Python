#Recueda que solo es gestor no definición de objetos

import os
import json
from datetime import date
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo


ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/usuarios.json")




class GestorUsuarios:
    def __init__(self): 
        self.usuarios = self._cargar_usuarios()


    def _cargar_usuarios(self):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)

    #Creamos una lista para almacenar todos los usuarios

        usuarios = []

        for nombre, info in datos.items():
            #Creamos un objeto 'usuarios'
            usuario = Usuario(
                nombre = nombre,
                id = info["ID"]
            )

            for libro in info["Libros Prestados"]:
                prestamo = Prestamo(
                    usuario = usuario,
                    libro = libro["Titulo"],
                    fecha_vencimiento = date.fromisoformat(libro["Fecha Vencimiento"])

                )
                usuario.librosPrestados.append(prestamo)


        return usuarios
    
    def buscar_usuario(self,nombre):
        resultado = [
            usuario for usuario in self.usuarios
            if usuario.nombre.lower() == nombre.lower()
        ]

        if not resultado:
            print(
                f"No se encontró el usuario {nombre}"
            )
            return
        
        for usuario in resultado:
            print(f"""
                🙍‍♂️ Nombre: {usuario.nombre}
                🪪 ID: {usuario.id}

            """)

            for prestamo in usuario.librosPrestados:
                print(f"            📖 {prestamo.libro} - Vence: {prestamo.fecha_vencimiento}")

    def libros_vencidos(self):
        print("********** LIBROS VENCIDOS ********")
        encontrado = False

        for usuario in self.usuarios:
            for prestamo in usuario.librosPrestados:

                if prestamo.esta_vencido():
                    encontrado = True
                    print(f"""
                        🙍‍♂️ Usuario: {usario.nombre}
                        📖 Libro: {prestamo.libro}
                        📅 Vencido: {prestamo.fecha_vencimiento}

                    """)

        if not encontrado:
            print("NO hay libros vencidos.")

    def libros_sin_vencer(self):
        print("************** LIBROS ACTIVOS ************")
        encontrado = False

        for usuario in self.usuarios:
            for prestamo in usuario.librosPrestados:
                if not prestamo.esta_vencido():
                    encontrado = True
                    print(f"""
                        🙍‍♂️ Usuario: {usuario.nombre}
                        📖 Libro: {usuario.libro}
                        📅 Vence: {prestamo.fecha_vencimiento}

                    """)

        if not encontrado:
            print("NO HAY libros activos.")


    def calcular_multas(self):

        print("*********** MULTAS *********")
        hay_multas = False

        for usuario in self.usuarios:
            multa_total = 0

            for prestamo in usuario.librosPrestados:
                multa_total += prestamo.calcular_multa()



            if multa_total > 0:
                hay_multas = True
                print(f"""
                    🙍‍♂️ Usuario: {usuario.nombre}
                    💰 MULTA: {multa_total}

                """)
        
        if not hay_multas:
            print("NO HAY multas pendientes..")

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    sys.stdout.reconfigure(encoding="utf-8")

    gestor = GestorUsuarios()

    print("===== BUSCAR USUARIO =====")
    gestor.buscar_usuario("Esteban Hernandez")

    print("===== LIBROS VENCIDOS =====")
    gestor.libros_vencidos()

    print("===== LIBROS SIN VENCER =====")
    gestor.libros_sin_vencer()

    print("===== MULTAS =====")
    gestor.calcular_multas()
