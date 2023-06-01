from functools import reduce

l = []
num = int(input("Enter a number"))
for i in range(num+1):
 l.append(i)


fibo = reduce(lambda x, y: x + y, l)
print(fibo)