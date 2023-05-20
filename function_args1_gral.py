'''
Python no se limita a permitirnos aceptar argumentos posicionales ilimitados; 
también nos da el poder de definir funciones con argumentos de palabras clave ilimitados. 
La sintaxis es muy similar pero utiliza dos asteriscos *args en lugar de uno. 
Por lo general, los llamamos **kwargs como una forma abreviada de argumentos de palabras clave.

Standard positional arguments
*args
Standard keyword arguments
**kwargs

As an example, this is what our function definition might look like 
if we wanted a function that printed animals utilizing all three types:

def print_animals(animal1, animal2, *args, animal4, **kwargs):
  print(animal1, animal2)
  print(args)
  print(animal4)
  print(kwargs)
We could call our function like so:

print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')
And our result would be:

Snake Fish		take the form of standard positional arguments map to animal1 and animal2
('Guinea Pig', 'Owl')	mapped to the args tuple ('Guinea Pig', 'Owl')
Cat			regular keyword arguments animal4 = Cat
{'animal5': 'Dog'}	keyword argument that is mapped to **kwargs,so the output is {'animal_5': 'Dog'}
'''
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)


#  Dict keyword names are arbitrary for desert_scoops
single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops',
	 sides='Mashed Potatoes', ice_cream_scoop1='Vanilla',
	 ice_cream_scoop2='Cookies and Cream' )

'''
*************************************************************************************************************

my_num_list = [3, 6, 9]
 
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
 
sum(*my_num_list)
**********************************************
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}
 
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
 
sum(**numbers)
**********************************************
start_and_stop = [3, 6]
 
range_values = range(*start_and_stop)
print(list(range_values))

Daría salida:
[3, 4, 5]
***********************************************
a, *b, c = [3, 6, 9, 12, 15]
 print(b)
Daría salida:
[6, 9, 12]
***********************************************
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)
Daría salida:
(0, 3, 6, 9, 12)
***********************************************
num_collection = [3, 6, 9]
 
def power_two(*nums): 
  for num in nums:
    print(num**2)
 
power_two(*num_collection)
Daría salida:
9 
36
81
**********************************************

'''