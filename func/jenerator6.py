def f():
    for i in range(50000000, 1, -1):
        yield i**2

for i in range(5000, 1, -1):
    pass
