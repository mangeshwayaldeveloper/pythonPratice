f=open('marks.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Makrs of the Student {i} In Maths={m1}")
    print(f"Makrs of the Student {i} In Maths={m2}")
    print(f"Makrs of the Student {i} In Maths={m3}")