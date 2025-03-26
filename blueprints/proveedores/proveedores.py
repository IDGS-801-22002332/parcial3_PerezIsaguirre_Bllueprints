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
            usuario=usuario,
            contrasenia=contrasenia,
            rol="proveedor"
        )

        try:
            db.session.add(nuevo_usuario)
            db.session.commit()

            nuevo_proveedor = Proveedores(
                nombre=nombre,
                contacto=contacto,
                empresa=empresa,
                telefono=telefono,
                correo=correo,
                direccion=direccion,
                rfc=rfc,
                usuario=usuario,
                contrasenia=contrasenia,
                usuario_id=nuevo_usuario.id 
            )

            db.session.add(nuevo_proveedor)
            db.session.commit()

            return redirect(url_for('proveedores.gestionar_proveedores'))
        except Exception as e:
            db.session.rollback()
            flash("Error al registrar el proveedor", "danger")

    proveedores = Proveedores.query.all()
    return render_template('proveedores.html', form=form, proveedores=proveedores)


@proveedores_bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Has cerrado sesión correctamente", "success")
    return redirect(url_for("login.login")) 