def fibonacci(n):
  if n < 0:
    raise ValueError("Input 0 or greater only!")
  fiblist = [0, 1]
  for i in range(2,n+1):
    fiblist.append(fiblist[i-1] + fiblist[i-2])
  return fiblist[n]