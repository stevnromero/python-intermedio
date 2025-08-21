"""import pandas as pd
aprendices = {
    "nombres ": ["Andrea", "Marizta", "Pedro"],
    "edad " : [22, 25, 19],
    "carrera" : ["programacion", "diseño de moda", "mecatronica"]
}
df = pd.DataFrame(aprendices)
print(df)
print(pd.__version__)
"""

# METODO LISTAS DE LISTAS

"""import pandas as pd
columnas = ["nombre", "apellido", "estado civil", "profesion"]
columnas= [x.capitalize() for x in columnas]
valueA = ["laura", "bonilla", "casada", "constructora"]
valueA= [x.capitalize() for x in valueA]
valueB =  ["carlos", "arbealez", "divorciado", "cocinero"]
valueB= [x.capitalize() for x in valueB]
valueC =  ["david", "loaiza", "soltero", "ingeniero civil"]
valueC= [x.capitalize() for x in valueC]
df = pd.DataFrame([valueA,valueB,valueC], columns= columnas,)
print(df)
"""

# FUNCION ZIP()

"""nombres = ["Andrea", "Marizta", "Pedro"]
apellidos = ["Florez", "Arjona", "Gonzalez"]

for nombre, apellido in zip(nombres,apellidos):
    print(f"{nombre} {apellido}")"""


# ZIP() CON Dataframes Pandas:

"""import pandas as pd
columnas = ["deportista", "edad", "ocupacion"]
columnas = [x.capitalize() for x in columnas]
deportistas = ["Lionel Messi", "Nairo Quintana", "The Rock", "Michael Jordan"]
edad = [38, 35, 53, 62]
ocupacion = ["futbolista", "ciclista", "luchador", "basquetbolista"]
ocupacion = [x.capitalize() for x in ocupacion]

df = pd.DataFrame(list(zip(deportistas, edad, ocupacion)), columns= columnas)
print(df)
"""

# Iteramos las pandas con el diccionario

"""import pandas 
deportistas = ["Lionel Messi", "Nairo Quintana", "The Rock", "Michael Jordan"]
edad = [38, 35, 53, 62]
ocupacion = ["futbolista", "ciclista", "luchador", "basquetbolista"]
diccionario = {"Deportista": deportistas, "Edad" : edad, "Ocupacion" : ocupacion}
df = pandas.DataFrame(dict(diccionario))
print(df)"""


# SERIES DE PANDAS
# es una matriz unidimensional que contiene datos de cualquier tipo (columnas en una tabla)

"""import pandas as pd
edad = [38, 35, 53, 62]
x = pd.Series(edad)
y = pd.Series(edad, index=["a","b","c","d"])
print(x)
print(x[1])# etiquetar filas
print(y)
print(y["b"])

import pandas as pd
aprendices = {"nombre" : "johan", "apellido" : "romero", "edad" : 22}
x = pd.Series(aprendices)
print(x)
"""


# LEER ARCHIVOS CSV

"""import pandas as pd 
pd.options.display.max_rows = 5
df = pd.read_csv("C:/Users/ThinkPad/Documents/CURSO DE PYTHON COMPLETO/INTERMEDIO Y AVANZADO/Archivos CVS/clima.csv")
#print(df.to_string())
print(df)"""



# ejemplo
"""import pandas as pd

df = pd.read_csv("C:/Users/ThinkPad/Documents/CURSO DE PYTHON COMPLETO/INTERMEDIO Y AVANZADO/Archivos CVS/libros.csv")
print(df)
print(df["titulo"][1:])
print(df.sort_values(by= "titulo"))
print(df.set_index("isbn"))
print(df[df["autor"] == "Homero"])"""


# AÑADIR COLUMNAS EN LA TABLA

import pandas as pd

import pandas as pd
aprendices = {
    "nombres ": ["Andrea", "Marizta", "Pedro"],
    "edad " : [22, 25, 19],
    "carrera" : ["programacion", "diseño de moda", "mecatronica"]
}
df = pd.DataFrame(aprendices)
df["estado civil"] = ["soltera", "casada", "viudo"] # sintaxis basica
df = df.assign(altura = [1.60, 1.50, 1.48]) # asignar valores en una columna nueva
df.insert(3, "fecha de nacimiento", ["12-12-1999", "15-04-1978", "27-08-1990"])
print(df)