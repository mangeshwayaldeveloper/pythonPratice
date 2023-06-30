def make_pretty(func):
 def inner():
  print("I am decorated")
  func()
 return inner

def ordinary_function():
 print("this is the ordinary function")

#lets created decorator function with method 1
decorated_func=make_pretty(ordinary_function)
decorated_func()