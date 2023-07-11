class employee:
 def __init__(self, name, id):
  self.name = name
  self.id = id

 def showDetails(self):
  print(f"the name of the employee:{self.name} and the id is {self.id}")


class Programmer(employee):
 def showLanguage(self):
  print("The Lanugage is the child class method")


o = employee("Mangesh", 23)
o.showDetails()
o2 = Programmer("Rushikesh",7)
o2.showDetails()
o2.showLanguage()
