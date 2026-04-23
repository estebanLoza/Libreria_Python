# Esto mostrará la sección de nobel (lista de json)


from flask import Blueprint, jsonify
from servicios.gestorNobel import GestorNobel


nobel_bp = Blueprint("nobel", __name__)
gestorNobel = GestorNobel()


@nobel_bp.route("/api/nobel")
def obtener_nobels():
    nobels = [
        {
            "nombre": autor.nombre,
            "nacionalidad": autor.nacionalidad,
            "motivo": autor.motivo,
            "anio": autor.anio
        }
        for autor in gestorNobel.autores
    ]
    return jsonify(nobels)
