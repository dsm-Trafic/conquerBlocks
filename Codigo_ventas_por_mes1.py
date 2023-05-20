"""
ANALISIS DE DATOS - VENTAS POR MES
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año. 
Cada fila representa una venta y tiene tres columnas: la fecha de la venta,
el monto de la venta y la categoría de producto vendido .
Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en cada mes. 
Para ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas,
donde n es el número de ventas. Luego, puedes usar operaciones de NumPy para filtrar
los datos por mes y sumar los montos de venta correspondientes.
(Pista: puedes cambiar el tipo de dato del array de string a entero usando array[:,i].astype(int) )
"""

import numpy as np
#import termcolor
#from termcolor import colored

#definimos el array de ventas. Aclaracion: al array se le pueden ir agregando ventas 
ventas = np.array([
    ["2022-01-01", 100, "ropa"],
    ["2022-01-02", 200, "alimentos"],
    ["2022-01-03", 150, "ropa"],
    ["2022-02-01", 120, "alimentos"],
    ["2022-02-02", 180, "electronicos"],
    ["2022-02-03", 200, "alimentos"],
    ["2022-03-01", 90, "ropa"],
    ["2022-03-02", 110, "electronicos"],
    ["2022-03-03", 100, "alimentos"],
    ["2022-12-31", 100, "alimentos"],
])

#guardamos en variables distintas las columnas
fechas = ventas[:,0]
venta_dia = ventas[:,1].astype(int)
categoria = ventas[:,2]

#contamos cuantas filas tiene el array para luego recorrerlo (es la cantida de ventas totales)
num_filas = ventas.shape[0]
print("----- CANTIDAD DE VENTAS TOTALES -----")
print("Se realizaron", num_filas, "ventas")

#creamos el array mes para contar las ventas por mes del array ventas
# y el array venta_mes para acumular la venta de cada mes
mes = np.zeros([12]).astype(int) #convertimos los datos del array a integer para eliminar el ".0"
venta_mes = np.zeros([12])

for i in range(0, num_filas):
    if fechas[i] >= "2022-01-01" and fechas[i] <= "2022-01-31":
        mes[0] += 1 #contamos la cantidad de ventas en el mes
        venta_mes[0] += venta_dia[i] #sumamos la cantidad de ventas del mes
    elif fechas[i] >= "2022-02-01" and fechas[i] <= "2022-02-31":
        mes[1] += 1
        venta_mes[1] += venta_dia[i]
    elif fechas[i] >= "2022-03-01" and fechas[i] <= "2022-03-31":
        mes[2] += 1
        venta_mes[2] += venta_dia[i]
    elif fechas[i] >= "2022-04-01" and fechas[i] <= "2022-04-31":
        mes[3] += 1
        venta_mes[3] += venta_dia[i]
    elif fechas[i] >= "2022-05-01" and fechas[i] <= "2022-05-31":
        mes[4] += 1
        venta_mes[4] += venta_dia[i]
    elif fechas[i] >= "2022-06-01" and fechas[i] <= "2022-06-31":
        mes[5] += 1
        venta_mes[5] += venta_dia[i]
    elif fechas[i] >= "2022-07-01" and fechas[i] <= "2022-07-31":
        mes[6] += 1
        venta_mes[6] += venta_dia[i]
    elif fechas[i] >= "2022-08-01" and fechas[i] <= "2022-08-31":
        mes[7] += 1
        venta_mes[7] += venta_dia[i]
    elif fechas[i] >= "2022-09-01" and fechas[i] <= "2022-09-31":
        mes[8] += 1
        venta_mes[8] += venta_dia[i]
    elif fechas[i] >= "2022-10-01" and fechas[i] <= "2022-10-31":
        mes[9] += 1
        venta_mes[9] += venta_dia[i]
    elif fechas[i] >= "2022-11-01" and fechas[i] <= "2022-11-31":
        mes[10] += 1
        venta_mes[10] += venta_dia[i]
    elif fechas[i] >= "2022-12-01" and fechas[i] <= "2022-12-31":
        mes[11] += 1
        venta_mes[11] += venta_dia[i]

#imprimimos las ventas por mes, cantidad y monto total
print("----- VENTAS POR MES -----")
for i in range(0,12):
    print("La cantidad de VENTAS realizadas en el mes",str(i+1),"es de",str(mes[i]),"y suma un total de: $",str(venta_mes[i]))