def armstrong(number):
 no = str(number)
 l = len(no)
 armstrong_num = sum(int(i) ** l for i in no)
 if armstrong_num == number:
  return True
 else:
  return False

num =int(input("Enter a number"))
if armstrong(num):
 print(num, "Is Armstrong Number")
else:
 print(num, "Not Armstrong")
