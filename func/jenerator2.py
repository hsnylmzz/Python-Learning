def f():
    for i in range(5,1,-1):
        yield i
      
for i in f():
    print(i)
