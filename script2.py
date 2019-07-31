def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b


fonks = smart_divide(divide(3,7))
result = divide(3,4)
print(fonks)
