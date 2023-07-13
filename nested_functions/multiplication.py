
def outer(y):
 s=90
 def inner(x):
  return x+y+s
 return inner

add=outer(45)
result=add(5)
print(result)