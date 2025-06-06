from datetime import date
from registros_ig import app
from flask import render_template,request,redirect
from registros_ig.models import *


def validateForm(datosFormulario):
    errores=[]#lista para guardar errores
    hoy = date.today().isoformat()#capturo laf echa de hoy
    if datosFormulario["date"] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario["concept"] =="":
        errores.append("El concepto no puede ir vacío")
    if datosFormulario["quantity"] =="" or float(datosFormulario["quantity"]) == 0.0:
        errores.append("El precio debe ser distinto a 0 y de vacío")
    return errores

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

@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("create.html", dataForm=None)
    else:
        errores = validateForm(request.form)
        if errores:
            return render_template("create.html",msgError=errores,dataForm=request.form)
        else:
            insert([request.form["date"],request.form["concept"],request.form["quantity"]])
            return redirect("/")
        
@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method =="GET":
        resultado = select_by(id)
        return render_template("delete.html",data=resultado)
    else:
        delete_by(id)
        return redirect("/")

@app.route("/update/<id>",methods=["GET","POST"])
def edit(id):
    if request.method == "GET":
        resultado = edit(id)
        return render_template("update.html",data=resultado)
    else:
        edit(id)
        return redirect("/")
    


    

           