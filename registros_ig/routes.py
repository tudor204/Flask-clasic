from registros_ig import app

@app.route("/")
def hello():
    return "Hola, ésto es flask clasic"
           