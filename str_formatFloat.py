cantVtaAutoA = input("Ingrese cantidad de autos vendidos Serie 1: ")
cantVtaAutoB = input("Ingrese cantidad de autos vendidos Serie +: ")
cantVtaAutoC = input("Ingrese cantidad de autos vendidos Serie 4x4: ")
comisVtaAutoA = float(cantVtaAutoA) * 20000 * .03
comisVtaAutoB = float(cantVtaAutoB) * 35000 * .05
comisVtaAutoC = float(cantVtaAutoC) * 60000 * .07
comisTotal = comisVtaAutoA + comisVtaAutoB + comisVtaAutoC
msg = "El total de comisiones a pagar es: {:.2f}"
print(msg.format(comisTotal))
