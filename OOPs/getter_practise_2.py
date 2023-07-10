class Myclass:
 def __init__(self, value):
  self.value = value

 def show(self):
  print(f"The value is {self.value}")


 @property
 def ten_value(self):
  return 120 * self.value


obj = Myclass(23)
obj.show()
print(obj.ten_value)
