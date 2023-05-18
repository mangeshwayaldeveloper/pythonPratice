num=int(input("Enter a number"))
Flag=True
if (num==0 or num==1):
    print("The number is Niether prime or not non-prime")
else:
    for i in range(1,num):
        if(num%i==0):
            Flag=False
if(Flag==True):
    print("Number is prime")
else:
    print("Number is not prime")