import random

# Función para generar datos aleatorios de ventas para un vendedor
def generar_ventas():
    return [random.randint(1000, 10000) for _ in range(5)]  # Genera 10 ventas aleatorias

# Generar datos para 100 vendedores
vendedores = []
for id_vendedor in range(1, 101):
    ventas = generar_ventas()
    vendedor = [id_vendedor] + ventas
    vendedores.append(vendedor)

# Escribir los datos en un archivo de texto
with open("ventas1.txt", "w") as archivo:
    for vendedor in vendedores:
        linea = ", ".join(map(str, vendedor))  # Convertir la lista a una cadena de texto
        archivo.write(linea + "\n")

print("Archivo 'datos_vendedores.txt' generado con éxito.")
