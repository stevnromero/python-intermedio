
# FUNCIONES MAP() Y FILTER ()

"""frase = [1, 3, 6, 10]
numeros_enteros = []
for numero in frase:
    
    if numero in (2,4,6,8,10,12,14,16,18,20):
        print(f"{numero} es par")
        numeros_enteros.append(numero)

    else:
        print(f"{numero} es impar")    

print(numeros_enteros)
"""


#FUNCION FILTER()

"""ropa = ["zapatos", "jeans", "zapatillas", "chaquetas"]

def operators(clothes):
    return "z" in clothes

num = list(filter(lambda x: "z" in  x, ropa))
print(num)


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)"""

"""
juegos = ["mario", "zelda", "FC25", "call of duty"]
juegos.sort()
juegos_2 = ["metroid", "donkey kong", "mortal kombat", "super smash"]
juegos_2.sort()
juegos.extend(juegos_2)
juegos.sort()
print(juegos)

def games(game):
    return game in juegos

over = filter(games, juegos)

for x in over:
    print(f"los juegos de nintendo por orden ASC son: {x}")


disponible = input("selecciona un juego: ")
if disponible in juegos:
    print("si esta disponible")
else:
    print("no esta disponible en catalogo")


cantidad = input("que juegos originales quieres llevar? :" ) 

if cantidad in juegos[0:] or juegos[:5]:
    print("llevatelos")
else:
    print("En otra ocasion, lo compraré")
"""


"""prendas_cuero = ["chaquetas", "gorras", "correas", "bolsos", "billeteras", "guantes"]
capitalise = [x.capitalize() for x in prendas_cuero]
capitalise.sort()
print(capitalise)

longitudes = tuple(map(lambda ropa: len(ropa),prendas_cuero))
print(longitudes)

import math
ejex = [1,2,4,6,7,9,12]
ejexx = [2,6,8,10,13,15]
ejey = tuple (map(lambda x, y: round(math.cos(x) + math.exp(y), 2), ejex,ejexx))
print(ejey)
"""

"""
nombre = ["andrea"]
apellido = ["roncancio"]"""


"""digitos = list(map(lambda amix : len(amix), nombre + apellido))
print(digitos)


def myfucn(nombre, apeliido):
    return nombre + " " + apeliido

x = list(map(myfucn,(nombre),(apellido)))
print(x)"""


"""def name(nombre):
    return "andrea" in nombre

amix = filter(name,nombre)

for x in amix:
    print(f"di el nombre tres veces: {x}")


nombre = ["andrea"]
apellido = ["roncancio"]"""


"""digitos = list(map(lambda amix : len(amix), nombre + apellido))
print(digitos)


def myfucn(nombre, apeliido):
    return nombre + " " + apeliido

x = list(map(myfucn,(nombre),(apellido)))
print(x)"""



"""nombre = ["andrea"]
apellido = ["roncancio"]
def name(nombre):
    return "andrea" in nombre

amix = filter(name,nombre)

for x in amix:
    pass

contador = 0
while contador < 6:
    contador +=1 
    print(f"di el nombre tres veces: {x}")
    if contador == 3:
        break
    """

"""prendas_cuero = ["chaquetas", "gorras", "correas", "bolsos", "billeteras", "guantes"]
capitalise = [x.capitalize() for x in prendas_cuero]
capitalise.sort()
print(capitalise)

longitudes = tuple(map(lambda ropa: len(ropa),prendas_cuero))
print(longitudes)



diccionario = dict(
    nombre = "johan",
    apellido = "romero",
    edad = 22,
    equipo = "Fc Barcelona",
    comida = "Pizza"

)

def filtro(item):
    clave, Valor = item
    return clave == "nombre" or Valor == "johan"

diccionario_filtrado = dict(filter(filtro, diccionario.items()))
print(diccionario_filtrado)

for clave, valor in diccionario_filtrado.items():
    pass

contador = 0
while contador < 5:
    contador +=2
    print(f"di el {clave} tres veces: {valor}")
    continue
"""


"""nombre = ["andrea", "pedro"]
apellido = ["roncancio", "jaramillo"]

def myfucn(nombre, apeliido):
    return nombre + " " + apeliido

x = list(map(myfucn,(nombre),(apellido)))
print(x)


nombres = ["Andrea", "Marizta", "Pedro"]
apellidos = ["Florez", "Arjona", "Gonzalez"]

def fusion(nombres, apellidos):
    return f"{nombres} {apellidos}"

x = tuple(map(fusion, (nombres), (apellidos)))
print(x)"""