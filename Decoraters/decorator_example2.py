# this example will show the function without decorator
def fun1(func):
 def inner():
  print("This is the decorator")
  func()

 return inner


def fun2():
 print("this is second function")


fun2()
