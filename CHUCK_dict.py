'''
asignacion de valores a claves
purse = dict()
purse['money'] = 12
purse['candy'] = 3
print purse

metodo get desde una lista
counts = dict()
names = ['one','two','three','four']
for name in names:                          idem a:
    if name not in counts:                  counts[name] = counts.get(name,0)+1
        counts[name] = 1
    else:
        counts[name] +=1

metodo get desde texto ingresado que cuenta sus palabras
counts = dict()
line = input("ingresar una linea de texto: ")
words = line.split()
for word in words:
    counts[word] = counts.get(word,0)+1
print(counts)
for key in counts:
    print(key,counts[key])
    print(counts.keys())
    print(counts.values())
    print(counts.items())    devuelve en tuplas

    
devuelve palabra mas usada y las veces que aparece desde archivo txt ingresado
fileName = print("enter file name:")
try:
    fhand = open(fileName)
except:
    print("file ", fileName, " can not be opened") 
    quit()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if !words[0] or len(words)<1 :
        continue
    for word in words:
        counts[word] = counts.get(word,0)+1
contAparicPalabra = -1
palabraMasRepetida = None
for word,count in counts.items() :
    if count > contAparicPalabra :
        palabraMasRepetida = word
        contAparicPalabra = count
print(palabraMasRepetida, contAparicPalabra)


ordenar dict by values instead of key
c = dict()
c['a'] = 10
c['b'] = 22
c['c'] = 33
c['d'] = 44
tmpList = list()
for k,v in c.items() :                      idem a:
    tmpList.append((v,k))                   print(sorted([(v,k)for k,v in c.items()]))
tmpList = sorted(tmpList, reverse=True)
print(tmpList)
for v,k in tmpList[:10] :
    print(k,v)





'''