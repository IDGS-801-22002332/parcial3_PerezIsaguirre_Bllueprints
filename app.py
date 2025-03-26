from flask import Flask
from models import db
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from blueprints.login.login import login_bp 
from blueprints.pedidos.pedidos import pedidos_bp
from blueprints.proveedores.proveedores import proveedores_bp
from models import Usuarios 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csr = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(pedidos_bp)
app.register_blueprint(proveedores_bp)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))  

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)
