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

/*
insert into user (name, user, pass, salt) values ("admin", "admin", "d6b62840b2861dbf0a17552a0900e433fc7bfaa4a9052d0239d0f032", "zJhgt");
insert into user (name, user, pass, salt) values ("Boris Sotomayor", "bsotomayor", "17aeb496d5e7ef8fd13017715854f52293379155c53128902f8e2477", "UlMQc");
*/