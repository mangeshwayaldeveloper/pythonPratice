import math

i = int(input("Enter a number "))
def multiplication(func):
 def wrapper():
  for f in range(10):
   print(f*i)
  func()
 return wrapper()

@multiplication
def sqare():
 print(math.sqrt(i))
