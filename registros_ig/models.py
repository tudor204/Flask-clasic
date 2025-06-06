import sqlite3

def select_all():
    con = sqlite3.connect("data/movimientos.sqlite")
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

    return lista_diccionario
   
