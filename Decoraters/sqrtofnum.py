def fun(fx):
 def tt(*args,**kwargs):
  print("This is the entry")
  fx(*args,**kwargs)
  print("the exit")
 return tt

@fun
def sums(a,n):
 print(a+n)

sums(23,42)