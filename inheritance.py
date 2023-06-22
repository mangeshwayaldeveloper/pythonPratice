class emp:
 def __init__(self,name,id):
  self.name=name
  self.id=id
  def show(self):
   print(f"the {self.name} and id is{self.id}")

class prog(emp):
 def showdet(self):
  print("this is the inehrited class")

e=emp('m',23)
e2=prog("mangesh",22)
e2.showdet()
