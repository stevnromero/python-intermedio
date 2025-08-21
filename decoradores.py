"""
def triplicate(num):
    return num * 3

def myfucntion(func):
    num_3 = 14
    return func(num_3)

print(myfucntion(triplicate))
"""

"""def funcion(asunto):

    def investigacion():
        print("se necesita una introduccion del texto!")
        print(asunto)
    return investigacion()

funcion("el medio ambiente")


def funcion_2(sustantivo):

    def userHistory(verbo):
        print("esta es la estructura de las historias de usuario!")
        return lambda usuarios: f"{verbo} + {sustantivo} + {usuarios}"
    verbo = userHistory("vender")
    print(verbo("clientes"))

funcion_2("productos")


def amiga(nombre , apellido):

    def frase():
        x = f"{nombre} {apellido}, muy buenos dias mi cielo"
        print(x)
    return frase
    

oración = amiga("andrea", "roncancio")
oración()"""


#########################################################################
"""from datetime import datetime

def fecha():
    print(datetime.today().strftime("%D-%M-%Y"))

def hora():
    print(datetime.now().strftime("%H:%M:%S"))

def funcionExterna(funcionInterna):
    def funcionEnvoltorio():
        print("\nempieza la funcion.\n")
        funcionInterna()
        print("\nfin de la funcion.\n")
    return funcionEnvoltorio

mostrar_hora = funcionExterna(hora)
mostrar_hora()
mostrar_fecha = funcionExterna(fecha)
mostrar_fecha()"""

# sintaxis de los decoradores



"""def nombre(asunto):

    def investigacion():
        print("\n########################################################################################")
        print("comienza la investigacion")
        asunto()
        print("finaliza la investigacion")
        print("########################################################################################\n\n\n")
        
    return investigacion


lista_investigacion = ["pandemia", "medio ambiente","colegios", "alcoholismo"]
lista_investigacion_2 = ["enfermedades mentales", "emprendimiento", "reforma laboral"]

@nombre
def primero():
    print("Primer semestre de comunicacion social!")
    for numero in lista_investigacion:
        print(f"nombre de la investigacion: {numero}. Investigacion n/{lista_investigacion.index(numero)+1}")
        continue
primero()

@nombre
def segundo():
    print("Segundo semestre de comunicacion social!")
    for numero in lista_investigacion_2:
        print(f"Nombre de la investigacion: {numero}. Investigacion n/{lista_investigacion_2.index(numero)+1}")
        continue
segundo()
""""""

def sumarNumeros(*args, **kwargs):
    acc = 0
    for num in args:
        acc += num
    return acc


def operarConPares(operacion):
    def wrapper(*args, **kwargs):
        soloPares= list(filter(lambda num: num%2 == 0, args))
        resultado = operacion(*soloPares, **kwargs)
        print(f"el resultado de la operacion es: {resultado}")
        return resultado
    return wrapper

sumarPares= operarConPares(sumarNumeros)
sumarPares(1,2,4,6,8)

@operarConPares

def multiplicar(*args, **kwargs):
    acc = 1
    for num in args:
        acc *= num
    if "max" in kwargs.keys():
        return min(kwargs["max"],acc)
    return acc
multiplicar(1,2,3,4)

"""
    












    
        
    
    

    
