a=int(input("Enter First Number\n"))
b=int(input("Enter Second Number\n"))
c=int(input("Enter Third Number\n"))
str="this is the greatest number"
if(a>b):
    if(a>c):
        print(str.title(),a)
    else:
        print(str.title(),c)
elif(b>c):
        print(str.title(),b)
else:
    print(str.title(),c)