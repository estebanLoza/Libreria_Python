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
