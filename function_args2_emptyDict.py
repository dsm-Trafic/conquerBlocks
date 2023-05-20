'''
Python no se limita a permitirnos aceptar argumentos posicionales ilimitados;
también nos da el poder de definir funciones con argumentos de palabras clave ilimitados.
La sintaxis es muy similar pero utiliza dos asteriscos **en lugar de uno.
Por lo general, los llamamos kwargscomo una forma abreviada de argumentos de palabras clave.
'''
def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)

# See if there's an 'anything_goes' keyword arg and print it
# print(kwargs.get('anything_goes'))
 
arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)
'''
Daría salida:
<class 'dict'>
{'this_arg': 'wowzers', 'anything_goes': 101}
101
Podemos observar dos cosas:
**kwargs toma la forma de un diccionario con todos los valores de
argumentos de palabras clave pasados ​​a arbitrary_keyword_args. 
Dado que **kwargs es un diccionario, podemos usar funciones de 
diccionario estándar como .get()recuperar valores.

Tal como vimos con *args, el nombre de kwargs es completamente arbitrario
'''
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)


#Checkpoint   **order_items argumento de funcion como dict vacio 
#                en el que se agrega order_items en dos claves
def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

# Checkpoint   Example Call
#llamada a funcion assign_food_items para un arg posicional table_number
# con contenido a ser agregado en dict para dos claves distintas

assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')

#imprimo tabla
print('\n --- tables after update --- \n',)
print(tables)



  





# 
