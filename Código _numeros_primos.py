''' 
Crea un programa que imprima todos los 
números primos entre el 2 y el 100. Un numero 
primo es un numero positivo y entero mayor que 
uno que no tiene un divisor positivo y entero 
que no sea 1 o sí mismo.
'''

# --- bucle que recorra los numeros del 2 al 100
for num in range(2,101):
    primo = True
    # --- para dicho numero, hay alguno que sea su divisor
    for i in range(2,num):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)

'''
for num in range(2,101):
    primo = True
    i = 2
    while primo == True and i < num:
        if num % i == 0:
            primo = False
        i += 1
        
    if primo:
        print(num)
'''

####################################################

'''
Dado una lista de números enteros, 
escribe un script en Python que 
devuelva una nueva lista con los 
números primos de la lista original. 
Además, el script debe devolver el número 
total de números primos encontrados y 
la suma de los números primos encontrados
'''

# --- lista de numeros enteros 
# + lista vacia para los numeros primos
# + numero total de numeros primos
# + suma de los numeros primos encontrados

numeros = [2,3,4,5,6,7,8,9,10]
primos = []
total_primos = 0
suma_primos = 0

# --- bucle para recorrer la lista de numeros
for numero in numeros:
    # comenzamos suponiendo que el numero es primo
    primo = True
    # comprobar si el numero es primo
    for i in range(2, numero):
        # si el numero es divisible por otro 
        # numero diferente a este o a 1 entonces
        # no es primo --> primo = False
        if numero % i == 0:
            primo = False

    ## si es primo lo añadimos a la nueva lista
    if primo == True:
        # añadimos el numero
        primos.append(numero)
        # aumentamos en uno el contador de numeros primos
        total_primos = total_primos + 1
        # sumamos este numero al total de la suma de numeros primos
        suma_primos = suma_primos + numero

# --- Imprimios los datos
print("Numeros primos:", primos)
print("Total de numeros primos:", total_primos)
print("Suma de numeros primos:", suma_primos)
print("Total de numeros primos:", len(primos))
print("Suma de numeros primos:", sum(primos))
##############################################################

