from functools import reduce

numbers=[1,2,4,5,6]

sum=reduce(lambda x,y:x+y,numbers)
print(sum)