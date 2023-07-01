def first(funx):
 def inner(*args,**kwargs):
  print("*"*15)
  funx(*args,**kwargs)
  print("%"*15)
 return inner

def second(func):
 def inner(*args,**kwargs):
  print("%"*15)
  func(*args,**kwargs)
  print("%"*15)
 return inner

@first
@second
def outer(msg):
 print(msg)

outer("Hello")