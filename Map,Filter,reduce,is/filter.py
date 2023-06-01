l=[1,2,4,5,67,8,5,45,90]
def filter_fun(a):
  return a>5

newl=list(filter(filter_fun,l))
print(newl)