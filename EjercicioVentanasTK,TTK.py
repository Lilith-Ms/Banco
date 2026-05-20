from tkinter import Tk, ttk, messagebox

def saludar():
    nombre = entrada.get()

    if nombre != "":
        messagebox.showinfo("Saludador con Validación", f"Hola {nombre}, bienvenid@")
    else:
        messagebox.showwarning("Advertencia", "Escriba un nombre")

def limpiar():
    entrada.delete(0, "end")
    entrada.focus()


root = Tk()
root.title("Saludo")
root.geometry("400x200")

frm = ttk.Frame(root, padding=10)
frm.grid()

lbl = ttk.Label(frm, text="Ingrese su nombre")
lbl.grid(column=0, row=0, padx=3, pady=5)

entrada = ttk.Entry(frm, width=30)
entrada.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

entrada.focus()


btn_saludar = ttk.Button(frm, text="Saludar", command=saludar)
btn_saludar.grid(column=0, row=2, padx=5)

btn_limpiar = ttk.Button(frm, text="Limpiar", command=limpiar)
btn_limpiar.grid(column=1, row=2, padx=5)

btn_salir = ttk.Button(frm, text="Salir", command=root.destroy)
btn_salir.grid(column=2, row=2, padx=5)

root.mainloop()