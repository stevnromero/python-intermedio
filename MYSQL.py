# CREAR UNA CONEXION MYSQL

"""import mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = " root",
    port = "3306",
    password = ""
)
print(conn.is_connected())"""


#CREAR LA BASE DE DATOS CON MYSQL

"""import mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = " root",
    port = "3306",
    password = ""
)
miCursor = conn.cursor()
miCursor.execute("CREATE DATABASE techno")"""


# COMPROBAR SI EXISTE LAS BASES DE DATOS MYSQL

"""mport mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = " root",
    port = "3306",
    password = ""
)
miCursor = conn.cursor()
miCursor.execute("SHOW DATABASES")

for database in miCursor:
    print(f"las bases de datos son: {database}")
"""

# CREAR TABLAS CON MYSQL
""""
import mysql.connector

data = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = data.cursor()
miCursor.execute("CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), apellido1 VARCHAR(100), apellido2 VARCHAR(100), ciudad VARCHAR(100), categoria INT)")
"""""
# Comprobar las tablas de la base de datos con MYSQL
"""miCursor.execute("SHOW TABLES")
for tables in miCursor:
    print(f"las tablas de la base de datos 'techno' son: {tables}")"""
"""
import mysql.connector

data = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = data.cursor() # creamos la llave foranea
miCursor.execute("CREATE TABLE productos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), precio decimal(10,2),  id_client INT(10), FOREIGN KEY (id_client) REFERENCES clientes (id))")"""

"""
miCursor.execute("SHOW TABLES")
for tables in miCursor:
    print(f"las tablas de la base de datos 'techno' son: {tables}")"""


# Insertar los valores de las tablas con MYSQL
"""
import mysql.connector

data = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = data.cursor()
sql = "INSERT INTO clientes (id, nombre, apellido1, apellido2, ciudad, categoria) VALUES (%s, %s,%s,%s,%s,%s)" #(%s, %s "contiene la cantida de valores en cada columna")
#valor = ("1", "Adela", "Salas", "Diaz", "Granada", 200)
#valor = ("6","Manuel", "OLiveros", "Salmon", "Bilbao", 150)
#insertar valores con executemany()
valor = [
    ("1","Adolfo","Rubio","Flores","Sevilla",300),
    ("2","Marcos","Loyota","Mendez","Almeria",250),
    ("3","Maria","Del Valle","Arjona","Barcelona",450),
    ("4","Daniel","Salamanca","Paez","Madrid",320)
]
#miCursor.execute(sql,valor)
miCursor.executemany(sql,valor)
data.commit()
print("1 record inserted, ID:", miCursor.lastrowid)
data.close()"""

"""
import mysql.connector

data = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = data.cursor()
sql = "INSERT INTO productos (id,nombre, precio, id_client) VALUES (%s,%s,%s,%s)"
valor = [
    (1,"Disco duro SATA3 1TB", 86.99, 1),
    (2,"Portatil Yoga 520", 59.34, 2),
    (3,"Portatil Ideapd 320", 44.19, 3),
    (4,"Impresora HP Deskjet 3720", 61.09, 4)
]
miCursor.executemany(sql, valor)
data.commit()
print(f"1 record inserted, ID: {miCursor.lastrowid}" )
data.close()
"""

# SELECCION DE MYSQL


# TAMBIEN SE PUEDEN SELECCIONAR ALGUNAS DE LAS COLUMNAS PARA DEVOLVER LOS ATRIBUTOS
"""import mysql.connector

conect = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)"""

"""miCursor = conect.cursor() 
miCursor.execute("SELECT nombre, apellido1 FROM clientes")
myresult = miCursor.fetchall()

for selected in myresult:
    print(f"los datos de la tabla clientes son: {selected}")"""

"""miCursor = conect.cursor()
miCursor.execute(""""SELECT * FROM productos"")"
"""myresult = miCursor.fetchall()
for selected2 in myresult:
    print(f"los datos de la tabla productos son: {selected2}")"""

# Utilizamos fetchone() para devolver la primera fila
"""miresultado = miCursor.fetchone()
print(miresultado)
for cow in miresultado:
    print(f"los datos de la primera fila de la tabla productos son: {cow} ")"""


# MYSQL DONDE

"""import mysql.connector

conect = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = conect.cursor()
sql = f"SELECT * FROM clientes WHERE ciudad LIKE '%ona%' "
miCursor.execute(sql)
resultado = miCursor.fetchall()

for filtracion in resultado:
    print(f"los nombres y apellidos de esta tabla son: {filtracion}")

miCursor.close()"""

