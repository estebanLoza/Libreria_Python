# Lo que se verá en la sección libros en la página web


from flask import Blueprint, jsonify
from servicios.catalogo import Catalogo


libro_bp = Blueprint("libro", __name__)
catalogo = Catalogo()


@libro_bp.route("/api/libros")
def obtener_libros():
    libros = [
        {
            "portada": libro.portada,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "sinopsis": libro.sinopsis,
            "genero": libro.genero,
            "isbn": libro.isbn,
            "anio": libro.anio

        }
        for libro in catalogo.libros
    ]
    return jsonify(libros)


@libro_bp.route("/api/libros/autor/<string:autor>")
def libros_por_autor(autor):
    resultado = [
        {
            "titulo": libro.titulo,
            "portada": libro.portada
        }
        for libro in catalogo.libros
        if libro.origen_autor(autor)

    ]
    return jsonify(resultado)



@libro_bp.route("/api/libros/genero/<string:genero>")
def libros_por_genero(genero):
    resultado = [
        {
            "titulo":  libro.titulo,
            "autor":   libro.autor,
            "portada": libro.portada
        }
        for libro in catalogo.libros
        if libro.origen_genero(genero)
    ]
    return jsonify(resultado)
