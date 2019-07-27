girdi = input("Lütfen bi sayı gir: ")
try:
    int_girdi = int(girdi)
    print("Guzel Sayi")
except ValueError:
    print("Sayi boyle mi verilir?")