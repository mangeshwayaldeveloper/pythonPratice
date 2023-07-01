def outer(y):
 def inner(x):
  return x*y
 return inner

add=outer(45)
result=add(5)
print(result)