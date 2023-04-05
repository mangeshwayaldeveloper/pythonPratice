def CalculationOfMean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
CalculationOfMean(10,2)
CalculationOfMean(20,10)
CalculationOfMean(9,8)
CalculationOfMean(8,7)

#functions to find greatest person among two
def greaterAge(age1,age2):
    if(age1>age2):
        print("The Greates Age Among Two Person Is",age1)
    elif(age1==age2):
        print("Both Ages Are Same")
    else:
        print("absolutely greater age is ",age2)

age1=int(input("Enter Age Of Person 1\n"))
age2=int(input("Enter Age Of Person 2\n"))

greaterAge(age1,age2)
greaterAge(45,23)