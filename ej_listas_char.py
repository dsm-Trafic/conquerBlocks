frutas = ['manzana','platano','cereza','pera','higo','frambuesa','fresa']

# metodo len para saber cuantos elem tiene la lista
longlista = len(frutas)

print(longlista)
print(frutas[2])
frutas[1] = 'mora'

#metodo append para agegar al linal de la lista
frutas.append('mango')

#metodo insert como primer elemento de la lista
frutas.insert(0,'uva')

#bucle for para recorrer lista
for fruta in frutas: print(fruta)

#metodo pop para eliminar ultimo elemento
ultima_fruta = frutas.pop(-1)
print(len(ultima_fruta))

#bucle while para recorrer lista, muestre para cada elem
# su len y muestre los que cumplan len(elem)>5
termino = False
contador = 0
max_frutas = []
while termino == False :
    if contador >= len(frutas):
        termino = True
        continue
    if contador <= len(frutas)-1:
        print(frutas[contador], len(frutas[contador]))
        if len(frutas[contador]) > 5 :
            print("agrego:",frutas[contador])
            max_frutas.append(frutas[contador])
        contador +=1
print(max_frutas)

#metodo remove por coincidencia con elem buscado
frutas.remove('cereza')
print(frutas)

#metodo clear para vaciar lista
max_frutas.clear()
print(max_frutas)




    