# ORDENAR ASC Y DESC EN MYSQL

"""import mysql.connector

order = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = order.cursor()
sql = f"SELECT * FROM clientes ORDER BY ciudad ASC"
miCursor.execute(sql)
resultado = miCursor.fetchall()
order.commit()
order.close()

for ordering in resultado:
    print(ordering)
    continue"""

"""
import mysql.connector

order = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = order.cursor()
sql = f"SELECT nombre, ciudad FROM clientes ORDER BY nombre DESC"
miCursor.execute(sql)
resultado = miCursor.fetchall()
order.commit()
order.close()

for ordering in resultado:
    print(ordering)
    continue"""
   
# eliminar registros de una tabla existente EN MYSQL

"""import mysql.connector

delete_register = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = delete_register.cursor()
sql = "DELETE FROM productos WHERE id = 4"
miCursor.execute(sql)
delete_register.commit()
print(miCursor.rowcount, "eliminacion exitosa!")
"""

# eliminar la tabla existente en MYSQL
"""""
import mysql.connector

delete_table = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)"""""

#miCursor = delete_table.cursor()
#sql = "DROP TABLE IF EXISTS productos"""
"""miCursor.execute(sql)
print(miCursor.rowcount, "tabla eliminada!")
delete_table.commit()
delete_table.close()"""



# ACTUALIZAR TABLA EN BD CON MYSQL

"""import mysql.connector

Uptading = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = Uptading.cursor()
SQL = "UPDATE productos SET nombre = 'GeForce GTX 1050Ti' WHERE id = 2"
#SQL = "UPDATE productos SET nombre = %s WHERE id = %s"
#nuevo = ('Monitor 24 LED Full HD', '3')
miCursor.execute(SQL)
Uptading.commit()
Uptading.close()
print(miCursor.rowcount, "actualizacion acertada!")"""

# LIMITAR DATOS MYSQL

"""import mysql.connector

limit = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = limit.cursor()
miCursor.execute("SELECT * FROM clientes LIMIT 3")
resultado = miCursor.fetchall()
for x in resultado:
    print(x)"""

# EMPEZANDO DESDE OTRA POSICION UTILIZANDO OFFSET MYSQL

"""import mysql.connector
limit = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = limit.cursor()
miCursor.execute("SELECT * FROM productos LIMIT 5 OFFSET 3")
resultado = miCursor.fetchall()
for x in resultado:
    print(x)"""


# UNIONES EN MYSQL

# INNER JOIN

"""import mysql.connector

inner = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = inner.cursor()
SQL = "SELECT * from clientes INNER JOIN productos p ON clientes.categoria = p.id_client"
miCursor.execute(SQL)
resultado = miCursor.fetchall()
inner.commit()
inner.close()
for join in resultado:
    print(join)
"""
 

# LEFT JOIN

"""import mysql.connector
inner = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = inner.cursor()
SQL = "SELECT * from clientes LEFT JOIN productos p ON clientes.nombre = p.precio"
miCursor.execute(SQL)
resultado = miCursor.fetchall()
inner.commit()
inner.close()
for join in resultado:
    print(join)"""


# RIGHT JOIN
"""
import mysql.connector
inner = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)
miCursor = inner.cursor()
SQL = "SELECT * from clientes RIGHT JOIN productos p ON clientes.nombre = p.precio"
miCursor.execute(SQL)
resultado = miCursor.fetchall()
inner.commit()
inner.close()
for join in resultado:
    print(join)"""



#FULL OUTER 



# Conexión a MySQL
"""import mysql.connector
conexion = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    port = "3306",
    password = "",
    database = "techno"
)

miCursor = conexion.cursor()

instruccion ="""""""
SELECT c.id, c.nombre, c.apellido1, c.apellido2, c.ciudad, c.categoria,
       p.precio
FROM clientes AS c
LEFT JOIN productos AS p ON c.nombre = p.precio
UNION
SELECT c.id, c.nombre, c.apellido1, c.apellido2, c.ciudad, c.categoria,
       p.precio
FROM productos AS p
LEFT JOIN clientes AS c ON c.nombre = p.precio
"""

"""miCursor.execute(instruccion)
resultado = miCursor.fetchall()

for fila in resultado:
    print(fila)

conexion.close()"""
""