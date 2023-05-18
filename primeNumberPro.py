num = int(input("Enter a number"))
for i in range(num):
    if (num % (i + 1) == 0):
        print("Number is not prime")
    else:
        print("The Number is prime")
