class Mycls:
 def __init__(self,value):
  self.value=value
 def show(self):
  print(f"Value is {self.value}")

 @property
 def show2(self):
  return self.value

obj=Mycls(34)
obj.show()