import random
import datetime


id_vendedores = [f'V{i}' for i in range(1, 51)]

with open('ventas1.txt', 'w') as archivo:
    for _ in range(100):
        id_vendedor = random.choice(id_vendedores)
        unidades_vendidas = random.randint(1, 10)
        precio_unitario = round(random.uniform(1, 10))

        # Escribe la línea en el archivo
        linea = f'{id_vendedor},{unidades_vendidas},{precio_unitario}\n'
        archivo.write(linea)

print("Archivo 'ventas.txt' generado con éxito.")