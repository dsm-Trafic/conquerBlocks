'''
Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado. 
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script 
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo 
introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y 
si se le cuela una almohadilla (p.e se#rgio)?
'''
import re #importamos la biblioteca expresiones regulares.


print("+++++ Inicio de Sesión +++++")

# función donde comprobamos si el usuario lo tenemos regirstrado, recibimos variable nombre.
def comprobar_Usuario(nombre): 
    if nombre == "Alejandro" or nombre == "Naomi" or nombre == "Sergio":
        print("Bienvenido usuario registrado " + nombre + "!")
    else:
        print("Bienvenido usuario sin registrar llamado " + nombre + "!")


# función donde solicitamos el nombre de usuario, y comprobamos su formato. Devolvemos la variable final.
def comprobar_Introduccion_Datos():
    nombre = input("Por favor, introduzca su nombre de usuario: ")

    # Usamos la biblioteca importada re
    # re.sub sustituirá los valores buscados por el caracter vacio ""

    # [^a-zA-Z]+, ^indica negación, 
    #             a-z indica valores entre a y z
    #             A-Z indica valores entre A y Z
    #             + indica buscar más de una coincidencia
    # En resumen, los corchetes busca todos los caracteres que no estén entre a-z y A-Z
    #             tmb busca letras y vocales con acentos.
    # "", nombre)
    # Esta parte, sustituye por ""(o lo que nosotros quisieramos) y lo guarda en nombre.
    nombre = re.sub("[^a-zA-ZÀ-ÖØ-öø-ÿ ]+", "", nombre)
    
    # Formateamos la variable nombre con .title()
    nombre = str.title(nombre)
    # Devolvemos la variable
    return nombre 



#Ejecutamos funciones.
nombre = comprobar_Introduccion_Datos()
comprobar_Usuario(nombre)
print("")

'''

Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos 
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario, 
comprueba si es una contraseña segura e indícalo por pantalla.

import re #Importamos la biblioteca re. 

print("++ Contraseña Segura. ++")
print("++++++++++++++++++++++++\n")

# Función que devuelve la contraseña solicitada
def leer_Contraseña():
    print('Consejos para contraseña segura:\n
    - Mínimo 8 caráctreres.\n 
    - Mínimo 1 vocal en minúscula y otra mayúscula.\n
    - Debe incluir al menos * y #\n
    - No se permite ningún otro caracter.\n')
    contraseña = str(input("Por favor, introduzca una contraseña: "))
    return contraseña

# Función que comprueba la contraseña pasada como valor
# Usamos la función de la biblioteca re.search que busca en el string
# devuelve un boolean según proceda
# [aeiou] controlo las 5 vocales (no acepto vocales con acentos)
# [*] controlo el *
# [#] controlo el #
# [A-Z] controlo que tenga al menos una mayúscula
# len(contraseña) >=8 controlo que tenga al menos 8 caracteres
# si pasa todos los filtros, aceptamos contraseña.
#
# if re.search("^[A-za-z*#]+$", contraseña): con este if filtro no aceptar otra cosa que no sea
# letras mayúsculas y minúsculas, * y #, tampoco acepto _ ni espacios.
# ^ niega lo que tenemos entre corchetes.
#    el + busca una o más coincidencias con los caracteres.
#    el $ indica que el patron debe encontrarse al final de la cadena.
def control_Contraseña(contraseña):
    if re.search("^[A-Za-z*#]+$", contraseña):
        if re.search("[aeiou]", contraseña) and \
        re.search("[*]", contraseña) and re.search("[#]", contraseña) and \
        re.search("[A-Z]", contraseña) and (len(contraseña) >=8):
            print("Su contraseña es SEGURA!")
        else:
            print("Su contraseña no es segura!")
    else:
        print("Su contraseña contiene caracteres no permitidos.")

#Ejecutamos el programa
contraseña = leer_Contraseña()
control_Contraseña(contraseña)

'''



