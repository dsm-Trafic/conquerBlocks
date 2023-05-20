primos = []
for x in range(2,101):
    primo = all(x % i != 0 for i in range(2, x))
    if primo : primos.append(x)
           
print(primos)