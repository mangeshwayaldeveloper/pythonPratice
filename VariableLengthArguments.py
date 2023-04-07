def varArgs(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("The sum of the numbers is",sum)

varArgs(4,5,3,6,3)