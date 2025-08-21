"""import sqlite3

def createDB():
    database = sqlite3.connect("libreria.db")
    database.commit()
    database.close()
if __name__ == "__main__":
    createDB()
               """

"""import sqlite3
def CreateTable1():
    table1 = sqlite3.connect("libreria.db")
    miCursor = table1.cursor()
    miCursor.execute(""""""
        CREATE TABLE clientes(
            id int auto_increment primary key,
            nombre varchar(100),
            email varchar(100),
            telefono varchar(15)
        )"""
"""    )
    table1.commit()
    table1.close()"""

"""if __name__ == "__main__":
    CreateTable1()
"""

"""import sqlite3
def CreateTable2():
    table2 = sqlite3.connect("libreria.db")
    miCursor = table2.cursor()
    miCursor.execute("""
"""CREATE TABLE libros(
            titulo varchar(100),
            actor varchar(100),
            precio decimal(6,2)"""
""")""""""
    )
    table2.commit()
    table2.close()

if __name__ == "__main__":
    CreateTable2() """


"""import sqlite3
def CreateTable3():
    table3 = sqlite3.connect("libreria.db")
    miCursor = table3.cursor()
    miCursor.execute(""""""
        CREATE TABLE ventas(
            id int UNSIGNED,
            fecha date NOT NULL,
            cantidad INT NOT NULL,
            id_client INT,
            id_read INT,
            FOREIGN KEY (id_client) REFERENCES clientes (id),
            FOREIGN KEY (id_read) REFERENCES libros (id)
        )"""
""" )
    table3.commit()
    table3.close()

if __name__ == "__main__":
    CreateTable3()"""
        

# ASIGNAR VALORES  

"""import sqlite3
asignar_tabla1 = sqlite3.connect("libreria.db")
miCursor = asignar_tabla1.cursor()
lista= [
    (1,'Ana Pérez', 'ana@example.com', '555-1234'),
    (2,'Luis Gómez', 'luis@example.com', '555-5678')
]
sql = "INSERT INTO clientes (id, nombre, email, telefono) VALUES (?, ?, ?, ?)"
miCursor.executemany(sql,lista)
asignar_tabla1.commit()
asignar_tabla1.close()
print(miCursor.rowcount, "valores insertado!")"""

"""import sqlite3
def Asignar_tabla2(lista):
    tabla2 = sqlite3.connect("libreria.db")
    miCursor = tabla2.cursor()
    sql = "INSERT INTO libros (titulo, actor, precio) VALUES (?, ?, ?)"
    miCursor.executemany(sql,lista)
    tabla2.commit()
    tabla2.close()
    print(miCursor.rowcount, "valores insertado!")

if __name__ == "__main__":
    Asignar_tabla2([('Cien Años de Soledad', 'Gabriel García Márquez', 15.50),
                    ('El Principito', 'Antoine de Saint-Exupéry', 9.99),
                    ('1984', 'George Orwell', 12.80)])"""


""

"""import sqlite3
def Asignar_tabla3(lista):
    tabla3 = sqlite3.connect("libreria.db")
    miCursor = tabla3.cursor()
    sql = "INSERT INTO ventas (id, fecha, cantidad, id_client, id_read) VALUES (?, ?, ?, ?, ?)"
    miCursor.executemany(sql,lista)
    tabla3.commit()
    tabla3.close()
    print(miCursor.rowcount, "valores insertado!")

if __name__ == "__main__":
    Asignar_tabla3([(1, '2025-08-15', 2, 1, 1),
                   (2, '2025-08-15', 3, 2, 2)])
"""



# ACTUALIZAR VALORES EN CASA TABLA

"""import sqlite3
updating = sqlite3.connect("C:/Users/ThinkPad/Documents/CURSO DE PYTHON COMPLETO/Python con MYSQL y SQLITE/FLASK/database/libreria.db")
miCursor = updating.cursor()
instruccion = "UPDATE libros SET titulo = ? WHERE ROWID= ?"
SQL = ("Cien Anos de Soledad", 1)
miCursor.execute(instruccion, SQL)
updating.commit()
updating.close()
print(miCursor.rowcount, "se cambio el dato")"""
