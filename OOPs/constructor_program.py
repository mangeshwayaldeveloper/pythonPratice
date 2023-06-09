class person:
 name=""
 age=""
 occ=""

 def info(selfs):
  print(f"{selfs.name} is a {selfs.age} occupation is {selfs.occ}")

a=person()
n=input("Enter Your Name")
age=input("Enter Your Age")
ocuu=input("Enter Your Occupation")
a.name=n
a.age=age
a.occ=ocuu
a.info()
