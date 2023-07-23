def gree(fx):
 def greeting():
  print("Welcome to this function")
  fx()
  print("Thanks for using this")
 return greeting

def newf():
 print("Hey there this is the new function")

gree(newf)()