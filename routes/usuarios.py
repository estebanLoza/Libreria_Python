from flask import Blueprint, json, jsonify
from servicios.gestorUsuarios import GestorUsuarios



usuarios_bp = Blueprint("usuarios", __name__)
gestorUsuarios = GestorUsuarios()


@usuarios_bp.route("/api/usuarios")
def obtener_usuarios():
    usuarios = [
        {
            "nombre": usuario.nombre,
            "id":   usuario.id,
            "librosPrestados": [
                {
                    "libro":   prestamo.libro,
                    "fecha_vencimiento": str(prestamo.fecha_vencimiento)
                }
                for prestamo in usuario.librosPrestados
            ]
        }
        for usuario in gestorUsuarios.usuarios
    ]
    return jsonify(usuarios)

@usuarios_bp.route("/api/usuarios/vencidos")
def obtener_vencidos():
    vencidos = []

    for usuario in gestorUsuarios.usuarios:
        for prestamo in usuario.librosPrestados:
            if prestamo.esta_vencido():
                vencidos.append({
                    "nombre":                   usuario.nombre,
                    "libro":                    prestamo.libro,
                    "fecha_vencimiento":        str(prestamo.fecha_vencimiento)
                })

    return jsonify(vencidos)


