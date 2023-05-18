num = int(input("Enter a number"))
Flag = False
if (num == 0 or num == 1):
    print("The number is Niether prime or not non-prime")
elif num>1:
    for i in range(2,num):
        if (num % i == 0):
            Flag = True
            break
        else:
            Flag=False
if (Flag == False):
    print("Number is prime")
else:
    print("Number is not prime")
