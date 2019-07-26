def fibonacci(num):
    if num == 0:
        return 0
    
    elif num == 1:
        return 1
    
    else :
        sonuc = fibonacci(num-2) + fibonacci(num-1)
        return sonuc
print(fibonacci(8))
