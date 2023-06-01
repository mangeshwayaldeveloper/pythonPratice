from functools import reduce

num = int(input("Enter a number"))
for i in range(num):
 l = []

fibo = reduce(lambda x, y: x + y, l)
print(fibo)