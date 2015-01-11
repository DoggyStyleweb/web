# -*- coding:utf-8 -*-
from sqlite3 import dbapi2 as sqlite3
from flask import (
	Flask, 
	render_template, 
	request
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
@app.route('/')
def show_entries():
	return render_template('log.html')

@app.route('/amigos')
def inicio():
	db=connect_db()
	cur=db.execute('SELECT username, lugar FROM usuario')
	entries=cur.fetchall()
	db.close()
	return render_template('welcome.html', entries=entries)



if __name__=="__main__":
	app.run(debug=True)
