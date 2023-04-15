# fibonacii program with recursion
a=int(input("Enter a number"))
def fibo(n):
    if(n<0):
        return 1
    else:
        fib=fibo(n-2)+fibo(n-1)
        return fib

print(fibo(a))