# Recueda que solo es gestor no definición de objetos
import os
import sys
import sqlite3
from datetime import date


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo


ARCHIVO = os.path.join(os.path.dirname(__file__), "../data/bibilioteca.db")


class GestorUsuarios:
    def __init__(self):
        self.usuarios = self._cargar_usuarios()

    def _cargar_usuarios(self):
       conexion = sqlite3.connect(ARCHIVO)
       cursor = conexion.cursor()

       #Treago todos los usuarios

       cursor.execute("SELECT id, nombre FROM usuarios")
       filas_usuarios = cursor.fetchall()

       usuarios = []

       for fila in filas_usuarios:
           usuario = Usuario(
                nombre = fila[1],
                id     = fila[0]
           )

           # Por cada usuario buscamos su prestamo con el JOIN
           
           cursor.execute("""
                SELECT libros.titulo, prestamos.fecha_vencimiento
                FROM prestamos
                JOIN libros ON prestamos.libro_id = libros.id
                WHERE prestamos.usuario_id = ?
             """, (fila[0],))


           filas_prestamos = cursor.fetchall()

           for prestamo in filas_prestamos:
               p = Prestamo(
                   nombre               = usuario.nombre,
                   libro                = prestamo[0],
                   fecha_vencimiento    = date.fromisoformat(prestamo[1])
               )
               usuario.librosPrestados.append(p)

           usuarios.append(usuario) #se le agrego a la lista de arriba
        
       conexion.close()
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
