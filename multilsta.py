numIngr = input("ingresar dos enteros separados por comas:")
dim = [int(x) for x in numIngr.split(",")]
rowCant = dim[0]
colCant = dim[1]
multList = [[row for col in range(colCant)] for row in range(rowCant)]
print(multList)