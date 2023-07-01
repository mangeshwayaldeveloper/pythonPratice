def first(funx):
 def inner(*args,**kwargs):
  print("#"*15)
  funx(*args,**kwargs)
  print("%"*15)
 return inner

def second(fux):
 def inner(*args,**kwargs):
  print("%"*15)
  fux(*args,**kwargs)
  print("%"*15)
 return inner

@first
@second
def last(msg):
 print(msg)

last("Mangesh")