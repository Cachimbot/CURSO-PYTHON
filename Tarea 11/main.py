import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Joseph', 'Arroyo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Aranza', 'Juarez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Pepito', 'Perez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Scarlet', 'Paredes')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Pablo', 'Santamaria')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Iris', 'Fazz')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Smith', 'Valencia')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Cachimbot', 'Botcito')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Joseph'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()