p={11:23,22:5,33:43,44:11}
s={10:2,20:3,30:4,40:5}
s.update(p)
print(s)

s.clear()
print(s)

p.pop(11)
print(p)

p.popitem()
print(p)