def greet(fn):
 def greeting(*args, **kwargs):
  print("Hey Hi There")
  fn(*args, **kwargs)
  print("Thank you for using")
 return greeting


def add(a, b):
 print(a + b)


greet(add)(4,5)