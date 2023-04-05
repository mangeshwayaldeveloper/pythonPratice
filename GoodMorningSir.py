import time
timestamp=time.strftime('%H')
a=int(22)
if(a<16 & a>12):
    print("Good Afternoon Sir",timestamp)
elif(a>16 & a<21):
    print("Good Evening Sir",timestamp)
elif(a>21 & a<6):
    print("Good Night Sir",timestamp)
else:
    print("Good Morning Sir")