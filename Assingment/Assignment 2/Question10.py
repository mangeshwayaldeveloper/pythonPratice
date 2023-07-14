class mycls:
 def __init__(self,name):
  self.name=name

 def show(self):
  print(f"the name of the person is {self.name}")


obj=mycls("john")
obj.show()