from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import logout_user, login_required, current_user
from models import db, Proveedores, Usuarios
import forms

proveedores_bp = Blueprint("proveedores", __name__, url_prefix="/proveedores")

@proveedores_bp.route('/proveedores', methods=['GET', 'POST'])
def gestionar_proveedores():
    form = forms.ProveedorForm(request.form)
    
    if request.method == 'POST' and form.validate():
        nombre = request.form.get('nombre')
        contacto = request.form.get('contacto')
        empresa = request.form.get('empresa')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        direccion = request.form.get('direccion')
        rfc = request.form.get('rfc')
        usuario = request.form.get('usuario')
        contrasenia = request.form.get('contrasenia')

        nuevo_usuario = Usuarios(
            nombre=nombre,
            apellido='', 
            telefono=telefono,
            correo=correo,
            contacto=contacto,
            rol="proveedor", 
            rfc=rfc,
            empresa=empresa,
            usuario=usuario,
            contrasenia=contrasenia
        )

        try:
            db.session.add(nuevo_usuario)
            db.session.commit()

            return redirect(url_for('proveedores.gestionar_proveedores'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error al registrar el proveedor: {str(e)}", "danger")

    proveedores = Usuarios.query.filter_by(rol='proveedor').all()
    
    return render_template('proveedores.html', form=form, proveedores=proveedores)



@proveedores_bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Has cerrado sesión correctamente", "success")
    return redirect(url_for("login.login")) 