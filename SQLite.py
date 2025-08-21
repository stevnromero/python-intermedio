
# creamos una conexion de BD con SQLITE

"""import sqlite3

#establecer conexion
conn = sqlite3.connect("new database.db")

#crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# cerrar la conexion (opcional= al finalizar)
conn.close()
"""


# CREAR BASE DE BATOS SQLITE
"""
import sqlite3 

conn = sqlite3.connect("technology.db")
conn.commit()
conn.close()

def CreateDB():
    conn = sqlite3.connect("technology.db")
    conn.commit()
    conn.close()
CreateDB()"""

# COMPROBAR SI EXISTEN LA BASE DE DATOS SQLITE
"""
import sqlite3
import os

My_database = "technology.db"

if os.path.exists(My_database):
    print(f"la base de datos {My_database} si existe")
    conn = sqlite3.connect(My_database)
else:
    print(f"la base de datos {My_database} no existe")
    conn = sqlite3.connect(My_database)
    conn.close()
    """

# CREAR TABLAS CON SQLITE
"""
import sqlite3

def CreateTable():
    conn = sqlite3.connect("technology.db")
    cursor = conn.cursor()
    cursor.execute("""
""" CREATE TABLE clientes(
        id int auto_increment primary key, # le asignamos las claves primarias para valores unicos de cada registro
        nombre varchar(100),
        apellido1 varchar(100),
        apellido2 varchar(100),
        ciudad varchar(100),
        categoria int
)
   )
    conn.commit()
    conn.close()
CreateTable()"""


""""conn = sqlite3.connect("technology.db")
cursor = conn.cursor()
cursor.execute("""""""
               CREATE TABLE productos(
               id int auto_increment primary key, 
               nombre varchar (100), 
               precio decimal (10,2), 
               id_client int, 
               foreign key(id_client) references clientes(id)
               )"""
""")
conn.commit()
conn.close()"""


# CAMBIAR EL NOMBRE DE LA TABLA
"""
import sqlite3

conn = sqlite3.connect("technology.db")
cursor = conn.cursor()
cursor.execute("ALTER TABLE producto RENAME TO productos")
conn.commit()
conn.close()
"""


# INSERTAR VALORES EN LAS TABLAS
# opcion 1: insertar cada una de las filas
"""
import sqlite3

def Insert(id, nombre, apellido1, apellido2, ciudad, categoria):
    conn =sqlite3.connect("technology.db")
    miCursor = conn.cursor()
    instruccion = f"INSERT INTO clientes VALUES ({id}, '{nombre}', '{apellido1}', '{apellido2}', '{ciudad}', {categoria})"
    miCursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #Insert(1,"Adolfo","Rubio","Flores","Sevilla",300)
    #Insert(5,"Pepe", "Ruiz", "Santana", "Huelva", 200)
    """

"""import sqlite3
def Insert2(id, nombre, precio, id_client):
    conn = sqlite3.connect("technology.db")
    miCursor = conn.cursor()
    instruccion = f"INSERT INTO productos VALUES ({id}, '{nombre}', {precio}, {id_client})"
    miCursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #Insert2(1,"Disco duro SATA3 1TB", 86.99, 1)
    #Insert2(5,'GeForce GTX 1080 Xtreme', 755, 5)
"""

# opcion 2 : insertar varias filas otra opcion de añadir elementos de una tabla

"""import sqlite3
conn =sqlite3.connect("technology.db")
miCursor = conn.cursor()

lista = [
    ("2","Marcos","Loyota","Mendez","Almeria",250),
    ("3","Maria","Del Valle","Arjona","Barcelona",450),
    ("4","Daniel","Salamanca","Paez","Madrid",320)
]
instruccion2 = "INSERT INTO clientes (id, nombre, apellido1, apellido2, ciudad, categoria) VALUES (?,?,?,?,?,?)"
miCursor.executemany(instruccion2,lista)
conn.commit()
conn.close()
print(f"record insert, ID: {miCursor.lastrowid}")


import sqlite3
conn =sqlite3.connect("technology.db")
miCursor = conn.cursor()

lista =[
    (2,"Portatil Yoga 520", 59.34, 2),
    (3,"Portatil Ideapd 320", 44.19, 3),
    (4,"Impresora HP Deskjet 3720", 61.09, 4)
]

instruccion2 = "INSERT INTO productos (id, nombre, precio, id_client) VALUES (?,?,?,?)"
miCursor.executemany(instruccion2, lista)
conn.commit()
conn.close()
"""


# SELECCION SQLITE
"""
import sqlite3

def select():
    conn = sqlite3.connect("technology.db")
    miCursor = conn.cursor()
    instruccion = f"SELECT nombre, apellido1 FROM clientes"
    miCursor.execute(instruccion)
    datos =miCursor.fetchall()
    for select in datos:
        print(f"los datos de esta tabla son: {select}")
    conn.commit()
    conn.close()

if __name__ in "__main__":
    select()

import sqlite3


conn = sqlite3.connect("technology.db")
miCursor = conn.cursor()
instruccion = f"SELECT * FROM productos"
miCursor.execute(instruccion)
datos =miCursor.fetchall()
for select in datos:
    print(f"los datos de esta tabla son: {select}")
conn.commit()
conn.close()"""

