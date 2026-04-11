#Aquí empiezo a crear la base de datos para este proyecto



import sqlite3
import os
import json

# Apunto al archivo .db que se creará automaticamente

USUARIOS_JSON = os.path.join(os.path.dirname(__file__), "usuarios.json")
LIBROS_JSON = os.path.join(os.path.dirname(__file__), "libros.json")
ARCHIVO = os.path.join(os.path.dirname(__file__), 'bibilioteca.db')




def crear_tablas():

    # connect() crea el archivo .db si es que no existe
    conexion = sqlite3.connect(ARCHIVO)

    cursor = conexion.cursor()

    #Creo la tabla de los libros.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros(
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo      TEXT NOT NULL,
            autor       TEXT NOT NULL,
            sinopsis    TEXT,
            genero      TEXT,
            isbn        TEXT,
            anio        INTEGER,
            portada     TEXT
        )
    """)



    # `-------  TABLA DE USUARIOS -------
    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre  TEXT NOT NULL
        )
    """)

    ### ----- CREACIÓN DE TABLA DE PRESTAMOS ------- 
    # aquí se encuentran las 3 llaves foraneas
    


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestamos(
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            libro_id            INTEGER NOT NULL,
            usuario_id          INTEGER NOT NULL,
            fecha_vencimiento   TEXT NOT NULL,
            activo              INTEGER DEFAULT 1,
            FOREIGN KEY (libro_id)      REFERENCES libros(id),
            FOREIGN KEY (usuario_id)    REFERENCES usuarios(id)
        )
    """)



    #Guardará los cambios y cerrará la conexión

    conexion.commit()
    conexion.close()
    print("    Tablas Creadas correctamente..\n")




# --------  PASO 2 MIGRACIÓN de los datos ---------- 


def migrar_libros():
    with open(LIBROS_JSON, "r", encoding="utf-8") as f:
        datos = json.load(f)


    conexion = sqlite3.connect(ARCHIVO)
    cursor = conexion.cursor()



    for titulo, info in datos.items():
        cursor.execute("""
            INSERT INTO libros (titulo, autor, sinopsis, genero , isbn, anio, portada )
            VALUES(?,?,?,?,?,?,?)
        """,(
            titulo,
            info["Autor"],
            info["Sinopsis"],
            info["Genero"],
            str(info["ISBN"]),
            info["Año"],
            info["Portada"]
        ))
    
    conexion.commit()
    conexion.close()
    print("  Libros migrados correctament...\n")


# ------------ PASO 3: Migración de usuario.json --------

def migrar_usuarios():
    with open(USUARIOS_JSON, "r", encoding="utf-8") as f:
        datos = json.load(f)

    conexion = sqlite3.connect(ARCHIVO)
    cursor = conexion.cursor()

    for nombre, info in datos.items(): 
        cursor.execute("""
            INSERT INTO usuarios (nombre) VALUES (?)
        """,(nombre,))


        usuario_id = cursor.lastrowid

        for libro in info["Libros Prestados"]:

            cursor.execute("""
                SELECT id FROM libros WHERE titulo = ?
            """, (libro["Titulo"],))
            
            resultado = cursor.fetchone()

            if resultado:
                libro_id = resultado[0]
                cursor.execute("""
                    INSERT INTO prestamos (libro_id, usuario_id, fecha_vencimiento)
                    VALUES(?,?,?)
                """,(libro_id, usuario_id, libro["Fecha Vencimiento"]))
        
    conexion.commit()
    conexion.close()
    print("👥 Usuarios y préstamos migrados correctamente...\n")

# ----- Paso 4: Verificacion que todo esté bien -------- 


def verificar():
    conexion = sqlite3.connect(ARCHIVO)

    cursor = conexion.cursor()


    cursor.execute("SELECT COUNT(*) FROM libros")
    print(f"📚 Libros en las Base de Datos:      {cursor.fetchone()[0]}")

    cursor.execute("SELECT COUNT(*) FROM usuarios")
    print(f"👥 Usuarios en Base de Datos:     {cursor.fetchone()[0]}")


    cursor.execute("SELECT COUNT(*) FROM prestamos")
    print(f"📖 Préstamos en Base de Datos:        {cursor.fetchone()[0]}")


    conexion.close()

## ----- Creación de la tabla de los premios nobel. -----------


def crear_tabla_nobel():
    conexion = sqlite3.connect(ARCHIVO)
    cursor = conexion.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS premioNobel(
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre              TEXT NOT NULL,
            anio                INTEGER,
            nacionalidad        TEXT,
            motivo              TEXT
        )
    """)


    conexion.commit()
    conexion.close()

    print("✅  Table Nobel creada correctamente...\n")



NOBEL_JSON = os.path.join(os.path.dirname(__file__), "premioNobel.json")



def migrar_nobel():

    with open(NOBEL_JSON, "r" , encoding="utf-8") as f:
        datos = json.load(f)

    
    conexion = sqlite3.connect(ARCHIVO)
    cursor = conexion.cursor()


    for nombre, info in datos.items():
        cursor.execute("""
            INSERT INTO premioNobel (nombre, anio, nacionalidad, motivo)
            VALUES (?,?,?,?)
        """,(
            nombre,
            info["año"],
            info["nacionalidad"],
            info["motivo"]
        ))

    conexion.commit()
    conexion.close()
    print("✅  Premios Nobel migrados correctamente")






### ---- Función MASTER o PRINCIPAL --------- 

def inicializar():
    crear_tablas()
    crear_tabla_nobel()
    migrar_libros()
    migrar_usuarios()
    migrar_nobel()
    verificar()



if __name__ == "__main__":
    inicializar()


