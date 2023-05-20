'''
uso libreria re 
re.search() es igual a metodo find() de string
re.findall() extrae porciones que matchean idem find() y slicing

expresiones regulares
dot "." match any character
"*" by adding this matches any number of times
"^" match all characters that follows at the beginning of the search
"?" not greedy (devuelve exactamente la primera coincidencia)
por defecto si no esta "?" la extraccion es greedy (criterio mas amplio)
"(" desde, ")" hasta, marca lugar donde hacer la extraccion
ejemplos
^X.*: match todo lo que comienze con X seguido por todos los caracteres siguientes hasta el char :
^X- \s+ match todo lo que comienze con X seguido por todos los caracteres siguientes que no sean en blanco
[0-9]+ cero or mas numeros

importe re
fileName = print("enter file name:")
try:
    fhand = open(fileName)
except:
    print("file ", fileName, " can not be opened") 
    quit()

for line in fhand:                              x = 'From: using: tom@uct.ac.za Sst'
    line = line.rstrip()                        y = re.findall('F.+?:', x) greedy
                                                print(y)                   devuelve ['From:'] 
    if line.startswith('From:'):                y = re.findall('F.+:', x)  not greedy
    idem                                                            devuelve ['From: using:']
    if re.search('^From:', line):               
    
**********************************************************************************************
extraccion direcciones email x = 'From: using: tom@uct.ac.za Sst'

y = re.findall('\s?+@\s+', x)       greedy
print(y)                            devuelve ['m@uct.ac.za']
y = re.findall('\s+@\s+', x)        not greedy
print(y)                            devuelve ['tom@uct.ac.za'] 
y = re.findall('^From(\s+@\s+)', x) not greedy
                                    devuelve ['tom@uct.ac.za'] de lo que comienza con From
extraccion host version1
atposic = x.find('@')
finposic = x.find('',atposic)
host = x[atposic+1:finposic]

extraccion host version2
words = x.split()
email = words[1]
pieces = email.split('@')
host = pieces[1]

extraccion host version3
import re
host = re.findall('^From: .*@([^ ]*)')

**********************************************************************************************
busca precios en archivo($ seguido de numeros)
hace skip de linea si en la misma no hay matcheo
devuelve el mayor precio del archivo
importe re
fileName = print("enter file name:")
try:
    fhand = open(fileName)
except:
    print("file ", fileName, " can not be opened") 
    quit()
numList = list()
for line in fhand:
    line = line.rstrip() 
    num = re.findall('\$[0-9.]+', line)
    if len(num) != 1 : continue
    number = float(num[0])
    numList.append(number)
print("el mayor valor es:", max(numList))



'''