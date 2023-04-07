l=[12,4,3,52,3,54,3,2,4,7,8,9,90]
print(l)
m=l  #this will not create a seperate copy of the list
# this will only create new referece for the list
m[12]=100
# print(len(l))
print(l)
#---------------------------copying elements---------------------------------------

l=[2,4,7,4,6,8,9,10,11,121,13]
m=l.copy()
m[0]=23
print(l)
print(m)

