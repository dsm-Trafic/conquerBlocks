numero = input("Ingrese numero con cuatro cifras ")

if not(len(numero) == 4) :
    raise Exception("Debe ingresar numero con cuatro cifras")
print(numero[::-1])