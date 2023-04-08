tup=(1,3,5,6)
print(type(tup),tup)

#this will not create a tuple
tup=(1)
print(tup)
#-----------------------------
# correct way to print the single element in the tuple is
tup=(1,)
print(tup)
# tuple indexing
tup=(2,4,6,4,2,8)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])

# Negative indexing
print("Printing the negative index")
print(tup[len(tup)-2])
print(tup[-2])
print(tup[6-2])

if 2 in tup:
    print(2,"Yes it is present")

# slicing is not possible in tuples instead of slicing it will create a new tuple
print(tup[2:5])