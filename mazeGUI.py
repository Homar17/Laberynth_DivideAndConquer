import tkinter as tk

def open_options_window():
    # Cerrar la ventana principal
    root.destroy()

    # Crear una nueva instancia de Tk para la ventana de opciones
    options_root = tk.Tk()
    options_root.title("Medida del Laberinto")
    options_root.geometry("300x100")


    rows_label = tk.Label(options_root, text="Número de filas:", font=("Berlin Sans FB Demi", 12))
    rows_label.grid(row=0, column=0)
    rows_entry = tk.Entry(options_root)
    rows_entry.grid(row=0, column=1)


    cols_label = tk.Label(options_root, text="Número de columnas:", font=("Berlin Sans FB Demi", 12))
    cols_label.grid(row=1, column=0)
    cols_entry = tk.Entry(options_root)
    cols_entry.grid(row=1, column=1)


    start_button = tk.Button(options_root, text="Comenzar juego", font=("Berlin Sans FB Demi",9))
    start_button.grid(row=2, columnspan=2)


# Crear ventana principal de tkinter
root = tk.Tk()
root.title("Laberinto")
icono = tk.PhotoImage(file="mazeicon.png")
root.iconphoto(True, icono)

# Etiqueta adicional en la ventana principal
label = tk.Label(root, text="¡Bienvenido al juego del laberinto!", font=("Berlin Sans FB Demi", 14))
label.pack()

label_2 = tk.Label(root, text="Creado por el equipo 5", font=("Berlin Sans FB Demi", 10))
label_2.pack()

# Botón para abrir ventana de opciones
start_button = tk.Button(root, text="Comenzar",font=("Berlin Sans FB Demi", 9), command=open_options_window)
start_button.pack(pady=20)

root.mainloop()
