class mycls:
 def __init__(self,name):
  self.name=name
 def meth(self):
  print(f"Hey there {self.name} how are you ")

 @property
 def meth2(self):
  return "Hello "+self.name

obj=mycls("Mangesh")
print(obj.meth2)