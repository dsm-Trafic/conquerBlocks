'''
Crea un script que dada una lista de listas M (numérica), 
identifique si se trata de una matriz y en ese caso imprima dos listas correspondientes a:
1. La fila cuyos elementos suman el máximo
2. La columna cuyos elementos suman el máximo
'''

M1=[[2,5,3],
    [6,1,8],
    [7,5,4]] 
M2 = [[4,2,3],[4,5],[6,8,2]] 

#empezamos veficando si son matrices(igual num de filas y columnas)
matriz = True
numFilas = len(M1)
numColumnas = len(M1[0])
if numFilas == numColumnas :
    for i in range(0, numFilas):
        columnas = len(M1[i])
        if columnas != numColumnas :
            print("no es matriz")
            matriz = False
            break
#determinamos y logueamos la fila cuyos elem mas sumen
max = 0
if matriz :
    for i in range(0, numFilas):
        fila = M1[i]         # cada una de las filas
        sumaFila = sum(fila) # calculamos la suma de la fila
        
        # comprobamos si la suma de la fila es mayor al de la fila anterior
        if sumaFila > max:  
            max = sumaFila      # actualizamos el valor de la suma maxima
            numFila = i        # actualizamos el valor del indice de la
                                # fila con la suma mas alta
    print("La fila cuyos elementos suman el maximo es:", M1[numFila], "con una suma total de", max)

#determinamos y logueamos la columna cuyos elem mas sumen
if matriz :
    sumaMaxCol = 0                       # inicializamos la variable que guarda max de columnas
    numColumnas = len(M1[0])             # inicializamos la variable que numero de columnas de primera fila
    # recorremos todas las columnas de la matriz
    for j in range(0,numColumnas):     
        columna = []                   # inicializamos nuestra lista donde guardamos los valores
                                       # de cada columna en cada iteracion
        sumaCol = 0               # inicializamos la variable que contiene la suma de la columna

        # recorrer las filas de la matriz
        for fila in M1:
            sumaCol +=  fila[j]         # sumar cada elemento de la columna j
            columna.append(fila[j])     # añadir cada elemento de la columna j a nuestra lista columna
                        
        # comprobar si la suma de la columna es mayor a la suma de la columna anterior
        if sumaCol > sumaMaxCol:
            sumaMaxCol = sumaCol        # actualizamos el valor de la suma maxima
            columnaMax = columna[:]     # actualizamos el valor de la columna con suma maxima
            
    print("La columna cuyos elementos suman el maximo es:", columnaMax, "con una suma total de", sumaMaxCol)

'''
# otra forma de calcular la columna cuyos elementos sea la de mayor numero
M1=[[2,5,3],[6,1,8],[7,5,4]]

# si cumple que el numero de filas y columnas es el mismo
#if matriz :
sumaMaxCol = 0                       # inicializamos la variable que guarda max de columnas
numColumnas = len(M1[0])             # creamos variable que guarda el numero de columnas
numFilas = len(M1)                   # creamos variable que guarda el numero de filas

#creamos matriz para trasponer filas por columnas
trspList = [[row for col in range(numColumnas)] for row in range(numFilas)]
print(trspList)

#inicializamos trspList
for i in range(numFilas):
    for j in range(numColumnas):
        trspList[i][j] = 0
print(trspList)

#realizamos la trasposicion de filas y columnas
for i in range(numFilas):
    for j in range(numColumnas):
        trspList[j][i] = M1[i][j] 
print('matriz original: ', M1)
print('matriz traspuesta: ', trspList)  

# ahora podemos aplicar a las filas de la matriz traspuesta 
# el codigo de calculo de la fila con elem de mayor numero
#para saber cual es la columna max de la matriz original

'''
              
                

