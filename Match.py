x=int(input("Enter the value of x \n"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("This is the 4th case")
    case 5:
        print("this is the fifth case")
    case 6:
        print("This is the fifth case")
    case 7:
        print("this is the 7th case")
    case _:
        print("this is the default case ")