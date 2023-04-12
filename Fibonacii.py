f=int(input("Enter a number"))
n=0
n1=1
fibo=0
for i in range (f):
    fibo=n+n1
    n=n1
    n1=fibo
    print(fibo)
