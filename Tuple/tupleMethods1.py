a=(4,"Mangesh",5,"Pavan",6,"Rushikesh")
m=list(a)
m.insert(4,7)
m.append(8)
print(type(a))

a=tuple(m)
print(type(a),a)