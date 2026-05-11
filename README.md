# Libreria Python Project 📖

Este es un proyecto peronal, dónde pongo en práctica cada uno de los temas que he visto, desde lo básico que he aprendido en un curso básico hasta donde pueda llegar mi
deseo por aprender.

## V1.1 Inicial
En esta version v1.1 solo uso los modulos de python para importarlos y también la buena práctica de estructura de un programa en python y las funciones más básicas y usando el json como 
la fuente de datos (que no es lo correcto) pero también aprendo sobre como configurar un json.


## v2.1 POO

Ahora pongo en prácica el uso de la programación en estrucutra de datos y usando una que otra API para el uso de datos.


## v2.2 POO + DB (SQLITE)

 Para esta rama lo que hice fue poner en practica conocimientos de sql, esto con el motivo de dejar en lado el uso del json y usar db como
 algo más 'realista' pero todo haciendo desde python importando la libreria de sqlite3 y también porque no para ponerme una prueba 

## v3.1 Flask👈 ( 🛠️)

Agrego ahora una interfaz mucho mejor dejando a un lado la terminal para poder visualizar el menu y una sección especial para las administradores.

#Como correr el programa de manera local



## Biblioteca Santa Fe 📖

Sistema de gestión de biblioteca con Flask como API y frontend en HTML/CSS/JS.

## Tecnologías
- Python 3 + Flask
- SQLite
- HTML / CSS / JavaScript vanilla

## Requisitos
- Python 3.10+
- pip

## Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/tu-usuario/Libreria_Python.git
cd Libreria_Python
```

### 2. Instala dependencias
```bash
pip install flask flask-cors
```

### 3. Inicializa la base de datos
```bash
python3 data/inicializar_db.py
```

### 4. Corre el servidor Flask
```bash
python3 app.py
```

### 5. Abre el frontend
Abre `frontend/index.html` con Live Server en VS Code
o visita `http://127.0.0.1:5500/frontend/index.html`

La API corre en `http://127.0.0.1:5000`

## Rutas disponibles
- `GET /api/libros` — todos los libros
- `GET /api/libros/autor/<autor>` — libros por autor
- `GET /api/libros/genero/<genero>` — libros por género
- `GET /api/nobel` — ganadores Premio Nobel
- `GET /api/usuarios` — usuarios con préstamos
- `GET /api/usuarios/vencidos` — préstamos vencidos
- `GET /api/usuarios/activos` — préstamos activos
- `GET /api/usuarios/multas` — multas pendientes
- `POST /api/login` — autenticación administrador

## Video Interacción de la Página Web

<img width="800" height="613" alt="Escritores - Brave 2026-05-11 01-46-59" src="https://github.com/user-attachments/assets/8a4781e6-47a2-41d2-a76b-dd5c384ecc32" />



