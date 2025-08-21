import tkinter as tk 

apk = tk.Tk()
apk.title("hello babrbie girl")
apk.geometry("300x500") # anchoxalto
apk.configure(background = "black")


# establecer propiedades de la ventana

tk.Wm.wm_title(apk, "hello adriana")
entrada = tk.StringVar(apk)
palabra = tk.StringVar(apk)
apk.config(background = "yellow")
apk.geometry("400x400+100+200")
apk.resizable(width= True, height= False)


def amiga():
    print(entrada.get())

def today():
    palabra.set(entrada.get())



# creamos los widgets

boton = tk.Button(apk, text="pulsa aqui", font= (12),command= amiga , bg= "green", fg= "white")
etiqueta = tk.Label(apk, text="hello rock!", font=(15), bg="black", fg= "white",justify="center")
entrada = tk.Entry(apk, font=(17), bg= "orange", fg= "white", justify= "center")


# orgranizar widgets

etiqueta.pack(fill= tk.BOTH, expand= False)
boton.pack(fill= tk.BOTH, expand= True)
entrada.pack(fill= tk.BOTH, expand= True)

apk.mainloop()