# SQLITE WHERE
"""
import sqlite3
conn = sqlite3.connect("technology.db")
miCursor = conn.cursor()
instruccion = f"SELECT * FROM clientes WHERE id = 1 or categoria = 250"
miCursor.execute(instruccion)
datos = miCursor.fetchall()
for filter in datos:
    print(f"los datos son: {filter}")
conn.commit()
conn.close()
"""
"""
import sqlite3
def where(instruccion):
    conn = sqlite3.connect("technology.db")
    miCursor = conn.cursor()
    miCursor.execute(instruccion)
    datos = miCursor.fetchall()
    for filter in datos:
        print(f"los datos son: {filter}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    where(f"SELECT * FROM productos WHERE id= 2 or id_client = 4")    
"""

# ORDENAR ASC Y DESC EN SQLITE

"""import sqlite3
order = sqlite3.connect("technology.db")
miCursor = order.cursor()
instruccion = f"SELECT nombre, ciudad FROM clientes ORDER BY ciudad ASC"
miCursor.execute(instruccion)
datos = miCursor.fetchmany(3)
for ordering in datos:
    print(f"las tuplas de esta tabla en ASC son: {ordering}")
    continue"""
    
"""import sqlite3
def OrderDesc(instruccion):
    order = sqlite3.connect("technology.db")
    miCursor = order.cursor()
    miCursor.execute(instruccion)
    datos = miCursor.fetchall()
    for ordering in datos:
        print (f"las tuplas de esta tabla en DESC son: {ordering}")  
if __name__ == "__main__":
    OrderDesc(f"SELECT nombre, id_client FROM productos ORDER BY nombre DESC")
"""

# eliminar datos existentes en SQLITE3

"""import sqlite3

def deleteRegister(instruccion):
    order = sqlite3.connect("technology.db")
    miCursor = order.cursor()
    miCursor.execute(instruccion)
    order.commit()
    order.close()
    print(miCursor.rowcount, "eliminacion exitosa")

if __name__ == "__main__":
    deleteRegister("DELETE FROM productos WHERE id = 5")"""


# ELIMINAR UNA TABLA EXISTENTE CON SQLITE

"""import sqlite3
def DropTable(instruccion):
    drop = sqlite3.connect("technology.db")
    miCursor = drop.cursor()
    miCursor.execute(instruccion)
    drop.commit()
    drop.close()
    print(miCursor.rowcount, "tabla eliminada!")
if __name__ == "__main__":
    DropTable("DROP TABLE IF EXISTS commercial")
"""

# ACTUALIZAR REGISTRO DE LA TABLA CON SQLITE

"""import sqlite3
updating = sqlite3.connect("technology.db")
miCursor = updating.cursor()
instruccion = "UPDATE clientes SET apellido1 = ?  WHERE id = ?"
nuevo = ("Arbeloa", 3)
miCursor.execute(instruccion,nuevo)
updating.commit()
updating.close()
print(miCursor.rowcount, "se cambiaron dos valores!")"""


# LIMITAR DATOS SQLITE 

"""import sqlite3
def limit(instruccion):
    limitar = sqlite3.connect("technology.db")
    miCursor = limitar.cursor()
    miCursor.execute(instruccion)
    resultado = miCursor.fetchall()
    for x in resultado:
        print(x)
if __name__ == "__main__":
    limit("SELECT * FROM productos LIMIT 2")"""


# EMPEZANDO DESDE OTRA POSICION UTILIZANDO OFFSET SQLITE

"""import sqlite3
def limit(instruccion):
    limitar = sqlite3.connect("technology.db")
    miCursor = limitar.cursor()
    miCursor.execute(instruccion)
    resultado = miCursor.fetchall()
    for x in resultado:
        print(x)
if __name__ == "__main__":
    limit("SELECT * FROM clientes LIMIT 5 OFFSET 2")"""


# UNION DE LOS JOINS EN SQLITE



"""# INNER JOIN
import sqlite3
inner = sqlite3.connect("technology.db")
miCursor = inner.cursor()
instruccion = "SELECT * from clientes INNER JOIN productos p ON clientes.categoria = p.id_client"
miCursor.execute(instruccion)
resutado = miCursor.fetchall()
for join in resutado:
    print(join)
"""

# LEFT JOIN

"""import sqlite3
inner = sqlite3.connect("technology.db")
miCursor = inner.cursor()
instruccion = "SELECT * from clientes LEFT JOIN productos p ON clientes.categoria = p.precio"
miCursor.execute(instruccion)
resutado = miCursor.fetchall()
for join in resutado:
    print(join)

"""
# RIGHT JOIN

"""import sqlite3
inner = sqlite3.connect("technology.db")
miCursor = inner.cursor()
instruccion = "SELECT * from clientes RIGHT JOIN productos p ON clientes.categoria = p.precio"
miCursor.execute(instruccion)
resutado = miCursor.fetchall()
for join in resutado:
    print(join)
"""

# FULL OUTER JOIN

"""import sqlite3

inner = sqlite3.connect("technology.db")
miCursor = inner.cursor()

instruccion = """"""
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

for join in resultado:
    print(join)
"""

