import math
def factorial(n):
 if n==1:
  return 1
 elif n>1:
  f=n*factorial(n-1)
  return f

num=float(input("Enter a number "))
sqrt=math.sqrt(num)

fact=factorial(int(sqrt))
print(f"The Square root of {num} is {sqrt} and factorial is {fact}")