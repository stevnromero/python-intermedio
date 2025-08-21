import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

nombre = "Instructora Johanna"
dulce = "Bon Bon Bum"

def amistad(respuesta):
    if respuesta.lower() == "si":
        messagebox.showinfo("Respuesta", f"¡Hola compañero! Acepto compartir {dulce} contigo 😊🍭")
    elif respuesta.lower() == "no":
        messagebox.showerror("Respuesta", f"No lo siento mucho, perdoname 😢")
    else:
        messagebox.showwarning("Advertencia", "Por favor elige SI o NO")

window = tk.Tk()
window.title("Bienvenido al amor")
window.geometry("600x450")



etiqueta = tk.Label(window, text=f"hola {nombre}, como se encuentra el dia de hoy?.\n He alcanzado a un python intermedio", bg="blue", font=("Arial", 17), fg="white")
etiqueta.pack(fill=tk.BOTH, expand= True)

# creamo la etiqueta
imagen = Image.open("dulce.jpg")
imagen_2 = ImageTk.PhotoImage(imagen)
etiqueta_2 = tk.Label(window, image= imagen_2, bg= "#42353F")
etiqueta_2.pack(fill=tk.BOTH, expand= True)


etiqueta_1 = tk.Label(window, text=f"{nombre}, ¿compartamos {dulce}?😊💕", bg= "red", font=("Arial", 17), fg="white")
etiqueta_1.pack(fill=tk.BOTH, expand= True)




# Botones que pasan la respuesta a la función
si = tk.Button(window, text="SI", command=lambda: amistad("si"), justify="left")
no = tk.Button(window, text="NO", command=lambda: amistad("no"), justify="right")

si.pack(fill=tk.BOTH)
no.pack(fill=tk.BOTH)

window.mainloop()