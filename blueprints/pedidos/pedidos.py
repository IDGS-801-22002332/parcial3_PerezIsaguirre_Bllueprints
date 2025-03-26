from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required
import forms
from models import db, Pedido
import os

pedidos_bp = Blueprint("pedidos", __name__, url_prefix="/pedidos")

PEDIDOS_FILE = "pedidos.txt"

def leer_pedidos():
    pedidos = []
    cliente = {"nombre": "", "direccion": "", "telefono": ""}

    if os.path.exists(PEDIDOS_FILE):
        with open(PEDIDOS_FILE, "r") as file:
            lineas = file.readlines()
            if lineas:
                datos_cliente = lineas[0].strip().split("|")
                if len(datos_cliente) == 3:
                    cliente = {"nombre": datos_cliente[0], "direccion": datos_cliente[1], "telefono": datos_cliente[2]}
                for linea in lineas[1:]:
                    datos_pedido = linea.strip().split("|")
                    if len(datos_pedido) == 5:
                        pedidos.append({
                            "tamanio": datos_pedido[0],
                            "ingredientes": datos_pedido[1],
                            "num_pizzas": datos_pedido[2],
                            "precio_unitario": datos_pedido[3],
                            "subtotal": datos_pedido[4]
                        })
    
    return cliente, pedidos

@pedidos_bp.route("/pizzas", methods=["GET", "POST"])
@login_required
def pizza():
    if "user_id" not in session:
        flash("Ingrese su usuario y contraseña para poder ingresar", "warning")
        return redirect(url_for("login.login"))
    
    pizza_class = forms.PizzaForm(request.form)
    cliente, pedidos = leer_pedidos()

    precios_pizza = {"Chica": 40, "Mediana": 80, "Grande": 120}
    precios_ingredientes = {"jamon": 10, "piña": 10, "champiñones": 10}

    cliente_reciente = db.session.query(Pedido).order_by(Pedido.id.desc()).first()
    subtotal_total = db.session.query(db.func.sum(Pedido.subtotal)).scalar() or 0

    if request.method == "POST":
        if "btnAgregar" in request.form:
            tamanio = pizza_class.tamanio.data
            ingredientes = pizza_class.ingredientes.data
            num_pizzas = int(pizza_class.numPizzas.data)

            precio_pizza = precios_pizza.get(tamanio, 0)
            precio_ingredientes_total = sum(precios_ingredientes.get(ing, 0) for ing in ingredientes)
            precio_unitario = precio_pizza + precio_ingredientes_total
            subtotal = precio_unitario * num_pizzas

            pedido = {
                "tamanio": tamanio,
                "ingredientes": ", ".join(ingredientes),
                "num_pizzas": str(num_pizzas),
                "precio_unitario": f"${precio_unitario}",
                "subtotal": f"${subtotal}"
            }

            pedidos.append(pedido)

        elif "btnTerminar" in request.form:
            total = sum(float(p["subtotal"].replace("$", "")) for p in pedidos)

            for p in pedidos:
                nuevo_pedido = Pedido(
                    nombre=cliente["nombre"],
                    direccion=cliente["direccion"],
                    telefono=cliente["telefono"],
                    tamanio=p["tamanio"],
                    ingredientes=p["ingredientes"],
                    num_pizzas=int(p["num_pizzas"]),
                    precio_unitario=float(p["precio_unitario"].replace("$", "")),
                    subtotal=float(p["subtotal"].replace("$", ""))
                )
                db.session.add(nuevo_pedido)

            db.session.commit()

            flash(f"Su pedido fue realizado. Su total es de: ${total}", "success")
            return redirect("/")

    return render_template("pizzas.html", form=pizza_class, cliente_reciente=cliente_reciente, subtotal_total=subtotal_total, pedidos=pedidos)
