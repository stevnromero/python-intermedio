# EXCEPCIONES
# BLOQUE: TRY, EXCEPT AND FINALLY

"""try:
    b = "barbie" + 23 + "vil"
    print(b)
    
except:
    TypeError
    print(TypeError("la sintaxis es incorrecta"))

finally:
    print("sigamos codeando")


try:
    def niño(x):
        return f"el niño esta {x}"
    print(niño())

except:
    TypeError
    print("falta un argumento")

finally:
    print(niño("enfermo"))

        """



"""lista_tech = ["celular", "laptop", "vrt camara", "impresora"]

try:
    print(lista_tech)
    index= int(input("selecciona un dispositivo (ponle el numero:)"))
    print(f"estas usando este/a: {lista_tech[index]}")

except IndexError:
    print(f"indice incorrecto, la posicion debe estar entre 0 y {len(lista_tech)-1}")

except:
    ValueError
    print("debes colocar un numero entero")"""



# EXCEPCIONES DEFINIDAS POR EL USUARIO

"""try:
    b = "barbie" + 23 + "vil"
    print(b)
    
except Exception as suckit:
    print(suckit)"""


# ELSE, FINALLY, RAISE

"""while True:
    try:
        total = 0
        sumando = input("ponme numeros separados por espacios: ")
        sumando = sumando.split()
        for num in sumando:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError("el valor no es un numero")
            
    except ValueError:
        print("los datos son incorrectos")
        print("vuelva a introducir el numero")

    else:
        print(f"el valor de la suma es {total}")
        break

    finally:
        print("ha terminado la iteración")"""


"""x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")



if 5 /0:
   raise TypeError ("la sintaxis es incorrecta")
"""


"""try:
    def suma_multiplicacion(num):
        return 5 + 5 * num
    print(suma_multiplicacion("dsa"))

except TypeError:
    print("debes colocar un numero para completar la operacion")

raise TypeError("debemos salir de ese error")"""



try:
    b = "barbie" + 23 + "vil"
    print(b)
    
except:
    TypeError
    print(TypeError("la sintaxis es incorrecta"))

finally:
    print("sigamos codeando")


try: 
    nuevo = open("practica.txt", "x", encoding = "utf-8")
    nuevo.write("soy nuevo")
    print(nuevo.readable())
    print(nuevo.writable())
    nuevo.close()

except:
    FileExistsError
    print("no se puede crear el fichero porque ya existe")