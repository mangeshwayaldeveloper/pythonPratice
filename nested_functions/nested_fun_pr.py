def outer(x):
 def inner(y):
  return x+y
 return inner

add=outer(34)
result=add(16)
print(result)
