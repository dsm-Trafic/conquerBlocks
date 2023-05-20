import re 
abecedario = re.compile('[a-zA-z]')
x = False
while x == False :
    caracter = input("Introduce un caracter")
    if abecedario.search(caracter) == None :
        print("Error introduzca una letra del alfabeto latino")
    elif len(caracter) > 1 :
        print("Error introduzca un caracter solo")
    else :
        if caracter == caracter.lower() :
            print("Es una letra minúscula")
            x = True
        else :
            print("Es una letra mayúscula")
            x = True 