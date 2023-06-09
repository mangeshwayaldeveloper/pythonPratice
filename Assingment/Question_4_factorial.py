a = int(input("Ente a number"))


def factorial(num):
 if num == 1:
  return 1
 else:
  fact = num * factorial(num - 1)
  return fact

print("The Factorial of ",a ,"is ",end='')
print(factorial(a))
