import logging
def log_function(func):
 def decorated(*args,**kwargs):
  logging.info(f"calling{func.__name__} with args={args}, kwargs={kwargs}")
  result=func(*args,**kwargs)
  logging.info(f"{func.__name__}returned {result}")
  return result
 return decorated

@log_function
def myFunction(a,b):
 return a+b

myFunction(3,4)