from registros_ig import app
from flask import render_template
from registros_ig.models import *

@app.route("/")
def index():

    registros= select_all()
    """
    datos_movimiento = [
        {"id":1,"date":"2025-06-06","concepto":"sueldo","quantity":"1600€"},
        {"id":2,"date":"2025-06-05","concepto":"Luz","quantity":"-100"},
        {"id":3,"date":"2025-06-04","concepto":"Teléfono","quantity":"-40"},
        {"id":4,"date":"2025-06-03","concepto":"Gas","quantity":"-25"},
    ]
    """

    return render_template("index.html",data = registros)
           