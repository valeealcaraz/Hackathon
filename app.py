#_*_ coding:utf-8 _*_
    



"""
integrantes: Vale, fede, ale ,adolfo, vero
fecha: 10-2-2019
fecha de ultima edicion: 14 de mayo del 2019
descripcion: Es un sistema de inscripcion para animales, regalo para mi papá, tiene
ciertos campos a rellenar para tener el historial de los animales, faltan muchas funcionalidades
pero lo basico ya tiene. 


"""


from flask import Flask, render_template, json, request
import sqlite3 as sql 

app=Flask(__name__)

nombre_db="base_datos3.db"   #nombre de la base de datos

@app.route('/')
def main():
    return render_template('Flexor/index.html')


@app.route('/showHome')
def showHome():
    return render_template('index.html') 

@app.route('/ingresar',methods=['POST','GET'])
def ingresar():
    return render_template('ingresar.html')

@app.route('/showSignUp',methods=['POST','GET'])
def showSignUp():
    return render_template('signup.html')

@app.route('/formulario')
def formulario():
    js=lista()    #llamamos a la funcion para retornar del lado del cliente datos par el formulario
    return render_template('registro.html',dato=js)

@app.route('/registro', methods=['POST','GET'])      # aca es para registrar al animal
def registro():
    if request.method=='POST':   
        try:
            Id=request.form['Id']                         #identificativo del animal
            nombre=request.form['inputName']             #esta es la raza en realidad 
            peso=request.form['peso']
            dosis=request.form['dosis']
            ultimafecha=request.form['ultimaFecha']
            vacunas=request.form['vacunas']  
            datos=[Id,nombre,peso,dosis,ultimafecha,vacunas]  # esto es para meter en la db luego
            with sql.connect(nombre_db) as con:        
                cur = con.cursor()
<<<<<<< HEAD
                cur.execute('''CREATE TABLE IF NOT EXISTS animales (
                                        Id integer ,
                                        Nombre text,                                        
                                        Peso integer NOT NULL,
                                        Dosis text NOT NULL,
                                        Ultimafecha text,
                                        Vacunas text
=======
                cur.execute('''CREATE TABLE IF NOT EXISTS servicios (
                                        Servicio name ,
                                        Descripcion_del_producto text,                                        
                                        Horas_por_semana integer NOT NULL,
                                        Precio_por_hora integer NOT NULL,
                                        Contacto number,
                                        Correo text
>>>>>>> 36b3357086faa8250e5974ea21cbfe4550f3d502
                                    );'''
                       )
                cur.execute('''INSERT INTO animales (Servicio,Descripcion_del_producto,Horas_por_semana,Precio_por_hora,Contacto,Correo) VALUES (?,?,?,?,?,?);''', datos )
            
                con.commit()   
             
        except:
            con.rollback()

        finally:
            con.close()# cerramos la conexion de la base de datos 
            js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('list.html',dato=js)
            


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    return render_template('signup.html')
    

@app.route('/list')
def list():
   con = sql.connect(nombre_db)   
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from servicios")  #seleccionamos todos los datos de la tabla animales
  
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)
    
@app.route('/consulta')
def consulta():
   return render_template("consulta.html")

@app.route('/consulta_id',methods=['POST','GET']) #esto es para la consulta por un animal (individual)
def consulta_id():
    columna=[]                                   #creo una lista vacía
    if request.method=='POST':                   
        variable=request.form['inputName']      #guardamos para luego buscar en la base de datos
        con = sql.connect(nombre_db)            #conectamos a la base de datos
        con.row_factory = sql.Row               #confirmamos para que los datos que se consulte estén en fila
    
        cur = con.cursor()
        cur.execute("select * from animales")   #hacemos la consulta y seleccionamos TODOS los datos de la base de dato
    
        rows = cur.fetchall()                
        for i in rows:                   #recorremos la lista dentro de otra lista que está en rows
            if variable==str(i["Id"]):   #si coincide con la consulta, agregamos lo que se consulto 
                columna.append(i)        #con append agregamos lo que se consultó en la base de datos, solo cuando coincide lo que se le metio en la consulta desde el html 
        
        return render_template("lista_id.html",Identificativo=variable,columna=columna)


def lista():
   try:
       con = sql.connect(nombre_db)
       con.row_factory = sql.Row  
       cur = con.cursor()
       cur.execute("select * from animales")
       dato = cur.fetchall()     #cargamos toda la info de la db en la variable dato
       razas=[]                   #lista para almacenar datos de razas 
       id=[]
       for a in dato:
          id.append(a[0])    #usamos la posicion 0 ya que ahi se encuentra el id
       for a in dato:
          razas.append(a[1])   #usamos la posicion 1 ya que ahi se encuentran las razas 
                            # en la siguiente linea formateamos en json para luego formatear del lado del cliente en js 
       js={
            'Id': id, 
        'razas': razas
        
        }
       return js   
   except:            #si tiene problemas puede ser porque no existe la base de datos
       with sql.connect(nombre_db) as con:        
           cur = con.cursor()
           cur.execute('''CREATE TABLE IF NOT EXISTS servicios (
                                        Servicio name ,
                                        Descripcion del producto text,                                        
                                        Horas por semana integer NOT NULL,
                                        Precio por hora integer NOT NULL,
                                        Contacto number,
                                        Correo text
                                    );'''
                       )
           js={
             'Servicio': " ",  
                 'Descripcion del producto': " "

            }
       return js

if __name__ == "__main__":
    app.run(debug=True)
