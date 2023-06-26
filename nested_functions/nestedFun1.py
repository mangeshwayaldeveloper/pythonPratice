def outer():
 print("The outer function")
 def inner():
  print("This is the function inside of the another function")
  print("The inner function")
 return inner()
outer()