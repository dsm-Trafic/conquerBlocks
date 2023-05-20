'''
EJERCICIOS 2B
MAYUSCULA O MINUSCULA (BONUS*):
Permite que el usuario introduzca una letra 
(del alfabeto latino) como input. Comprueba 
si esta es una mayúscula o una minúscula. 
'''

# --- Pedir al usuario una letra
letra = input("Introduce una letra: ")

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# --- Comprobacion del input
if len(letra) == 1:

    # --- Condicional
    # Si es mayuscula imprimiremos que es mayuscula
    if letra in letras_mayusculas:
        print("La letra es mayúscula")
    # Si es minuscula imprimiremos que es minuscula
    elif letra in letras_minusculas:
        print("La letra es minúsucla")
    # Si es un caracter no reconocido lo indicaremos
    else: 
        print("La letra introducido no es válida")

else:
    print("Error. Debe introducir una única letra")

##############################################################

