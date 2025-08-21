# crear la clase llamado celular()

"""class celular ():
    marca = input("ingresa el nombre de la marca:")
    precio =  int(input("ingresa el precio"))
    tienda = "WOM"
    Ciudad = "Bogotá D.C."

print(celular)
print(f"el precio del celular es: {celular.precio}")
print(type(celular))"""


# crear el objeto para imprimir la variable o atributos de un objeto.

"""p1 = celular()
print(p1.marca)"""


# usamos el metodo _init_()

"""class chaqueta:
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre
        self.precio = precio
        self.talla = talla
        self.color = color

p2 = chaqueta("chamarra", 50000.0, "S", "Negro")
print(f"{p2.nombre}, ${p2.precio}, {p2.talla}, {p2.color}. ")"""


# usamos otro metodo con y/o sin _str_()

"""print("con el metodo _str_()")
class chaqueta:
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre
        self.precio = precio
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"{self.nombre}, {self.precio}, {self.talla}, {self.color}"
    
p2 = chaqueta("chamarra", 50000.0, "S", "Negro")
print(p2)"""


#crear metodos dentro de los objetos

"""
class chaqueta:
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre
        self.precio = int(precio)
        self.talla = talla
        self.color = color

    def myfunc(self):
        print (f"la cuaqueta es la marca {self.nombre} y tiene un precio de {self.precio}")
        
p2 = chaqueta("chamarra", 50000, "S", "Negro")
p2.myfunc()
"""

# parametro propio

"""class girlfriend:
    def __init__(Mylove, nombre, edad, tiempo_relacion, color_favorito):
        Mylove.nombre = nombre
        Mylove.edad = edad
        Mylove.tiempo_relacion = tiempo_relacion
        Mylove.color_favorito = color_favorito

    def loves(best):
        print (f"{best.nombre} llevó conmigo {best.tiempo_relacion} de noviazgo")
        
p2 = girlfriend("Juanita", 26, "8 meses", "rosado")
p2.loves()

# modificar propiedades de objeto
p2.edad = 28
print(p2.edad)

del p2.edad
print(p2.edad)"""


#ejercicio de hoy

"""class Camiseta:
    def __init__(self, marca, precio, talla, color):
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color
        self.rebajada = True

    def aplicarDescuento(self, porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebajada = True

    def infoPorducto(self):
        info = f"Descripcion de la camiseta: Marca: {self.marca} precio: {self.precio} Talla: {self.talla} color: {self.color}"
        if self.rebajada:
            info += "ESTE PRODUCTO ESTA REBAJADO"
        return info
    


camiseta = Camiseta("Nike", 19.99, "S", "Lila")
camisetaAdidas = Camiseta("Adidas", 30, "M", "rojo")

print(camisetaAdidas.precio)
camisetaAdidas.aplicarDescuento(50)
print(camisetaAdidas.precio)


print(camiseta.infoPorducto())
print("##############")
print(camisetaAdidas.infoPorducto())"""


# POO HERENCIA

"""class persona:
    def __init__(self, nombre, apellido, edad, ID):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ID = ID
        
    def printname(self):
        print(self.nombre, self.apellido)


class student(persona):
    pass
        

p2 = student("Samuel", "Orozco", 24, "PSFOA1")
p2.printname()"""



"""
    def __str__(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} y su ID ES {self.ID}"""

"""
class persona:
    def __init__(self, nombre, apellido, edad, ID):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ID = ID
        
    def printname(self):
        print(self.nombre, self.apellido)
        
class student(persona):
      def __init__(self, nombre, apellido, edad, ID):
          persona.__init__(self,nombre,apellido,edad, ID)
      
    
curriculo = student("Samuel", "Orozco", 24, "PSFOA1")
curriculo.printname()


class student(persona):
    def __init__(self, nombre, apellido, edad, ID, facultad, materia, universidad):
        super().__init__(nombre, apellido, edad, ID)
        self.facultad = facultad
        self.materia = materia
        self.universidad = universidad

    def Estudio(self):
        return f"{self.nombre} estudia en la universidad {self.universidad} y sus materias son {self.materia}"
        

curriculo = student("Samuel", "Orozco", 24, "PSFOA1", "Ingeniería", ["Progamacion", "IOT", "Bases de datos"], "CUN")
print(curriculo.Estudio())
"""


