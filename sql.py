import sqlite3

with sqlite3.connect("proyecto.db") as connection:
	con = connection.cursor();
	con.execute("DROP TABLE IF EXISTS usuario")
	con.execute("CREATE TABLE IF NOT EXISTS usuario (id_usuario integer primary key autoincrement, username text not null, password text not null, nombre text, telefono integer, mail text, ciudad text,lugar text);")
	con.execute('insert INTO usuario (username,password,nombre,telefono,mail,ciudad,lugar) values ("dany","1234","daniela amestica",123456,"damol_13@hotmail.com","valdivia","saval");')
	con.execute('insert INTO usuario (username,password,nombre,telefono,mail,ciudad,lugar) values ("seba","1234","sebastian hechenleitner",123456,"sebasth24@hotmail.com","valdivia","parque");')
	con.execute('insert INTO usuario (username,password,nombre,telefono,mail,ciudad,lugar) values ("pancho","1234","francisco bello",123456,"pancho_bello@hotmail.com","santiago","parque");')
	con.execute('insert INTO usuario (username,password,nombre,telefono,mail,ciudad,lugar) values ("kareen","1234","kareen hechenleitner",123456,"kareen@hotmail.com","providencia","parque");')

	con.execute("DROP TABLE IF EXISTS perro")
	con.execute("CREATE TABLE IF NOT EXISTS perro (id_perro integer primary key autoincrement,id_usuario integer not null, nombre text, raza text, edad integer, sexo text, foto text);")
	con.execute('insert INTO perro (id_usuario,nombre, raza,edad,sexo,foto) VALUES (1,"Dandy","yorkshire",2,"macho","mifoto.jpg");')
	con.execute('insert INTO perro (id_usuario,nombre, raza,edad,sexo,foto) VALUES (2,"Pola","labrador",4,"hembra","mifoto2.jpg");')
	con.execute('insert INTO perro (id_usuario,nombre, raza,edad,sexo,foto) VALUES (3,"Ross","samoyedo",1,"macho","mifoto3.jpg");')
	con.execute('insert INTO perro (id_usuario,nombre, raza,edad,sexo,foto) VALUES (4,"Oliver","buldog frances",1,"macho","mifoto4.jpg");')



