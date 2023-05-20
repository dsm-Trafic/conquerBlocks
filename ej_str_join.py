lista = []
for i in range(2900,3000):
    if (i%7 == 0):
        lista.append(str(i))
    print(",".join(lista))
