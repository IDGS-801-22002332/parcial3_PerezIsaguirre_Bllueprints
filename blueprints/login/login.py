from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
import forms
from models import db, Usuarios

login_bp = Blueprint("login", __name__, url_prefix="/login")

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:  
        return redirect(url_for("pedidos.pizza"))

    classuser = forms.UsuarioFrom(request.form)

    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasenia = request.form["contrasenia"]

        user = Usuarios.query.filter_by(usuario=usuario).first()

        if user and user.contrasenia == contrasenia:
            login_user(user)
            session["user_id"] = user.id
            
            if user.rol == "cliente":
                return redirect(url_for("pedidos.pizza"))
            else:
                return redirect(url_for("proveedores.gestionar_proveedores"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
            return redirect(url_for("login.login"))

    return render_template("index.html", form=classuser)


@login_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    classuser = forms.UsuarioFrom(request.form)
    if request.method == 'POST':
        nombre = request.form.get('floating_first_name')
        apellido = request.form.get('floating_last_name')
        telefono = request.form.get('floating_phone')
        correo = request.form.get('floating_email')
        usuario = request.form.get('floating_usuario')  
        contrasenia = request.form.get('floating_password')
        rol = 'cliente' 

        if Usuarios.query.filter_by(usuario=usuario).first():
            flash('El nombre de usuario ya existe. Intenta con otro.', 'danger')
            return redirect(url_for('login.registro'))

        if Usuarios.query.filter_by(correo=correo).first():
            flash('El correo ya está registrado.', 'danger')
            return redirect(url_for('login.registro'))

        nuevo_usuario = Usuarios(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            correo=correo,
            usuario=usuario,
            contrasenia=contrasenia,
            rol=rol  
        )

        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Cuenta creada con éxito. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrió un error: {str(e)}', 'danger')

    return render_template('cuenta.html', form=classuser)



@login_bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("login.login"))
