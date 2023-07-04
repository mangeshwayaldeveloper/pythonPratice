class Myclass:
 def __init__(self,value):
  self.value=value
 def show(self):
  print(f"The value is {self.value}")

 @property
 def ten_value(self):
  return 10*self.value

 @ten_value.setter
 def ten_value(self,new_value):
  self.value=new_value


a=Myclass(10)
print(a.ten_value)
a.ten_value=345
print(a.value)