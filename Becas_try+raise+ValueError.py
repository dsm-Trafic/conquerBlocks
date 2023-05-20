'''
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media. 
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que 
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
'''
# Creamos un bucle a la espera del break para cerrarse.
while True:
    # Abrimos un try - except para controlar los errores en la introducción de los datos.
    try:
        nombre = str.title(input("Introduzca su nombre: "))         
        edad = int(input("Introduzca sus edad: ")) 
        if edad < 17 or edad > 21: 
            # Si no los cumple creamos una excepción con mensaje especifico.
            raise ValueError ("Lo sentimos, no cumple la condición de la edad.(17-21)\n") 
        else: 
            nota_Media = float(input("Introduzca su nota media: ")) 
            if nota_Media < 8: 
                # Si es una nota media inferior a la nota mínima creamos una excepción con mensaje especifico.
                raise ValueError ("\nLo sentimos, su nota media no alcanza para la beca.\n")
            elif nota_Media > 10: 
                # Si es una nota media supera la nota máxima creamos una excepción con mensaje especifico.
                raise ValueError ("\nError, su nota media no puede ser superior a 10.\n")
            else: 
                print("\nENHORABUENA! CUMPLE TODAS LAS CONDIONES PARA LA BECA!\n")
                break 
    except ValueError as error:
         # Excepciones
         # Controlamos a través del texto mostrado si es una excepción creado por nosotros
         # o una excepción creada por el interprete de python. Para mostras los mensajes
         # anteriomente creados o mostras un mensaje nuevo para las creadas por el intérprete.
        if "su nota media" in str(error) or "Lo sentimos" in str(error) :    
            print(error)                                    
            break                                                                
        else:
            print("\nError en la introduzción de los datos. Vuelva a intentarlo.\n")
            
