class person:
 name="mangesh"
 occupation="software developer"
 age=22
 def fun(self):
  print(f"{self.name} does {self.occupation}")

a=person()
a.name="mahesh"
a.occupation="no job"
a.age="23"

b=person()
b.name="vinay"
b.occupation="timepass"
b.age="23"

b.fun()
a.fun()
