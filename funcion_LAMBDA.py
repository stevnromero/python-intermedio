
"""frase = lambda nombre: f"hola, {nombre} como estas?"
print(frase("Andrea")) 

frase = lambda nombre: print(f"hola, {nombre} como estas?")
frase("Andrea")"""


"""estudiantes = lambda nombres: f"los nombres del grupo colaborativo son: {nombres}"
print(estudiantes("johan"))
print(estudiantes("julián"))
print(estudiantes("marlon"))
print(estudiantes("pedro"))

"""

"""def myfucn(b):
    return lambda a: a - b
resta = myfucn(4)
print(resta(11))"""


"""def myPhrase(saludo):
    return lambda nombre: f"{saludo} {nombre}, how are you my best friend?"
nombre = myPhrase("hello")
print(nombre("Andrea"))


maximo = lambda a,b,c: f"El mayor numero está entre {a}, {b} y {c} es: {max(a,b,c)}"
print(maximo(15,4,9))
"""

"""def operaciones(num1, num2):
    return lambda num3: num1 * num2 / num3
opcion_1 = operaciones(12,4)
print(opcion_1(2))
"""


def raices(num1):
    import math 
    return lambda num2: f"la raiz cuaduada de 81 es: {math.sqrt(num2)} y la raiz cubica es: {math.cbrt(num1)}"

resultado = raices(8)
print(resultado(81))



