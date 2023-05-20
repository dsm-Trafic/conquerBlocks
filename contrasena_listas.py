'''Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios 
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos. 
Pista 1: Puedes crear dos listas, una con los nombre de usuario como por ejemplo...
nombres_usuario = ["juan123", "ana456", „pedro789"] 
Y otra lista con las contraseñas guardadas para cada usuario... 
contraseñas = ["clave123", "clave456", „clave789"] 
Otra opción puede ser que crees una lista de listas con la forma: 
nombres_contraseñas = [ ["juan123“,"clave123"] , ["ana456“,“clave456“] , ["pedro789“,  
"clave789“] ] 
Despues puedes pedir el usuario y contraseña y comprobar si coinciden. 
Pista 2: Para verificar si el usuario y contraseña son correctos puedes crear un bucle donde 
recorras los nombres de usuario y compruebes con un if si el nombre de usuario introducido y la 
contraseña coinciden con los datos de tus listas'''

from termcolor import colored

# --- creamos la lista con usuario y contraseña
nombres_contraseñas = [['juan123','clave123'],['ana456','clave456'],['pedro789','clave789']] 
intentos = 0
contraseña_ingresada = False
# --- vamos a dar 3 intentos para que ingrese los datos
while intentos < 3: 
        # --- pedimos por pantalla el usuario y la contraseña
        usuario = input('Ingrese su usuario: ')
        contraseña = input('Ingrese su contraseña: ')
        intentos += 1
        # --- corroboramos que esten bien sino volvemos a pedir los datos
        for i in range(0,len(nombres_contraseñas)):
            if usuario == nombres_contraseñas[i][0] and contraseña == nombres_contraseñas[i][1]:
                print(colored(f'Acceso permitido ¡Bienvenido al sistema {nombres_contraseñas[i][0]}!','magenta'))
                intentos = 3 
                contraseña_ingresada = True 
        if contraseña_ingresada == False:
             # si los intentos son > que 3 el acceso esta denegado y se termina el programa
             if intentos < 3:
                 print(colored('Los datos ingresados son invalidos. Ingrese de nuevo su usuario y contraseña','blue'))
             else:
                  print(colored('Usted no tiene mas intentos. ¡Acceso denegado!','red'))
                
            