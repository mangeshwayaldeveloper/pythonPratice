def outer(x):
 def inner(y):
  return x+y
 return inner

addition=outer(23)
result=addition(7)
print(result)