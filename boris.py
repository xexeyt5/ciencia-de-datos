import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageOps
import customtkinter
import customtkinter as ctk



def cargar_imagen():
    global imagen_actual, imagen_original
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        imagen_original = Image.open(ruta_imagen)
        imagen_actual = imagen_original.copy()  # Mantenemos una copia de la imagen original
        mostrar_imagen(imagen_original)

def mostrar_imagen(imagen):
    imagen.thumbnail((300, 300))
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Actualizar la etiqueta de la imagen
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

def aplicar_efecto(efecto):
    global imagen_actual
    if imagen_actual:
        if efecto == "Escala de Grises":
            imagen_actual = imagen_actual.convert("L")
        elif efecto == "Blanco y Negro":
            imagen_actual = imagen_actual.convert("1")
        elif efecto == "Filtro Sobel":
            imagen_actual = imagen_actual.filter(ImageFilter.FIND_EDGES)
        elif efecto == "Original":
            imagen_actual = imagen_original.copy()  # Revertir a la imagen original
        mostrar_imagen(imagen_actual)

def guardar_imagen():
    if imagen_actual:
        ruta_guardar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", ".png"), ("Archivos JPEG", ".jpg"), ("Todos los archivos", ".")])
        if ruta_guardar:
            imagen_actual.save(ruta_guardar)

# Crear una ventana de Tkinter
ventana = ctk.CTk()
ctk.set_appearance_mode("Dark")
ventana.geometry("500x400")
switch_var = customtkinter.StringVar(value="on")
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")  
ventana.title("Procesamiento de Imágenes")

# Botón para cargar una imagen
boton_cargar = ctk.CTkButton(ventana, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack(pady=10)

# Etiqueta para mostrar la imagen
etiqueta_imagen = ctk.CTkLabel(ventana, text="")
etiqueta_imagen.pack()

# Opciones para aplicar efectos
opciones_efectos = ["Escala de Grises", "Blanco y Negro", "Filtro Sobel", "Original"]
menu_efectos = tk.StringVar(value=opciones_efectos[0])
menu_desplegable = tk.OptionMenu(ventana, menu_efectos, *opciones_efectos)
menu_desplegable.place(x=340, y=10)

combobox = customtkinter.CTkOptionMenu(master=ventana,
                                     values=["escala de grises", "blanco y negro", "filtro sobel", "original"],
                                      command=aplicar_efecto)
combobox.place(x=10,y=50)

# Botón para aplicar el efecto seleccionado
boton_aplicar_efecto = ctk.CTkButton(ventana, text="Aplicar Efecto", command=lambda: aplicar_efecto(menu_efectos.get()))
boton_aplicar_efecto.place(x=10 , y=10)

# Botón para guardar la imagen
boton_guardar = ctk.CTkButton(ventana, text="Guardar Imagen", command=guardar_imagen)
boton_guardar.place(x=180, y=350)

# Variables para almacenar la imagen actual y la imagen original
imagen_actual = None
imagen_original = None

ventana.mainloop()