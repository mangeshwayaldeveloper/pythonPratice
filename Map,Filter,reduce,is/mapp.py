# manual process to print cube of given list
def cube(x):
 return x * x * x


l = [2, 3, 4, 5, 6]
newl = []
for item in l:
 newl.append(cube(item))
print("Manual Approach To print List",newl)


f=lambda x:x**2
l=[2,4,5,6,7]
newl=list(map(f,l))
print("Modern Approach",newl)
