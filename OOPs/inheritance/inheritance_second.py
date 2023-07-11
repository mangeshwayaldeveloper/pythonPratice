class parent:
 def __init__(self,name,rollno):
  self.name=name
  self.rollno=rollno
 def meth(self):
  print(f"the name of the person is {self.name} and the roll number is {self.rollno}")

class child(parent):
 def meths(self):
  print(f"The name of student is {self.name} and the PRN is {self.rollno}")

obj=parent("mangehs",234)
obj2=child("Ashish",666)
obj.meth()
obj2.meth()
obj2.meths()