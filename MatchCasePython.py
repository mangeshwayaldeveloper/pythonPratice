a=int(input("Enter a number"))
match a:
    case 1:
          print("This is number 1")
    case 2:
        print("This is hte number 2")
    case 3:
        print("this is the case 3")
    case _:
        print("This is the default number",a)