"""
class persona:
    def __init__(self, nombre, apellido, edad, ID):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ID = ID
        
    def printname(self):
        print(self.nombre, self.apellido)
        

class student(persona):
    def __init__(self, nombre, apellido, edad, ID, facultad, materia, universidad):
        super().__init__(nombre, apellido, edad, ID)
        self.facultad = facultad
        self.materia = materia
        self.universidad = universidad

    def Estudio(self):
        return f"{self.nombre} estudia en la universidad {self.universidad} y sus materias son {self.materia}"
        

    def welcome(self):
        print(self.nombre, "bievenido a la univeridad", self.universidad  )

curriculo = student("Samuel", "Orozco", 24, "PSFOA1", "Ingeniería", ["Progamacion", "IOT", "Bases de datos"], "CUN")
curriculo.welcome()
print(curriculo.universidad)
curriculo.printname()



class chaqueta:
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre
        self.precio = precio
        self.talla = talla
        self.color = color

p2 = chaqueta("chamarra", 50000.0, "S", "Negro")
print(f"{p2.nombre}, ${p2.precio}, {p2.talla}, {p2.color}. ")
"""


# ENCAPSULAMIENTO



"""
class persona:
    def __init__(self, nombre, apellido, edad, ID):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__ID = ID
        
    def printname(self):
        return f"mi nombre es {self.__nombre} {self.__apellido} tengo {self.__edad} mi cedula es {self.__ID}"
        


x = persona("Samuel", "Orozco", 24, "PSFOA1")
print(x.printname())
print(f"su nombre es: {x._persona__apellido}")"""


"""class persona:
    def __init__(self, nombre, apellido, edad, ID):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__ID = ID
        
        
class student(persona):
    def __init__(self, nombre, apellido, edad, ID, facultad, materia, universidad):
        super().__init__(nombre, apellido, edad, ID)
        self._name = nombre
        self.__facultad = facultad
        self.__materia = materia
        self._universidad = universidad

    def smart(self):
        return f"{self._name} estudia en la universidad {self._universidad} y sus materias son {self.__materia}"
        

    def welcome(self):
        return f"{self._name}. bievenido a la univeridad {self._universidad} + en la facultad de {self.__facultad}"

curriculo = student("Samuel", "Orozco", 24, "PSFOA1", "Ingeniería", ["Progamacion", "IOT", "Bases de datos"], "CUN")
print(f"sus nombres del estudiante son: {curriculo._persona__nombre} {curriculo._persona__apellido}")
print(curriculo.smart())
print(curriculo.welcome())"""

""""
class persona:
    def __init__(self, nombre, apellido, edad, ID):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._ID = ID
        
    def printname(self):
        print(self._nombre, self._apellido, self._edad, self._ID)
        
class student(persona):
    def __init__(self, nombre, apellido, edad, ID, facultad, materia, universidad):
        super().__init__(nombre, apellido, edad, ID)
        self._facultad = facultad
        self._materia = materia
        self._universidad = universidad
        pass

    def smart(self):
        return f"{self._nombre} estudia en la universidad {self._universidad} y sus materias son {self._materia}"
        
    def welcome(self):
        return f"{self._nombre}. bievenido a la univeridad {self._universidad} + en la facultad de {self._facultad}" 

curriculo = student("Samuel", "Orozco", 24, "PSFOA1", "Ingeniería", ["Progamacion", "IOT", "Bases de datos"], "CUN")
print(f"sus nombres del estudiante son: {curriculo._nombre} {curriculo._apellido}")
print(curriculo.printname())
print(curriculo.smart())
print(curriculo.welcome())"""



# POLIMORFISMO
"""
class celular:
    def __init__(self, nombre, marca, precio):
        self.client = nombre
        self.marca = marca
        self.precio = precio


    
    def IVA (self):
        return f"el iva del precio del celular es de: ${int(self.precio) * iva/100}"
    


    def RETEFUENTE (self):
        return f"el retefuente del precio de celular es de: ${int(self.precio) * retefuente/100}"
    
    def TOTAL (self):
        return  f"el valor total del precio del celular es de: ${int(self.precio) * iva/100 - int(self.precio) 
        * retefuente/100 + int(self.precio)}"
    

x = celular("Pablo Medusa", "Samsung Galaxy", 950000)
iva = int(19)
retefuente = int(25)
print(x.IVA())
print(x.RETEFUENTE())
print(x.TOTAL())
"""


"""class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
"""

