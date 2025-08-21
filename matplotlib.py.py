"""from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
pd.options.display.max_rows = 5
df = pd.read_csv("C:/Users/ThinkPad/Documents/CURSO DE PYTHON COMPLETO/INTERMEDIO Y AVANZADO/Archivos CVS/clima.csv")
#print(df.to_string())

# GRAFICO

max_simples= 50
humedad = df["humedad"][: max_simples]
plt.plot(humedad, "o", label= " grado temperatura", )
plt.title("el clima de este mes")
plt.xlabel("precipitacion")
plt.ylabel("humedad")
plt.xticks(rotation = 0)
plt.legend()
plt.show()"""



# trazar sin linea
"""import matplotlib.pyplot as plt
import numpy as np 
xpoints = np.array([2, 4])
ypoints = np.array([1, 5])
plt.plot(xpoints,ypoints,"o")
plt.title("PLAN CARTESIANO")
plt.show()"""

# PUNTOS MULTIPLES

# MARCADORES
"""import matplotlib.pyplot as plt 
import numpy as np 
Xpoints = np.array([1,1,2,3,4,5,5,3,1])
Ypoints = np.array([3,5,6,5,6,5,3,1,3])
#Ypoints = np.array([3,5,6,5,1]) 
plt.plot(Xpoints, Ypoints, "*-k", ms = 20 ) #= cadena de formato FMT
plt.fill(Xpoints,Ypoints, color = "red")
#plt.plot(Xpoints, Ypoints, "o-.g", markersize = 20) = Tamaño del marcador
#plt.plot(Xpoints, Ypoints, "o-.g", markersize = 20, mec = "k") = cambiar el borde del marcador
#plt.plot(Xpoints, Ypoints, "o-.r", mfc = "k", markersize= 20) = cambiar el color del marcador
plt.show()"""


# LINEAS

"""import matplotlib.pyplot as plt 
import numpy as np 
Xpoints = np.array([1,5,1,1])
Ypoints = np.array([5,1,1,5])
Xpoints2 = np.array([])
ypoints2= np.array([])
#plt.plot(Xpoints, ls = "-.", marker = "o", markersize = 20, mec = "black", lw = 10)
#plt.plot(Ypoints, ls = "-.", marker = "o", markersize = 20, mec = "black", lw =10) = cambiar el ancho de la linea
plt.plot(Xpoints,Ypoints, marker = "o", markersize = 20, mfc = "red" )
plt.fill(Xpoints, Ypoints, color='yellow', alpha=1)
plt.show()
"""

# ETIQUETAS Y TITULOS

"""import matplotlib.pyplot as plt 
import numpy as np 

Xpoints = np.array([1,5,1,1])
Ypoints = np.array([5,1,1,5])
Xpoints2 = np.array([5,1,5,5])
ypoints2= np.array([5,5,1,5])

#plt.plot(Xpoints,Ypoints, marker = "*", markersize = 20, mfc = "red", color = "black" )
plt.plot(Xpoints, Ypoints, Xpoints2, ypoints2, color = "k", marker = "o", ms = 20, mfc = "r", lw = 5, mec ="r")
plt.fill(Xpoints2,ypoints2, color = "blue")
plt.fill(Xpoints, Ypoints, color='yellow', alpha=1) # rellenar la figura
#plt.title("triangulo recto".upper(), fontdict= {"color" : "red", "size" : 10, "family" : "Times new roman"}) #establecer un titulo de la figura y cambiar las propiedades de fuente
#plt.xlabel("lado 1".upper(), fontdict= {"color" : "red", "size" : 10, "family" : "Times new roman"}) # etiquetar los ejes
#plt.ylabel("lado 2".upper(), fontdict= {"color" : "red", "size" : 10, "family" : "Times new roman"}) # etiquetar los ejes
plt.title("triangulo recto".upper(), loc= "left") # posicionar el titulo"""



# LINEAS DE CUADRICULA

"""
import matplotlib.pyplot as plt 
import numpy as np 

Xpoints = np.array([1,5,1,1])
Ypoints = np.array([5,1,1,5])
Xpoints2 = np.array([5,1,5,5])
ypoints2= np.array([5,5,1,5])

plt.plot(Xpoints, Ypoints, Xpoints2, ypoints2, color = "k", marker = "o", ms = 20, mfc = "r", lw = 5, mec ="r")
plt.fill(Xpoints2,ypoints2, color = "blue")
plt.fill(Xpoints, Ypoints, color='yellow', alpha=1)

#plt.grid() # agregar lineas de cuadricula
#plt.grid(axis= "y") # especificar la linea
plt.grid(color = "magenta", lw = 2, linestyle = "-") # establecer lineas de cuadricula
plt.show()"""


