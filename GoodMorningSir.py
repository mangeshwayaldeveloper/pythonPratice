import time

hours = int(time.strftime('%H'))

if hours >= 0 and hours < 12:
    print("Good Morning Sir", hours)
elif hours >= 12 and hours < 17:
    print("Good Evening Sir", hours)
elif hours >= 17 and hours < 0:
    print("Good Night Sir", hours)
else:
    print("Good Morning Sir")
