# ABRIR ARCHIVO
"""
fichero = open("practica.txt")
primera_linea = fichero.readline()
print(primera_linea)
print(fichero.readline())

todaslasLienas = fichero.readlines()
print(todaslasLienas)

with open("practica.txt", "rt") as new:
    print(new.readline())
    print(new.readline())
    print(new.readline())



fichero_lista = open("practica.txt", "rt")
primera_linea = fichero_lista.readline()
print(primera_linea)
lista = fichero_lista.readlines()
print(lista)
    
with open("practica.txt", "rt") as new:
    print(new.readline())
    print(new.readline())
    new.close()
   


# CERRAR ARCHIVO
fichero_lista = open("practica.txt", "rt", encoding = "utf-8")
primera_linea = fichero_lista.readlines()
print(primera_linea)
fichero_lista.close()
"""

# ESCRIBIR UN ARCHIVO EXISTENTE

# SOBRESCRIBIR "W"
"""fichero = open("./practica.txt", "w", encoding = "utf-8") 
fichero.write("hola andrea. Como estas amix? \n")
fichero.write("quiero compartir un largo tiempo de amistad.\n\n")
lista_frases = [
    "eres bella.\n",
    "tu eres el amor",
    " de mi vida.\n",
    "eres mi prioridad.\n"
]

fichero.writelines(lista_frases)
fichero.close()"""


# AGREGAR "a"

"""with open("practica.txt", "a", encoding = "utf-8") as newest:
    newest.write("te doy un osito de peluche.\n")
    newest.write("comprame una tortilla.\n")
    newest.write("quieres ser mi mejor amiga?.\n\n")
    lista_frases2 = [
        "te doy un abrazo.",
        "jamas te perderé.",
        "eres mi prioridad."]
    lista_frases2 = map(lambda linea: linea + "\n", lista_frases2)
    print(lista_frases2)
    newest.writelines(lista_frases2)
    newest.close()
"""
# CREAR FICHERO



"""nuevo = open("practice2.txt", "w", encoding = "utf-8")
nuevo.write("soy nuevo.\n")
nuevo.write("que tal viejo?.\n")
print(nuevo.readable())
print(nuevo.writable())
nuevo.close()
"""

# AÑADIR UNA LINEA DE TEXTO AL FINAL DEL FICHERO

"""nuevo = open("practice2.txt", "a", encoding = "utf-8")
nuevo.write("que hay de nuevo, SCOOBY DOO.\n")
nuevo.close()

with open("practice2.txt", "a", encoding = "utf-8") as nuevo:
    nuevo.write("mis pasatiempos son: el futbol, la programación y las novelas .")
    nuevo.readable()
    nuevo.writable()

nuevo.close()
"""


# metodo seek()
"""
fichero = open("practica.txt")
print("leeme desde el principio de la letra: ")
fichero.seek(5)
print(fichero.readline())
print(fichero.read(33))
fichero.close()"""

# ELIMINAR UN ARCHIVO


#creamos el archivo
"""fichero = open("hello.txt", "w", encoding = "utf-8")
fichero.write("hoy es jueves festivo: dia de las cometas")"""


#luego, lo eliminamos 

"""import os 
os.remove("today.txt")"""

"""import os
if os.path.exists("today.txt"):
    os.remove("today.txt")
else:
    print("no existe el archivo")"""


# eliminar carpeta

"""import os
os.rmdir("eliminate")"""

import os
os.remove("C:/Users/ThinkPad/Pictures/Screenshots/ERROR DEL SEGUNDO FORMULARIO.png")