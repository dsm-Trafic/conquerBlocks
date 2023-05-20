nombres_usuario = ["juan123", "ana456", "pedro789"]
passwds = ["clave123", "clave456", "clave789"]

# De la siguiente manera uno ambas listas para generar una lista anidada con los pares nombre_usuario - passwd
lista_acceso = list(zip(nombres_usuario, passwds))
print(lista_acceso)

intentos = 3
login = False
while intentos > 0 and not login:   # Damos 3 intentos para introducir los datos
    user = input("Introduce el nombre de usuario: ")
    passwd = input("Introduce la contraseña: ")    

    # A continuación verifico si la lista con el par user - passwd está en la lista anidada "lista_acceso"
    if (user, passwd) in lista_acceso:
        login = True
    else:
        intentos -= 1
        print("\33[31mUsuario o contraseña incorrecto.\33[0m")
        if intentos > 0: print("Le quedan "+(str(intentos))+" intentos")

if login:
    print("\33[1mHola de nuevo "+user+"\33[0m")
else:
    print("Su cuenta ha sido bloqueada.")
    