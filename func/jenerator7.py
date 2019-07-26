def f():
    for i in range(100, 1, -1):
        yield i**2

for i in f():
    if i == 2500:
        print("bitti")

