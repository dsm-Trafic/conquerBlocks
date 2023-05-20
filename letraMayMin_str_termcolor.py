from termcolor import colored
import time
# Pedimos una letra del alfabeto latino al usuario
letra = str(input('\nDime una letra del alfabeto latino:\n'))
# Comprovamos si la letra introducida esta en mayusculas o minusculas con issuper que nos devolvera
# si esta en minusculas false y si esta en mayusculas true
for index in range(len(letra)):
    # Controlamos los espacios
    if letra[index].isspace() == True:
        print (colored('Tenemos un espacio\n', 'red'))
    else:
        # Controlamos que sea minuscula
        if letra[index].isupper() == False:
            print (colored(letra[index], 'magenta'))
            print (colored('la letra introducida esta en minusculas\n', 'magenta'))
            time.sleep(1) 
        # Controlamos que sea mayuscula
        elif letra[index].isupper() == True:
            print (colored(letra[index], 'cyan'))
            print (colored('La letra esta en mayusculas\n', 'cyan'))
            time.sleep(1)