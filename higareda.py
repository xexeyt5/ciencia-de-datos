import tkinter as tk
import customtkinter
import customtkinter as ctk

ventana = ctk.CTk()
ctk.set_appearance_mode("Dark")
ventana.geometry("500x400")
ctk.set_default_color_theme("green") 
ventana.title('simon')

boton = ctk.CTkButton(text='reiniciar', fg_color='red')
boton.pack(padx=10,pady=20) 

ventana.mainloop()