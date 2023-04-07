# program to print the Reverse numbers
a=int(input("Enter a 3 digit number"))
num=0
while a>0:
    rem=a%10
    num=num*10+rem
    a=int(a/10)
print(num)