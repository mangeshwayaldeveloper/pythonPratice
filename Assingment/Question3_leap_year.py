def isLeap(year):
 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  return True
 else:
  return False


year = int(input("Enter a number"))
if isLeap(year):
 print(year, "Is a leap year")
else:
 print(year, "Is not a leap year")
