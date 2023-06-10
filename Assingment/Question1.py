def check_even_odd(number):
 if number % 2 == 0:
  print(number, "is even.")
 else:
  print(number, "is odd.")


def check_prime(number):
 if number <= 1:
  print(number, "is not prime.")
  return

 for i in range(2, int(number ** 0.5) + 1):
  if number % i == 0:
   print(number, "is not prime.")
   return

 print(number, "is prime.")


number = int(input("Enter a number: "))

check_even_odd(number)

check_prime(number)
