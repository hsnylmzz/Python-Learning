def f():
    for i in range(5,1,-1):
        yield i**2
      
for i in f():
    print(i)

print(type(range(5,1,-1)))
