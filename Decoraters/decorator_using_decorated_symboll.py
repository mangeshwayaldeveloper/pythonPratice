def make_pretty(funnc):
 def innner():
  print("This is the decorated function using decorator symbol")
  funnc()
 return innner

@make_pretty
def ordinary():
 print("This is the ordinary function")

ordinary()