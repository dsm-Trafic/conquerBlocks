def ingresoLista():
    numIngresados = input("Ingresar numeros separados por coma: ")
    lista = [int(x) for x in numIngresados.split(",")]
    return(lista)

def mayor(lista):
    max = lista[0];
    for i in lista:
        if i > max:
            max = i
    return max    
 
def menor(lista):
    min = lista[0];
    for i in lista:
        if i < min:
            min = i
    return min
 
def main():
    lista = ingresoLista()
    print ("La lista es ", lista)
    print ("El número mayor es ", mayor(lista))
    print ("El número menor es ", menor(lista))
    print ("Usando las funciones estándar de Python")
    print ("El número mayor es: ", max(lista))
    print ("El número menos es: ", min(lista))


main()