'''Escribe un programa que pida al usuario un número entero 
y muestre por pantalla una estructura como la de más abajo, 
donde el valor de entrada es el número de estrellas en el 
centro de la estructura.
*
** 
*** 
**** 
***** 
**** 
*** 
**
*

'''

# --- pedir al usuario un numero entero
num = int(input("Introduzca la anchura central (numero entero): "))
#num = 5
# --- bucle ascendente
for i in range(1, num + 1):
    print("*" * i + " " * (num - i))
# --- bucle descendente
for i in range(num-1,0,-1):
    print("*" * i + " " * (num - i))

################################################################

'''
Crea un script que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última.
'''
# --- pedir palabra al usuario
palabra = input("Ingrese una palabra: ")
longitud = len(palabra)

# --- bucle que recorra el string de atras en adelante
for i in range(longitud - 1, -1, -1):
    # imprimir cada letra
    print(palabra[i])

'''
otra forma
# --- pedir palabra al usuario
palabra = input("Ingrese una palabra: ")

for letra in palabra[::-1]:
    print(letra)
'''

#####################################################################



    
