def fun(sx):
 def fun2():
  print("This is the second function")
 sx()
 return fun2

@fun
def fun3():
 print("This is the fun 3")

fun3()