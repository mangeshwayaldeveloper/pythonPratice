def fun():
    try:
        l=[1,2,4,52,12]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error will be occured")
        return 0
    finally:
        print("this will always be executed")
x=fun()
print(x)