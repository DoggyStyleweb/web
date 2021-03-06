# -*- coding:utf-8 -*-
from sqlite3 import dbapi2 as sqlite3
from flask import * #####
from flask import make_response ##INCLUI ESTO
from flask import redirect####
from werkzeug import secure_filename #####
from flask import (
	Flask, 
	render_template, 
	request,
	url_for
	)

app=Flask(__name__)

#conexion con la base de datos
def connect_db():
	"""retorna una coexion a DB"""
	path_to_db='proyecto.db'
	rv=sqlite3.connect(path_to_db)
	rv.row_factory=sqlite3.Row
	return rv

def init_db():
	"""crear la tabla"""
	db=connect_db()
	with app.open_resource('schema.sql',mode='r')as f:
		db.cursor().executescript(f.read())
	db.commit()
	db.close()

#rutas
@app.route('/', methods=['GET','POST'])
def show_entries():
	if request.method=='GET':
		return render_template('log.html')
	elif request.method=='POST':
		usuario=request.form['username']
		pas=request.form['password']
		db=connect_db()
		cur=db.execute('SELECT username,password from usuario where username =? and password=?',[usuario,pas])
		entries=cur.fetchall()
		c=len(entries)
		if c>0:
			return inicio()
	else:
		return render_template('log.html')


@app.route('/amigos')
def inicio():
	db=connect_db()
	cur=db.execute('SELECT * FROM perro')
	entries=cur.fetchall()
	db.close()
	return render_template('welcome.html', entries=entries)


@app.route('/buscandoamor')
def buscandoamor():
	db=connect_db()
	cur=db.execute('SELECT username, lugar FROM usuario where  lugar="saval" ')
	entries=cur.fetchall()
	db.close()
	return render_template('buscandoamor.html', entries=entries)

@app.route('/filtro', methods=['POST'])
def filtro(): 
	sexo = request.form['sexo']
	raza = request.form['raza']
	ciudad = request.form['ciudad']
	db = connect_db()
	cur=db.execute('select perro.nombre, usuario.username, usuario.nombre, usuario.telefono from perro,usuario where perro.id_usuario=usuario.id_usuario and sexo=? and raza=? and ciudad= ?', 
	                            [sexo,raza,ciudad])
	entries=cur.fetchall()
	db.commit()
	return render_template('filtro.html', entries=entries)

@app.route('/registro/usuario', methods=['GET','POST'])
def registro():
	if request.method=='GET':
		return render_template('register.html')
	elif request.method=='POST':
		username=request.form['user']
		password=request.form['pass']
		nombre=request.form['nombre']
		telefono=request.form['telefono']
		mail=request.form['mail']
		ciudad=request.form['ciudad']
		lugar=request.form['lugar']
		db=connect_db()
		db.execute('INSERT INTO usuario (username, password, nombre, telefono, mail, ciudad, lugar) VALUES (?,?,?,?,?,?,?)',[username, password, nombre, telefono, mail, ciudad, lugar])
		db.commit()
		db.close()
		return redirect(url_for('registro2'))
	else:
		return "Acceso denegado"

@app.route('/registro/mascota', methods=['GET','POST'])
def registro2():
	
	if request.method=='GET':
		return render_template('registerPet.html')
	elif request.method=='POST':
		id_usuario=11
		nombre=request.form['nombre']
		raza=request.form['raza']
		edad=request.form['edad']
		sexo=request.form['sexo']
		foto="mifoto.jpg"
		db=connect_db()
		db.execute('INSERT INTO perro (id_usuario, nombre, raza, edad, sexo, foto) VALUES (?,?,?,?,?,?)',[id_usuario, nombre, raza, edad, sexo, foto])
		db.commit()
		db.close()
		return render_template('registerSuccess.html')
	else:
		return "Acceso denegado"


@app.route('/registro/success')
def registro3():
	return render_template('registerSuccess.html')

if __name__=="__main__":
	app.run(debug=True)
