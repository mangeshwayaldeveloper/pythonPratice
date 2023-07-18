def gen():
 for i in range(90):
  yield i

var=gen()
print(next(var))
print(next(var))