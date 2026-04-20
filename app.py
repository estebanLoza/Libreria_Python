# Este archivo sirve para el llamado de flask con los datos que tengo para mostrarlos
# la páqina web.


from flask import Flask
from flask_cors import CORS


from routes.libro import libro_bp
# from routes.nobel import nobel_bp
# from routes.usuarios import usuarios_bp
# from routes.admin import admin_bp
#

app = Flask(__name__)

CORS(app)


app.register_blueprint(libro_bp)
# app.register_blueprint(nobel_bp)
# app.register_blueprint(usuarios_bp)
# app.register_blueprint(admin_bp)
#

if __name__ == "__main__":
    app.run(debug=True)
