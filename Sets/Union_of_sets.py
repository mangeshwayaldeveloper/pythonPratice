a={2,35,6,7,4,6,8,20,30}
a2={"mangesh",23,35,45,42}
print(a.union(a2))

#updating the values of the set
a.update(a2)
print("This will update the element of one set from another set",a)
print("this will not print the all element of the two sets\n  because we not update this set",a2)