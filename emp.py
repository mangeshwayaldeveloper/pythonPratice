class emp:
 hour = 0
 grosspay = 0

 def pay(hour):
  if (hour == 8):
   print("the gross pay is 1500")
  elif (hour < 8):
   grosspay = hour * 75
   print("The gross pay is ", grosspay)
  elif (hour > 8):
   grosspay = 1500 + (hour - 8) * 75
   print("The gross pay is", grosspay)
  else:
   print("Invalid Input")


h = int(input("Enter No. of Hours"))

o = emp()
o.pay()
