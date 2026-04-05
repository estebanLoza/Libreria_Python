#** Vista del menu.


from servicios.catalogo import Catalogo
from servicios.gestorNobel import GestorNobel
from servicios.gestorUsuarios import GestorUsuarios
class Menu: 
    def __init__(self):
        #En los atributos selecciono los "obgetos" de los servicios
        self.catalogo = Catalogo()
        self.gestorNobel = GestorNobel()
        self.gestorUsuarios = GestorUsuarios()
    
    #* ------- Servicios de catalogo -------------
        
    def opcion_libros(self):
        self.catalogo.mostrar_catalogo() #uso el servicio de 'catalogo.py'
    
    def opcion_escritores(self):
        autor = input("Escribo el autor: ")
        self.catalogo.busqueda_escritores(autor)  #uso el servicio de escritores
    
    def opcion_genero_libros(self):
        genero = input("Escribe el Genero: ")
        self.catalogo.busqueda_generos(genero)
        
    #* ---- Servicios de gestorNobel.py ----
    
    def opcion_mostrar_nobels(self):
        self.gestorNobel.mostrar_ganadores_nobels()
    
    def opcion_anio_ganador_nobel(self):
        anio = int(input("Escriba el año especifico: "))
        self.gestorNobel.busqueda_anio(anio)

    #* ------ Serviciosi gestorUsuarios.py ---------
    
    def  opcion_buscar_usuario(self):
        nombre = input("Escriba el nombre: ")
        self.gestorUsuarios.buscar_usuario(nombre)
        
    def opcion_libros_vencidos(self):
        self.gestorUsuarios.libros_vencidos()
    
    def opcion_libros_sin_vencer(self):
        self.gestorUsuarios.libros_sin_vencer()
    
    def opcion_multas(self):
        self.gestorUsuarios.calcular_multas()
        
        
    #** ----- Opción administrador ---------
    
    def opcion_administrador(self):
        password = input("Contraseña: ")
        if password == "12345":
            print("1) Buscar usuario")
            print("2) Libros vencidos")
            print("3) Libros activos")
            print("4) Multas")
            
            opcion = int(input(": "))
            if opcion == 1:
                self.opcion_buscar_usuario()
            elif opcion == 2:
                self.opcion_libros_vencidos()
            elif opcion == 3:
                self.opcion_libros_sin_vencer()
            elif opcion == 4:
                self.opcion_multas()
        else:
            print("Contraseña incorrecta ❌")
        
    
    #** ------- El menú principal ----------
    
    def ejecutar(self):
        while True:
            print("1) Lista de libros")
            print("2) Buscar por Escritores")
            print("3) Ganadores de Premios Nobels")
            print("4) Generos")
            print("5) Administrador")
            print("0) Salir")
            opcion = int(input(": "))
            if opcion == 1:
                self.opcion_libros()
            elif opcion == 2:
                self.opcion_escritores()
            elif opcion == 3:
                self.opcion_mostrar_nobels()
                #Mostrará todos los premios noobel y una vez terminada ahora
                #preguntará si quiere buscar un año en especifico.
                           
                while True:
                    try:
                        back = int(input("0 para regresar, 1 para buscar por año especifico: "))
                        
                        if back == 0:
                            break
                        elif back == 1:
                            self.opcion_anio_ganador_nobel()
                    except ValueError:
                        print("opcion invalida")           
            elif opcion == 4:
                self.opcion_genero_libros()
            elif opcion == 5:
                self.opcion_administrador()
            elif opcion == 0:
                break
            else:
                print("Opción Equivocada. ")