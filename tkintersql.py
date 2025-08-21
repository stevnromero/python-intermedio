import sqlite3
import tkinter as tk
from tkinter import messagebox

# --------------------
# Configuración DB
# --------------------
conn = sqlite3.connect('contactos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
''')
conn.commit()

# --------------------
# Funciones
# --------------------
def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    
    if nombre and telefono:
        cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
        conn.commit()
        messagebox.showinfo("Éxito", "Contacto agregado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        mostrar_contactos()
    else:
        messagebox.showwarning("Error", "Debe ingresar nombre y teléfono.")

def mostrar_contactos():
    lista_contactos.delete(0, tk.END)
    cursor.execute("SELECT * FROM contactos")
    for row in cursor.fetchall():
        lista_contactos.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")

def eliminar_contacto():
    try:
        seleccionado = lista_contactos.get(lista_contactos.curselection())
        id_contacto = seleccionado.split(" - ")[0]
        cursor.execute("DELETE FROM contactos WHERE id=?", (id_contacto,))
        conn.commit()
        messagebox.showinfo("Éxito", "Contacto eliminado.")
        mostrar_contactos()
    except:
        messagebox.showwarning("Error", "Debe seleccionar un contacto para eliminar.")

# --------------------
# Interfaz gráfica
# --------------------
ventana = tk.Tk()
ventana.title("Gestión de Contactos")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=1, column=1, padx=10, pady=10)

btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_contacto)
btn_agregar.grid(row=2, column=0, columnspan=2, pady=10)

lista_contactos = tk.Listbox(ventana, width=40)
lista_contactos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

btn_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_contacto)
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=10)

mostrar_contactos()

ventana.mainloop()
