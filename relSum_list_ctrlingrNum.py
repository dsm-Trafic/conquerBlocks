# debe establecer si hay relacion de suma entre los numeros ingresados
#pido y contolo que sean numeros enteros y no esten repetidos,devuelvo lista valida
listNum = []
contador = 0
while True:
        if contador < 3 :
            num = int(input("\nIngrese numero entero: "))
            if isinstance(num,int):  
                listNum.append(num)
                contador = contador + 1
                
                if (len(listNum) != len(set(listNum))):
                    print("\nERROR: No debe ingresar numeros repetidos")
                    listNum.pop(-1)
                    contador = contador - 1
            else:
                print("\nERROR: Debe ingresar numeros enteros sin repetirlos")
        else:
            break
    
#controlo y despliego si existe relacion de suma entre numeros ingresados
if listNum[0] + listNum[1] == listNum[2]:
        print("\nLa suma de:", listNum[0], "mas ", listNum[1], "es igual a: ", listNum[2])
elif (listNum[0] + listNum[2] == listNum[1]):
        print("\nLa suma de:", listNum[0], "mas ", listNum[2], "es igual a: ", listNum[1])
elif (listNum[1] + listNum[2] == listNum[0]):
        print("\nLa suma de:", listNum[1], "mas ", listNum[2], "es igual a: ", listNum[0])
else:
        print("\nLos numeros ingresados: ", listNum(), "no tienen relacion de suma entre ellos")

