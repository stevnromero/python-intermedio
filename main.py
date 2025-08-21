"""
def suma(num):
    return num * 2


if __name__ == "__main__":
    print(suma(2))


def amiga (nombre,apellido):
    def fraseBonita():
        greet = f"{nombre} {apellido}"
        print(greet)
    return fraseBonita()
           

if __name__ == "__main__":
    amiga("andrea","roncancio")
    """
"""import os

def EliminarArchivo():
    return f"eliminame este archivo: {os.remove("liloStick.db")}"

if __name__ == "__main__":
    print(EliminarArchivo())"""


"""def agrad(name):
    return f"Thank you. {name.capitalize()}"
if __name__ == "__main__":
    print(agrad("superstar"))"""

"""import sqlite3

def deleteRegister(instruccion):
    order = sqlite3.connect("technology.db")
    miCursor = order.cursor()
    eliminar = (1,)
    miCursor.execute(instruccion,eliminar)
    order.commit()
    order.close()
    print(miCursor.rowcount, "eliminacion exitosa")

if __name__ == "__main__":
    deleteRegister("DELETE FROM productos WHERE id = ?")"""