CREATE TABLE IF NOT EXISTS usuario (
	id_usuario integer primary key autoincrement, 
	username text not null, 
	password text not null, 
	nombre text, 
	telefono integer, 
	mail text, 
	ciudad text,
	lugar text
);

CREATE TABLE IF NOT EXISTS perro (
	id_perro integer primary key autoincrement,
	id_usuario integer not null, 
	nombre text, 
	raza text, 
	edad integer, 
	sexo text, 
	foto text)

##nada faltan los datos