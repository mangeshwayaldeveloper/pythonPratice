class Person:
 print("Hey I am a person")
 def __init__(self,n,j):
  self.name=n
  self.job=j
 def display(self):
  print(f"Hey there your name is {self.name} and you are {self.job}")

a=Person('mangesh','android developer')
a.display()