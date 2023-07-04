class mycl:
 def __init__(self,value):
  self.value=value
 def show(self):
  print(f"The value is {self.value}")

 @property
 def getter_fun(self):
  return self.value

 @getter_fun.setter
 def getter_fun(self,newValue):
  self.value=newValue

a=mycl(34)
a.show()
a.getter_fun=345
a.show()