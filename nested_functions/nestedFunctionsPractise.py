def outer(y):
 def inner(x):
  return x*y
 return inner

add=outer(34)
result=add(2)
print(result)