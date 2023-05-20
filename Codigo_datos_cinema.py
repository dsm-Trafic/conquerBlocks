'''DATOS CINEMATOGRÁFICOS 
Supongamos que tienes un conjunto de datos de películas que contiene información 
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar 
estos datos para determinar cuál es el género de película más popular, cuántas películas 
se lanzaron en cada década y cuál es la duración promedio de cada género de película.
(Pista 1: Tu array de entrada puede tener la forma…)
(Pista 2: puede ser util investigar np.unique, np.argsort y np.count_nonzero'''
import numpy as np
peliculas = np.array([
    ["Peli1", "comedia", 120, 1990, 8.5],
    ["Peli2", "accion", 110, 2005, 7.8],
    ["Peli3", "drama", 95, 2010, 6.9],
    ["Peli4", "comedia", 100, 1985, 7.5],
    ["Peli5", "accion", 130, 2015, 8.1],
    ["Peli6", "drama", 115, 2000, 6.7],
    ["Peli7", "comedia", 90, 1995, 8.2],
    ["Peli8", "accion", 105, 2010, 7.4],
    ["Peli9", "drama", 125, 1980, 6.8],
    ["Peli10", "comedia", 95, 2000, 8.0],
    ["Peli11", "comedia", 95, 2000, 8.0]
])

#buscar el genero mas visto
nombre, indice, visualizaciones = np.unique(peliculas[0:,1],return_index = True,return_counts=True)
#con este metodo podemos separar todos los datos en variables independientes
print(nombre,"\n",indice,"\n",visualizaciones)

#ordeno array visualizaciones de mayor a menor
array_visualiz_ordenado = np.argsort(visualizaciones)[::-1]
print(array_visualiz_ordenado)
# el nombre mas pop es el que tiene el indice igual al primer lugar
#del array ordenado de mayor a menor de visualizaciones
nombre_mas_pop = nombre[array_visualiz_ordenado[0]]

print("----------")
# y asi poder utilizar los datos obtenidos por separado
print("El genero mas popular es:", nombre_mas_pop,"\nCon un total de:",visualizaciones.max())
print("----------")


# si el caso fuera que tuvieramos miles de datos
# podriamos coger y concatenar las listas creadas pero en string
# y despues sacar los datos convirtiendolos de nuevo a integer
# numero de peliculas que se lanzaron en cada decada
#inicializamos las decadas en unas variables
decad_80 = 1980
decad_90 = 1990
decad_2000 = 2000
decad_2010 = 2010
# creamos un array de peliculas a las que le vamos a asignar la decada
array_pelic_x_año = np.zeros((4,2))
#colocamos las decadas en la primera columna
array_pelic_x_año[0,0],array_pelic_x_año[1,0],array_pelic_x_año[2,0],array_pelic_x_año[3,0], = 1980, 1990, 2000, 2010
# para cada pelicula en array peliculas segun el año de cada una lo suma en la posicion del array
# que corresponda a la decada en la que se produjo
for año_pelic in peliculas[:,3].astype(int):
    if año_pelic >= decad_80 and año_pelic < decad_90:
        array_pelic_x_año[0,1] += 1
    elif año_pelic >= decad_90 and año_pelic < decad_2000:
        array_pelic_x_año[1,1] +=1
    elif año_pelic >= decad_2000 and año_pelic < decad_2010:
        array_pelic_x_año[2,1] += 1
    else:
        array_pelic_x_año[3,1] += 1
print(array_pelic_x_año.astype(int))
print("----------")
# aqui pedimos que dentro de array_pelic_x_año nos busque la posicion
# donde se encuentra el valor maximo de la columna 1
fila, colum = np.where(array_pelic_x_año == array_pelic_x_año[:,1].max())
print(fila,colum)
print("La dec con mas pelic fue:",array_pelic_x_año[fila,0],"con un total de",array_pelic_x_año[fila,colum])

print("----------")
#duracion promedio por genero
#creamos arrays vacios para meter en cada array las duraciones para cada categoria
tiempo_comedia = np.empty(0)
tiempo_accion = np.empty(0)
tiempo_drama =np.empty(0)

#recorremos array peliculas guardando para cada categoria las duraciones de todas las peliculas
for i in range(len(peliculas[:,1])):
    if peliculas[i,1] == "comedia":
        tiempo_comedia = np.append(tiempo_comedia,peliculas[i,4].astype(float))
    elif peliculas[i,1] == "accion":
        tiempo_accion = np.append(tiempo_accion,peliculas[i,4].astype(float))
    elif peliculas[i,1] == "drama":
        tiempo_drama = np.append(tiempo_drama,peliculas[i,4].astype(float))
print("Tiempo promedio de peliculas de comedia es: ","{:.2f}".format(tiempo_comedia.mean()))
print("Tiempo promedio de peliculas de accion es: ","{:.2f}".format(tiempo_accion.mean()))
print("Tiempo promedio de peliculas de drama es: ","{:.2f}".format(tiempo_drama.mean()))