kilo = int(input("Kilonuz : "))
boy = float(input("Boyunuz : "))

bki = kilo /(boy * boy)

if bki < 18:
    print("Zayıf")
elif bki >= 18 and bki < 25:
    print("Normal")
elif bki >= 25 and bki < 30:
    print("Fazla Kilolu")
elif bki > 30:
    print("Obez")
