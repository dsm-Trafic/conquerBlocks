restauranteDict = {
    "Ensalada mixta": 12,
    "Sopa pescado": 10,
    "Dorada al horno": 18,
    "Arroz al curry": 14,
    "Lasana de carne": 15,
    "Brownie chocolate": 8,
    "Helado": 6,
    "Refrescos": 5.5,
    "Cafe": 3.5
}

totalConsumo = 0

while True:
    consumoItem = input("Ingrese item ")
    if not(consumoItem) in restauranteDict.keys() :
        print("item no existe en carta")
    else:    
        cantItem = input("Ingrese cantidad ")
        for x, y in restauranteDict.items():
            if x == consumoItem :
                totalConsumo = totalConsumo + (int(cantItem) * y)                
    preg = input("incluir mas items? si|no ")
    if (preg == 'no'):
        break


print("el monto del consumo realizado es: EU "+ str(totalConsumo))