# MOSTRAR MULTIPLES GRAFICAS

"""import matplotlib.pyplot as plt 
import numpy as np

Xpoints = np.array([1,3,1,1])
Ypoints = np.array([3,1,1,3])
plt.subplot(1,2,1)
plt.plot(Xpoints, Ypoints)


Xpoints2 = np.array([1,1,2,3,4,5,5,3,1])
Ypoints2 = np.array([3,5,6,5,6,5,3,1,3])

plt.subplot(1,2,2)
plt.plot(Xpoints2, Ypoints2)"""

# EJERCICIO 2

"""import matplotlib.pyplot as plt 
import numpy as np

Xpoints = np.array([2,6,10,8,11,7,6,5,1,4,2,6])
Ypoints = np.array([1,3,1,5,7,7,11,7,7,5,1,3])
plt.subplot(2,2,1)
plt.plot(Xpoints, Ypoints, c = "k")
plt.fill(Xpoints,Ypoints, color = "yellow")
plt.title("estrella".upper())
plt.grid()

Xpoints2 = np.array([1,2,3,2,1])
Ypoints2 = np.array([3,1,3,5,3])
plt.subplot(2,2,2)
plt.plot(Xpoints2, Ypoints2, c = "k")
plt.fill(Xpoints2,Ypoints2, color = "red")
plt.title("rombo".upper())
plt.grid()


Xpoints3 = np.array([1,3,6,4,6,3,1])
Ypoints3 = np.array([3,5,5,3,1,1,3])
plt.subplot(2,2,3)
plt.plot(Xpoints3, Ypoints3, c = "k")
plt.fill(Xpoints3,Ypoints3, color = "lightblue")
plt.title("concavo".upper(), y= 0.4, c ="k", x = 0.35)
plt.grid()


Xpoints4 = np.array([1,1,5,5,1])
Ypoints4 = np.array([1,5,5,1,1])
plt.subplot(2,2,4)
plt.plot(Xpoints4, Ypoints4, c = "k")
plt.fill(Xpoints4,Ypoints4, color = "green")
plt.title("cuadrado".upper(), y=0.4)
plt.grid()

plt.suptitle("figuras geometricas".upper())
plt.show()"""


# DISPERSION DE GRAFICAS
# es un diagrama de dispersion que traza un punto por cada observacion y necesita 2 matrices
# de la misma longitud : valores ejes X y Y.

"""import matplotlib.pyplot as plt 
import numpy as np

Xpoints = np.array([2,6,10,8,11,7,6,5,1,4,2,6,2])
Ypoints = np.array([1,3,1,5,7,7,11,7,7,5,1,3,1])
#plt.scatter(Xpoints,Ypoints, color = "yellow") usamos la bandera de color

#colors = np.array(["red","green","blue","yellow","pink","black","orange",
#                   "purple","beige","brown","gray","magenta"]) #usamos la matriz de colores

colors = np.array([0,10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90,100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,70])

#plt.scatter(Xpoints, Ypoints, c= colors)
#plt.scatter(Xpoints, Ypoints, c= colors, cmap= "viridis") # usamos el argumento cmap = "viridis"
#plt.colorbar() mostrar los niveles del mapa
#plt.scatter(Xpoints,Ypoints, color = "k", s= 500) # aumemtar el tamaño de los puntos
plt.scatter(Xpoints,Ypoints,c = colors ,s= sizes, cmap= "viridis", alpha= 0.5)
plt.colorbar()
plt.show()"""


"""import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()"""


# BARRAS 

"""import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

#plt.bar(x,y) # dibujamos la barra vertical
#plt.barh(x,y) # dibujamos la barra horizontal
#plt.bar(x,y, width= 0.3) #establecemos las barras verticales
#plt.barh(x,y,height=0.3) # establecemos las barras horizontales
plt.show()"""


# HISTOGRAMAS

"""import numpy as np
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
"""


# GRAFICOS CIRCULARES

"""import matplotlib.pyplot as plt 
import numpy as np  

colors = (["red", "blue", "yellow", "green"])
explotar = [0,0.5,0.5,0]
y = np.array([35, 25, 25, 15])
labels = ["manzana", "melocoton", "banana", "pera"] # etiquetas los nombres cada cuña
#plt.pie(y, colors = colors, labels= labels)
#plt.pie(y, colors = colors, labels= labels, startangle= 90, explode= explotar) # usamos explode() para distanciar cada cuña
plt.pie(y, colors = colors, labels= labels, shadow= True)
plt.legend(title = "cuatro frutas") # usamos legend() opcional el titulo
plt.show() """





