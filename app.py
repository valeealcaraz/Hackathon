#_*_ coding:utf-8 _*_
    

"""
integrantes: Vale, fede, ale ,adolfo, vero
fecha: 10-2-2019
fecha de ultima edicion: 14 de mayo del 2019
descripcion: Es un sistema de inscripcion para servicios tiene
ciertos campos a rellenar para tener el historial de los servicios, faltan muchas funcionalidades
pero lo basico ya tiene. 
"""



from flask import Flask, render_template, json, request
import sqlite3 as sql 

app=Flask(__name__, static_url_path='')

nombre_db="base_datos3.db"   #nombre de la base de datos

@app.route('/') #pagina principal, retorna a index.html
def main():
    print("adfdsdf")
    return render_template('index.html')


@app.route('/showHome')
def showHome():
    return render_template('index.html')  


@app.route('/ingresar',methods=['POST','GET'])
def ingresar():
    return render_template('ingresar.html')

@app.route('/showlogin',methods=['POST','GET'])
def showlogin():
    return render_template('login.html')

@app.route('/formulario')
def formulario():
    js=lista_servicios()    #llamamos a la funcion para retornar del lado del cliente datos par el formulario
    return render_template('registro.html',dato=js)

@app.route('/registro', methods=['POST','GET'])      # aca es para registrar al animal
def registro():
    if request.method=='POST':   
        try:
            Servicio_Producto=request.form['Servicio']                         #identificativo del servicio
            Descripcion_del_producto=request.form['Descripcion del producto']             #descripcion del servicio 
            Horas_por_semana=request.form['Horas por semana']  #cuantas horas por semana
            Precio_por_hora=request.form['Precio por hora'] #precio por hora o servicio por servicio
            Numero_de_telefono=request.form['Contacto'] #contacto
            Correo=request.form['Correo']  
            datos=[Servicio_Producto,Descripcion_del_producto,Horas_por_semana,Precio_por_hora,Numero_de_telefono,Correo]  # esto es para meter en la db luego
            print(datos)
            with sql.connect(nombre_db) as con:
                    
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS servicios (
                                        Servicio text,
                                        Descripcion_del_producto text,                                        
                                        Horas_por_semana integer NOT NULL,
                                        Precio_por_hora integer NOT NULL,
                                        Contacto number,
                                        Correo text
                                    );"""
                       )
                cur.execute('''INSERT INTO servicios (Servicio,Descripcion_del_producto,Horas_por_semana,Precio_por_hora,Contacto,Correo) VALUES (?,?,?,?,?,?);''', datos )
            
                con.commit()   
             
        except sql.Error as e:
            print(e)
            con.rollback()

        finally:
            con.close()# cerramos la conexion de la base de datos 
            js=lista_servicios()   #retornamos datos de la db para el form del lado del cliente
            return render_template('registro.html',dato=js)
            

@app.route('/registro_usuario')
def register():
    return render_template('registro_usuario.html')



@app.route('/lista_servicios')
def lista_servicios():
   con = sql.connect(nombre_db)   
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from servicios")  #seleccionamos todos los datos de la tabla animales
  
   
   rows = cur.fetchall()
   print(rows)
   return render_template("lista_servicios.html",rows = rows)

@app.route('/lista_usuarios')
def lista_usuarios():
   con = sql.connect(nombre_db)   
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from registro")  #seleccionamos todos los datos de la tabla animales
   
   rows = cur.fetchall()
   print(rows)
   return render_template("lista_usuarios.html",rows = rows)

@app.route('/consulta')
def consulta():
   return render_template("consulta.html")

@app.route('/consulta_servicio',methods=['POST','GET']) #esto es para la consulta por un serivico (individual)
def consulta_servicio():
    columna=[]                                   #creo una lista vacía
    if request.method=='POST':                   
        variable=request.form['inputName']      #guardamos para luego buscar en la base de datos
        print(type(variable))
        con = sql.connect(nombre_db)            #conectamos a la base de datos
        con.row_factory = sql.Row               #confirmamos para que los datos que se consulte estén en fila
    
        cur = con.cursor()
        cur.execute("select * from servicios")   #hacemos la consulta y seleccionamos TODOS los datos de la base de dato
    
        rows = cur.fetchall()                
        for i in rows:                   #recorremos la lista dentro de otra lista que está en rows
            if variable==str(i["Servicio"]):   #si coincide con la consulta, agregamos lo que se consulto 
                columna.append(i)        #con append agregamos lo que se consultó en la base de datos, solo cuando coincide lo que se le metio en la consulta desde el html 
        
        return render_template("consulta_servicio.html",Identificativo=variable,columna=columna)



@app.route('/registro_usuario', methods=['POST','GET'])      # aca es para registrar al usuario
def registro_usuario():
    if request.method=='POST':   
        try:
            Usuario=request.form['Username']                         #nombre de usuario
            Nombre_usuario=request.form['Nombre']             #descripcion del servicio 
            Apellido_usuario=request.form['Apellido']
            Nacimiento=request.form['Fecha_de_Nacimiento']  #input para fecha de nacimiento
            Contrasenha=request.form['Contrasenha'] #Descripción de hobbies
            Numero_de_telefono=request.form['Telefono'] #contacto
            Correo=request.form['Correo']  
            print("hgfggf")
            datos=[Usuario,Nombre_usuario,Apellido_usuario,Nacimiento,Contrasenha,Numero_de_telefono,Correo]  # esto es para meter en la db luego
            print(datos)
            with sql.connect(nombre_db) as con:

                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS registro (
                                        Usuario text,
                                        Nombre_usuario text,  
                                        Apellido_usuario text,                                      
                                        Nacimiento integer NOT NULL,
                                        Contrasenha text,
                                        Numero_de_telefono integer NOT NULL,
                                        Correo text
                                    );"""
                       )
                cur.execute("""INSERT INTO registro (Usuario,Nombre_usuario,Apellido_usuario,Nacimiento,Contrasenha,Numero_de_telefono,Correo) VALUES (?,?,?,?,?,?,?);""", datos )
            
                con.commit()   
             
        except sql.Error as e:
            print(e)
            con.rollback()

        finally:
            con.close() #cerramos la conexion de la base de datos 
            js=lista_usuarios()   #retornamos datos de la db para el form del lado del cliente
            return render_template('registro_usuario.html',dato=js)

@app.route('/consulta')
def consulta_usuario():
   return render_template("consulta.html")

@app.route('/consulta_username',methods=['POST','GET']) #esto es para la consulta por un animal (individual)
def consulta_username():
    columna=[]                                   #creo una lista vacía
    if request.method=='POST':                   
        variable=request.form['inputName']      #guardamos para luego buscar en la base de datos
        con = sql.connect(nombre_db)            #conectamos a la base de datos
        con.row_factory = sql.Row               #confirmamos para que los datos que se consulte estén en fila
    
        cur = con.cursor()
        cur.execute("select * from registro")   #hacemos la consulta y seleccionamos TODOS los datos de la base de dato
    
        rows = cur.fetchall()                
        for i in rows:                   #recorremos la lista dentro de otra lista que está en rows
            if variable==str(i["Nombre_usuario"]):   #si coincide con la consulta, agregamos lo que se consulto 
                columna.append(i)        #con append agregamos lo que se consultó en la base de datos, solo cuando coincide lo que se le metio en la consulta desde el html 
        
        return render_template("consulta_username.html",Identificativo=variable,columna=columna)




if __name__ == "__main__":
    app.run(debug=True)


