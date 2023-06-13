class person:
 def __init__(self,name,occ):
  self.occ = occ
  self.name = name

  print("Hey I am person ")

 def inf(self):
  print(f"{self.name} is a {self.occ}")

a=person("mangesh","developer")
a.inf()