tiempoAtlA = input("Ingresar tiempo registrado por atleta A:\nminutos XX|segundos XX|centesimas XX\n")
cantSegAtlA = int(tiempoAtlA[0:1])*60 + int(tiempoAtlA[3:4]) + int(tiempoAtlA[6:7])/60
velMediaAtlA = cantSegAtlA / 100

tiempoAtlB = input("Ingresar tiempo registrado por atleta B:\nminutos XX|segundos XX|centesimas XX\n")
cantSegAtlB = int(tiempoAtlB[0:1])*60 + int(tiempoAtlB[3:4]) + int(tiempoAtlB[6:7])/60
velMediaAtlB = cantSegAtlB / 100 

tiempoAtlC = input("Ingresar tiempo registrado por atleta C:\nminutos XX|segundos XX|centesimas XX\n")
cantSegAtlC = int(tiempoAtlC[0:1])*60 + int(tiempoAtlC[3:4]) + int(tiempoAtlC[6:7])/60
velMediaAtlC = cantSegAtlC / 100

print(cantSegAtlA)
print('La veloc media del A es: '+ str(velMediaAtlA))
print(cantSegAtlB)
print('La veloc media del B es: '+ str(velMediaAtlB))
print(cantSegAtlC)
print('La veloc media del C es: '+ str(velMediaAtlC))
