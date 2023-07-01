#passing arguments
def smart(func):
 def inner(a,b):
  print(f"The division of two numbers is {a} and {b}")
  if b==0:
   print("Hey you can not divide")
   return

  return func(a,b)
 return inner
@smart
def smart_divide(a,b):
 print(a/b)

smart_divide(2,0)
smart_divide(35,7)
