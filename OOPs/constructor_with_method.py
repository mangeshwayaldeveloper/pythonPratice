class myclass:
 name=""
 age=23
 address="pune"
 def __init__(self,name,age,address):
  self.name=name
  self.age=age
  self.address=address
 def methd(self):
  print(f"hello {self.name} are you {self.age} year old and from{self.address}")

a=myclass("mangesh",23,"pune")
a.methd()