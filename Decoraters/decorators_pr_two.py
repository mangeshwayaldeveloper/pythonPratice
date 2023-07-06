import math
num=int(input("enter a numebr"))
def square(fx):
 def square_root(num):
  number=math.sqrt(num)
  print(number)
  return fx
 return square_root

@square
def add():
 print("The Square root of number is")

add(45)