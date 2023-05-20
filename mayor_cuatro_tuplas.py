''' 
Este es la solucion al ejercicio
"Mayor de cuatro" si queremos que 
nos devuelva la secuencia de numeros
ordenados de manera ascendente
'''

# --- Pedir NUMEROS al usuario
a = float(input("Introduce un numero: "))
b = float(input("Introduce otro numero: "))
c = float(input("Introduce otro numero: "))
d = float(input("Introduce otro numero: "))


if (a > b):
    a, b = b, a
if (a > c):
    a, c = c, a
if (a > d):
    a, d = d, a
if (b > c):
    b, c = c, b
if (b > d):
    b, d = d, b
if (c > d):
    c, d = d, c

print(" El mayor de los 4 es ", d)
print("El orden de los numeros es: ", a, b, c, d)

'''
# --- Pedir NUMEROS al usuario
a = float(input("Introduce un numero: "))
b = float(input("Introduce otro numero: "))
c = float(input("Introduce otro numero: "))
d = float(input("Introduce otro numero: "))


# --- Imprimir el mayor de los cuatro numeros
if (a>b):
    a, b = b, a 

if (b>c):
    b, c = c, b

if (c>d):
    c, d = d, c

print(" El mayor de los 4 es ", d)
print("El orden de los numeros es: ", a, b, c, d)
'''
