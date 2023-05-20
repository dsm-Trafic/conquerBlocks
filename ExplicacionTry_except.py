import re
# Usamos un try:
#           except:
# Cuando queremos capturar alguna excepción(errores en el tipo de datos introducidos,
#  errores de tipo, errores con operaciones, 
# con variables no definidas,un for que se sale del indice,..) Para resumir,
#  practicamente todos los errores que te aparecen en la terminal
# cuando ejecutas y el programa peta.

# El código al que quieras controlar una excepción tienes que ponerlo dentro del try
# y en el except pones lo que pasa si ocurre.

# Ejemplos:
# Controlamos que solo me introduzca enteros y si introduce
#  una letra(por ejemplo) saltaría la excepción.
try:
        numero = int(input("Introduce un número: "))    
except:
        print("eso no es un número entero.")

# Controlamos una operación.
try:
        num = 2
        letra = "a"
        resultado = num + letra
except:
        print("No puede sumar letras y números.")

# Controlamos que una función o una variable no esté definida
#  (aunq de esto ya te avisa VSCODE realmente.)
try:
        funcion()
except:
        print("No existe esa función.")


# Ademas de las excepciones que ya controla el compilador,
#  tu puedes crear las tuyas.
# Por ejemplo, si necesitas que te introduzca una letra mayuscula,

try:
        letra = str(input("Introduce una letra: "))
        if not re.search("[A-Z]", letra):
                #Creas tu propia excepción para que el programa salte tan pronto lo encuentre.
                raise ValueError ("No ha introducido una letra mayuscula.")      
except ValueError as nombreError:                                                # 
        print(nombreError)


## NOTA IMPORTANTE
## Tan pronto encuentre la excepción salta automáticamente al except,
#  dejando sin ejecutar el resto del código que quede en el try.
#la idea es:
#le dices al programa, try(intenta este código)
#pero si salta algún error en la ejecución
#en vez de petarme el programa, saltas al except y haces lo que esta en la exception

#TIPOS ERROR

#Exception: es la clase base para todas las excepciones en Python. Cualquier excepción que
#  herede de esta clase se considera una excepción en general.

#ArithmeticError: es la clase base para todas las excepciones relacionadas
        #  con operaciones aritméticas. Esta clase incluye excepciones como 
        # OverflowError, ZeroDivisionError, y FloatingPointError.

#LookupError: es la clase base para todas las excepciones relacionadas con búsquedas.
        #  Esta clase incluye excepciones como IndexError y KeyError.

#AssertionError: se genera cuando una afirmación (assert) falla.

#AttributeError: se genera cuando se intenta acceder a un atributo o método que no existe en un objeto.

#EOFError: se genera cuando se intenta leer más allá del final de un archivo.

#FileNotFoundError: se genera cuando se intenta abrir un archivo que no existe.

#ImportError: se genera cuando se intenta importar un módulo que no existe.

#IndentationError: se genera cuando hay un error en la indentación del código.

#NameError: se genera cuando se hace referencia a una variable no definida.

#modificaciones del try except q tmb existen

#FORMATO GENERAL

#try:
    # intenta ejecutar este código
#except: <tipo_de_excepcion> as <variable>:
    #si ocurre una excepción de este tipo en try, detente y ejecuta éste código.
#else: 
    # si no ocurrio una excepción en try ejecuta este código
#finally:
     # Ejecuta este código haya ocurrido la excepción o no. 
     # Esta parte es para algo que debas realizar continuando el codigo 
     # despues del codigo del try o el de las excepciones si las hubiera. 
