from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    dia = db.Column(db.String(20), nullable=False)
    mes = db.Column(db.String(20), nullable=False)
    anio = db.Column(db.String(20), nullable=False)
    tamanio = db.Column(db.String(50), nullable=False)
    ingredientes = db.Column(db.String(255), nullable=False)
    num_pizzas = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

class Usuarios(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(100))
    correo = db.Column(db.String(100), unique=True)
    contacto = db.Column(db.String(100))
    rol = db.Column(db.String(100))
    rfc = db.Column(db.String(20))
    empresa = db.Column(db.String(100))
    usuario = db.Column(db.String(100), unique=True)
    contrasenia = db.Column(db.String(100))


class Proveedores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(100))
    direccion = db.Column(db.Text)
    empresa = db.Column(db.String(100))
    rfc = db.Column(db.String(20))
    rol = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    contrasenia = db.Column(db.String(100), nullable=False)
