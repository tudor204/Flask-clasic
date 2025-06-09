from registros_ig.conexion import Conexion

def select_all():
    conectar = Conexion("select * from movements order by date DESC")    
    filas = conectar.res.fetchall()
    columnas = conectar.res.description #columnas
    lista_diccionario=[]  

    for f in filas:
        diccionario={}    
        posicion=0
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1
        lista_diccionario.append(diccionario)
    conectar.con.close()
    return lista_diccionario
   
def insert(registroForm):
    conectarInsert = Conexion("insert into movements(date,concept,quantity) values(?,?,?)",registroForm)    
    conectarInsert.con.commit()#funcion para validar el registro
    conectarInsert.con.close()

def select_by(id):
    conectarSelect = Conexion(f"SELECT * from movements WHERE id={id}")    
    resultado = conectarSelect.res.fetchall()
    conectarSelect.con.close()
    return resultado[0]

def delete_by(id):
    conectarDelete = Conexion(f"DELETE FROM movements WHERE id={id}")    
    conectarDelete.con.commit()#funcion para validar el registro
    conectarDelete.con.close()

def update_by(id, date, concept, quantity):
    conectarUpdate = Conexion("""
        UPDATE movements
        SET date = ?, concept = ?, quantity = ?
        WHERE id = ?
    """, (date, concept, quantity, id))    
    conectarUpdate.con.commit()
    conectarUpdate.con.close()

  