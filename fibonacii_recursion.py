def fibo(n):
    if(n<0):
        return 0
    else:
        n=n+fibo(n-1)
    return n
print(fibo(5))
