from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, IntegerField, RadioField, SelectMultipleField
from wtforms import validators

class PizzaForm(Form):
    nombre=StringField("Nombre",[
        validators.DataRequired(message='Ingrese su nombre correctamente')
    ])
    direccion=StringField("Direccion",[
        validators.DataRequired(message='Ingrese su direccion correctamente')
    ])
    telefono=StringField("Telefono",[
        validators.DataRequired(message='Ingrese su telefono correctamente')
    ])
    
    tamanio = RadioField("", [
        validators.DataRequired(message="El tamaño es requerido")
    ], choices=[
        ('Chica', 'Chica $40'),
        ('Mediana', 'Mediana $80'),
        ('Grande', 'Grande $120')
    ])
    ingredientes = SelectMultipleField("", [
        validators.DataRequired(message="Los Ingredientes son requeridos")
    ], choices=[
        ('jamon', 'Jamón $10'),
        ('piña', 'Piña $10'),
        ('champiñones', 'Champiñones $10')
    ])
    
    numPizzas = IntegerField("", [
        validators.DataRequired(message='El número de pizzas a comprar es requerido')
    ])
    dia=StringField("Dia",[
        validators.DataRequired(message='El dia es requerido')
    ])
    mes=StringField("Mes",[
        validators.DataRequired(message='El mes es requerido')
    ])
    anio=StringField("Año",[
        validators.DataRequired(message='El año es requerido')
    ])
    
class ProveedorForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="Ingrese el nombre del proveedor")
    ])
    
    contacto = StringField("Contacto", [
        validators.DataRequired(message="Ingrese el nombre de contacto")
    ])
    
    telefono = StringField("Teléfono", [
        validators.DataRequired(message="Ingrese un número de teléfono")
    ])
    
    correo = EmailField("Correo", [
        validators.DataRequired(message="Ingrese un correo válido")
    ])
    
    direccion = StringField("Dirección", [
        validators.DataRequired(message="Ingrese la dirección del proveedor")
    ])
    
    empresa = StringField("Empresa", [
        validators.DataRequired(message="Ingrese el nombre de la empresa")
    ])
    
    rfc = StringField("RFC", [
        validators.DataRequired(message="Ingrese el RFC del proveedor")
    ])
    
    usuario=StringField("Usuario",[
        validators.DataRequired(message='El usuario es requerido')
    ])
    
    contrasenia= PasswordField("Contraseña", [
        validators.DataRequired(message="Ingrese una contraseña")
    ])

class UsuarioFrom(Form):
    usuario=StringField("Usuario",[
        validators.DataRequired(message='El usuario es requerido')
    ])
    contrasenia=PasswordField("Contrasenia",[
        validators.DataRequired(message='La contraseña es requerida')
    ])
    submit=SubmitField("Ingresar")