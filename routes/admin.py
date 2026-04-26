# esta ruta es para el login


from flask import Blueprint, json, jsonify, request


admin_bp = Blueprint("admin", __name__)

ADMINS = {
    "admin": "12345",
    "biblioteca": "sanfe2025"
}


@admin_bp.route("/api/login", methods=["POST"])
def login():
    datos = request.get_json()
    usuario = datos.get("usuario")
    password = datos.get("password")

    if usuario in ADMINS and ADMINS[usuario] == password:
        return jsonify({"ok": True, "mensaje": "Bienvenido"})
    else:
        return jsonify({"ok": False, "mensaje": "Usuario o contraseña incorrecta"}), 401
