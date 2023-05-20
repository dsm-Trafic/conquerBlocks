numero = input("Ingrese numero con mas de una cifra ")

if not(len(numero) > 1) :
    raise Exception("Debe ingresar numero con mas de una cifra")
for cifra in numero :
    print(cifra)

    
