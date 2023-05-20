#Pedimos los numeros por pantalla
num_1 = float(input("Dime un numero: ").replace(',','.')) # Cambiamos comas por puntos

num_2 = float(input("\nDime otro numero: ").replace(',','.')) # Cambiamos comas por puntos
# Con el condicional if si el divisor es cero damos error si no damos el resultado
if num_2 == 0:
    print ('No se pueden dividir los numeros entre' , 0)
else:
    resultado = num_1/num_2
    print ('El resultado de la division de ' , num_1 , '/' , num_2 , ' es: ' , resultado)