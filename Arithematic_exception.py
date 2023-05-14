try:
    a=10/0
except Exception as e:
    print(e)

# value error
try:
    num=int(input("Enter a number"))
except ValueError:
    print("Number entered is not an integer")