"""
class empleado:
    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual


    def SueldoNormal(self):
        print(f"el sueldo del empleado es {self.sueldoMensual}")

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual *(1+1/100)
        print(f"El sueldo anual de {self.nombre}, empleado formal, es de {sueldo}")




class contable(empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)


    def SueldoNormal(self):
        print(f"el sueldo del contador es {self.sueldoMensual}")

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual *(1+4/100)
        print(f"El sueldo anual de {self.nombre}, contable, es de {sueldo}")



class publicista(empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def SueldoNormal(self):
        print(f"el sueldo del publicista es {self.sueldoMensual}")
    
    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual *(1+4/100)
        print(f"El sueldo anual de {self.nombre}, publicista, es de {sueldo}")




empleados = [
    empleado("juan", 1300000),
    contable("edwin", 1240000),
    publicista("luna", 1300000)
]

print(len(empleados))   


for job in empleados:
    job.calcularSueldoAnual()


for empleado1 in (empleados):
    empleado1.SueldoNormal()
    continue"""




#PROGRAMACION ORIENTADA A OBJETOS ABSTRACCION

"""from abc import ABC, abstractmethod

class personaje(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100

    @abstractmethod
    def atacar (self, objetivo):
        pass

    @abstractmethod
    def getStatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")
    
    def subirNivel (self):
        self.nivel += 1

    def veterinario(self):
        print(f"Inventario de: {self.nombre}")
        for objeto in self.inventario:
            print(objeto)

    
class Mago(personaje):
    def __init__(self, nombre):
      super().__init__(nombre)
      self.vida = 120
      self.inteligencia = 95
      self.inventario = ["Porción de Mana", "Grimorio"]

    def getStatus(self):
        print(f"clase mago")
        super().getStatus()

      
    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia*0.6
        print(f"vida actual del objetivo es: {objetivo.vida}")





class Guerrero(personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Porción de vida", "Escudo", "Espada"]


    def getStatus(self):
        print(f"clase guerrero")
        super().getStatus()


    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.8
        print(f"el objetivo se ha quedado con {objetivo.vida} puntos de vida") 



guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")

guerrero.getStatus()
mago.getStatus()

mago.veterinario()
guerrero.veterinario()

mago.atacar(guerrero)
guerrero.atacar(mago)
"""

"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass

class Bird(Animal):
    @property
    def sound(self):
        return "Chirp"


class Dog(Animal):
    @property
    def sound(self):
        return "BULLDOG"
    
bird = Bird()
print(bird.sound)

dog = Dog()
print(dog.sound)"""

"""from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Uncommenting the following line will raise an error because we’re missing method implementations
# shape = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods #area, perimeter

circle = Circle(5)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")
"""


# EJERCICIO DE PRACTICA 


"""from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class Email(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando correo: {mensaje}")

class SMS(Notificacion):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

# Prueba
correo = Email()
mensaje_texto = SMS()
correo.enviar("Hola desde Python.")
mensaje_texto.enviar("Hola por SMS.")"""


"""from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau!")

class Gato(Animal):
    def sonido(self):
        print("Miau!")

# Prueba
animales = [Perro(), Gato()]
for animal in animales:
    animal.sonido()
"""

"""
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def frase(self, nombre, edad, altura):
        pass

    @abstractmethod
    def logros(self, nombre, premio):
        pass

class Luchador(Persona):
    def __init__(self):
        self.lista_luchadores = []

    def frase(self, nombre, edad, altura):
        print(f"{nombre} tiene {edad} de edad. Mide una altura de: {altura} cm")

    def logros(self, nombre, premio):
        self.lista_luchadores.append((nombre, premio))

    def mostrar_logros_ordenados(self):
        ordenados = sorted(self.lista_luchadores, key=lambda x: x[1])  # orden ascendente por premios
        for nombre, premio in ordenados:
            print(f"{nombre} ha conseguido un total de {premio} títulos mundiales de la WWE.")
            if premio >= 17:
                print(f"{nombre} es el máximo ganador")
            elif premio == 16:
                print(f"{nombre} es el segundo ganador")
            elif premio == 14:
                print(f"{nombre} es el tercer ganador")
            elif premio == 12:
                print(f"{nombre} es el cuarto ganador")
            else:
                print(f"{nombre} es el último ganador")

# Uso
cv = Luchador()
cv.frase("Triple H", 56, 1.93)
cv.logros("Triple H", 14)
cv.frase("John Cena", 47, 1.85)
cv.logros("John Cena", 17)
cv.frase("Hulk Hogan", 71, 2.01)
cv.logros("Hulk Hogan", 12)
cv.frase("Ric Flair", 76, 1.85)
cv.logros("Ric Flair", 16)
cv.frase("The Rock", 53, 1.93)
cv.logros("The Rock", 10)

cv.mostrar_logros_ordenados()
"""