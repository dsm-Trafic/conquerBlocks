'''
contador lineas de archivo
xfile = open ("arch.txt")
count = 0
for line in xfile:
    count += 1
print("Line count:", count)

contador de caracteres, muestra primeros y ultimos 20
xfile = open ("arch.txt")
input = xfile.read()
print("total de char:", len(input))
print("primeros 20 char:", input[:20])
print("ultimos 20 char:", input[::20])

try: puede abrir el archivo
elimina espacios en lineas leidas desde archivo
busca "patron" en lineas leidas que comienzan con 'From:'

fileName = print("enter file name:")
try:
    fhand = open(fileName)
except:
    print("file ", fileName, " can not be opened") 
    quit()

for line in fhand:
    line = line.rstrip()
    if not(line.startswith('From:')):
        continue
    if not("patron" in line):
        continue
    print(line)

*******************************************************************************

contador de palabras en archivo

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

***********************************************************************************

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

'''