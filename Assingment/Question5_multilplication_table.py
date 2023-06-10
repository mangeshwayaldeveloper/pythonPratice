a = int(input("Enter a number"))


def multiplication(num):
 if a == 0:
  return 0
 elif a > 0:
  for i in range(1, 11):
   print(a, "X", i, "=", a * i)


print(multiplication(a))
