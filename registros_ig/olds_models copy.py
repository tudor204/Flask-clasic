import sqlite3
from registros_ig import ORIGIN_DATA

def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("select * from movements;")
    filas = res.fetchall()
    columnas = res.description #columnas
    lista_diccionario=[]  

    for f in filas:
        diccionario={}    
        posicion=0
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1
        lista_diccionario.append(diccionario)
    con.close()
    return lista_diccionario
   
def insert(registroForm):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("insert into movements(date,concept,quantity) values(?,?,?)",registroForm)
    con.commit()#funcion para validar el registro
    con.close()

def select_by(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute(f"SELECT * from movements WHERE id={id}")
    
    resultado = res.fetchall()
    con.close()
    return resultado[0]

def delete_by(id):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    cur.execute(f"DELETE FROM movements WHERE id={id}")
    con.commit()#funcion para validar el registro
    con.close()

def update_by(id, date, concept, quantity):
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    cur.execute("""
        UPDATE movements
        SET date = ?, concept = ?, quantity = ?
        WHERE id = ?
    """, (date, concept, quantity, id))
    con.commit()
    con.close()

  