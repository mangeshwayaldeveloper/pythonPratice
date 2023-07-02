class Myclass:
 def __init__(self,value):
  self.value=value
 def show(self):
  print(f"The value is {self.value}")

 @property
 def ten_value(self):
  return 10*self.value

a=Myclass(10)
print(a.ten_value)