'''
GRUPOS DE ALUMNOS:
En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos 
lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la 
M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y 
R hasta la Z se les ha asignado al grupo A también, el resto están en el B. 
Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por 
pantalla el grupo que le corresponde a ese alumno
Grupo a --> mujer entre e-m           hombre a - h r-z
grupo b --> mujer entre a-d y n-z     hombre i - r

'''
from unicode import unicode
grupo_A = []
grupo_B = []

dic_nombres = {"Pablo":"H", "anA":"M", "Ángel":"H", "élida":"M", "Íñigo":"H", "Úrsula":"M", \
    "Ñoño": "H", "óscar":"H", "María": "M", "isabel":"M", "Noelia":"H", "Antonio":"H", "Héctor":"H"}


# función para asignar grupos según los valores y claves del diccionario
def asignar_Grupo(nombre, sexo):
    sin_Acentos = unicode(nombre)
    if (sexo == "M") :
        if ("E"<= sin_Acentos.upper()[0] <= "M"):
            grupo_A.append(nombre.title())
        else:
            grupo_B.append(nombre.title())
    if (sexo == "H"):
        if ("I"<= sin_Acentos.upper()[0] <= "R"):
            grupo_B.append(nombre.title())
        else:
            grupo_A.append(nombre.title())

# Función para mostrar los grupos.
def mostrar_Datos():
    print("\n Grupo A: ", grupo_A)
    print("\n Grupo B: ", grupo_B)
    print()


# Algoritmo principal.
for nombre, sexo in dic_nombres.items():            # para asignar los valores existentes del diccionario.
    asignar_Grupo(nombre, sexo)                     # Asignamos grupos.
mostrar_Datos()                                     # Mostramos grupos.
control = False
while control==False:                    # while para pedir más datos de alumnos para añadir al diccionario y asignarle grupo.
    try: 
        nombreIntroducido = input("Introduzca un nuevo nombre: ")
        if (len(nombreIntroducido)) == 0:          # Controlamos excepciones de errores al introducir datos.
            raise IndexError ("*Error. No ha introducido nada.")
        sexo_Introducido = str.title(input("Introduzca su sexo(H/M): "))
        if (len(sexo_Introducido)) == 0:
            raise IndexError ("*Error. No ha introducido nada.")
        if sexo_Introducido.upper() != "H" and sexo_Introducido.upper() != "M":
            raise ValueError ("*Error. Respuesta incorrecta.")
    except IndexError as error:
        print(error)
    except ValueError as error:
        print(error)
    except:
        print("Error genérico.")
    else:                                 # Si no hay excepciones añadimos los nuevos datos al diccionario.
        dic_nombres[nombreIntroducido]=sexo_Introducido           
        asignar_Grupo(nombreIntroducido,sexo_Introducido)       # Asignamos grupo con los nuevos valores.
        #print(dic_nombres)     # Instrucción comentada de control para ver el diccionario si se modificaba.                
        print("\n Datos introducidos en la lista de alumnos.")
    finally:
        while True:                     # Aprovechamos finally para saber si quiere introducir nuevos datos.
            respuesta = input("\nDesea introducir otro dato(S/N): ")  #Controlamos excepciones y volvemos al while o salimos de el según corresponda.
            if respuesta.upper() == "N":
                print("\nLISTA FINAL ORGANIZADA POR GRUPOS:")
                mostrar_Datos()
                control=True
                break            
            elif respuesta.upper() == "S" :
                continue
            else:
                print("Error. Respuesta incorrecta.")


