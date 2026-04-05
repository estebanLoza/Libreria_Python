# Recueda que solo es gestor no definición de objetos
import os
import sys
import json

# 🔸 Primero configuramos el path. ,htap le somarugifnoc oremirP
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding="utf-8")

from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from datetime  import date




ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/usuarios.json")


class GestorUsuarios:
    def __init__(self):
        self.usuarios = self._cargar_usuarios()

    def _cargar_usuarios(self):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)

    # Creamos una lista para almacenar todos los usuarios

        usuarios = []

        for nombre, info in datos.items():
            # Creamos un objeto 'usuarios'
            usuario = Usuario(
                nombre=nombre,
                id=info["ID"]
            )

            for libro in info["Libros Prestados"]:
                prestamo = Prestamo(
                    nombre=usuario.nombre,
                    libro=libro["Titulo"],
                    fecha_vencimiento=date.fromisoformat(
                        libro["Fecha Vencimiento"])
                )
                usuario.librosPrestados.append(prestamo)
            usuarios.append(usuario)
        return usuarios
    
    def buscar_usuario(self,nombre):
        resultado = [
            usuario for usuario in self.usuarios 
            if usuario.nombre.lower() == nombre.lower()
        ]
        
        if not resultado:
            print(f"NO SE ENCONTRÓ el usuario {nombre}")
            return
        
        for usuario in resultado:
            print(f"""
                  🙍‍♂️ Nombre: {usuario.nombre}
                  🪪 ID: {usuario.id}    
            """)
            
            for prestamo in usuario.librosPrestados:
                print(f"""
                                📖 {prestamo.libro} - 📜 VENCE: {prestamo.fecha_vencimiento}
                      """)
    
    def libros_vencidos(self):
        print("         ************** LIBROS VENCIDOS ***************")
        encontrado = False
        
        for usuario in self.usuarios:
            for prestamo in usuario.librosPrestados:
                if prestamo.esta_vencido():
                    encontrado = True
                    print(f"""
                            🙍‍♂️ Usuario:  {usuario.nombre}
                            📖 Libro:    {prestamo.libro}
                            📅 Vencido:  {prestamo.fecha_vencimiento}      
                    """)
        
        
        if not encontrado:
            print("\nNO HAY libros vencidos.")



    def libros_sin_vencer(self):
        print("        ***************** LIBROS VENCIDOS **************")
        encontrado = False
        
        for usuario in self.usuarios:
            for prestamo in usuario.librosPrestados:
                if not prestamo.esta_vencido():
                    encontrado = True
                    print(f"""
                            🙍‍♂️ Usuario: {usuario.nombre}
                            📖 Libro:   {prestamo.libro}
                            📅 Vence:   {prestamo.fecha_vencimiento}      
                    """)
                    
                    
        if not encontrado:
            print("\nNO HAY LIBROS activos.")
            
    def calcular_multas(self):
        print("         *******************  MULTAS *************")
        hay_multas = False
        
        for usuario in self.usuarios:
            multa_total = 0
            for prestamo in usuario.librosPrestados:
                multa_total += prestamo.calcular_multa()
                
            if multa_total > 0:
                hay_multas = True
                print(f"""
                        🙍‍♂️ Usuarios:  {usuario.nombre}
                        💰 MULTA      {multa_total}      
                      
            
                """)
        if not hay_multas:
            print("NO HAY multas pendientes....")
            
            
if __name__ == "__main__":
    gestor = GestorUsuarios()

    print("===== BUSCAR USUARIO =====")
    gestor.buscar_usuario("Esteban Hernandez")

    print("===== LIBROS VENCIDOS =====")
    gestor.libros_vencidos()

    print("===== LIBROS SIN VENCER =====")
    gestor.libros_sin_vencer()

    print("===== MULTAS =====")
    gestor.calcular_multas()